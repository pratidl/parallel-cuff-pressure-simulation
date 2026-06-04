import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count


def generate_pressure_signal(total_data=1_000_000):
    """
    Membuat simulasi data tekanan cuff.
    Sinyal dibuat menurun seperti proses deflasi cuff,
    lalu ditambahkan osilasi dan noise.
    """
    x = np.linspace(0, 10, total_data)

    cuff_pressure = 180 - (12 * x)
    oscillation = 5 * np.sin(2 * np.pi * 2 * x)
    noise = np.random.normal(0, 1.5, total_data)

    signal = cuff_pressure + oscillation + noise
    return signal


def moving_average(data, window_size=50):
    """
    Melakukan smoothing sederhana menggunakan moving average.
    """
    kernel = np.ones(window_size) / window_size
    return np.convolve(data, kernel, mode="same")


def process_chunk(chunk):
    """
    Fungsi pemrosesan untuk setiap chunk data.
    """
    filtered = moving_average(chunk)
    peaks = np.where(filtered > np.mean(filtered))[0]
    return len(peaks)


def serial_processing(data):
    """
    Pemrosesan data secara serial.
    """
    return process_chunk(data)


def parallel_processing(data):
    """
    Pemrosesan data secara paralel.
    Data dibagi berdasarkan jumlah CPU core.
    """
    cores = cpu_count()
    chunks = np.array_split(data, cores)

    with Pool(cores) as pool:
        results = pool.map(process_chunk, chunks)

    return sum(results)


def estimate_blood_pressure(signal):
    """
    Estimasi sederhana systolic dan diastolic berdasarkan nilai sinyal.
    Ini bukan diagnosis medis, hanya simulasi project komputasi.
    """
    systolic = np.percentile(signal, 90)
    diastolic = np.percentile(signal, 40)

    return round(systolic, 2), round(diastolic, 2)


def save_pressure_graph(signal):
    plt.figure(figsize=(10, 5))
    plt.plot(signal[:5000])
    plt.title("Simulated Cuff Pressure Signal")
    plt.xlabel("Sample")
    plt.ylabel("Pressure Value")
    plt.tight_layout()
    plt.savefig("assets/pressure_signal.png")
    plt.close()


def save_runtime_graph(serial_time, parallel_time):
    methods = ["Serial", "Parallel"]
    times = [serial_time, parallel_time]

    plt.figure(figsize=(7, 5))
    plt.bar(methods, times)
    plt.title("Runtime Comparison")
    plt.xlabel("Processing Method")
    plt.ylabel("Time (seconds)")
    plt.tight_layout()
    plt.savefig("assets/runtime_comparison.png")
    plt.close()


def main():
    print("Parallel Cuff Pressure Signal Processing Simulation")
    print("Generating signal data...")

    data = generate_pressure_signal()

    print("Running serial processing...")
    start = time.time()
    serial_result = serial_processing(data)
    serial_time = time.time() - start

    print("Running parallel processing...")
    start = time.time()
    parallel_result = parallel_processing(data)
    parallel_time = time.time() - start

    systolic, diastolic = estimate_blood_pressure(data)

    speedup = serial_time / parallel_time if parallel_time > 0 else 0

    print("\n=== Result ===")
    print(f"Serial result       : {serial_result}")
    print(f"Parallel result     : {parallel_result}")
    print(f"Serial time         : {serial_time:.4f} seconds")
    print(f"Parallel time       : {parallel_time:.4f} seconds")
    print(f"Speedup             : {speedup:.2f}x")
    print(f"Estimated systolic  : {systolic}")
    print(f"Estimated diastolic : {diastolic}")

    save_pressure_graph(data)
    save_runtime_graph(serial_time, parallel_time)

    print("\nGraphs saved to assets folder.")


if __name__ == "__main__":
    main()