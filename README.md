# Simulasi Pemrosesan Sinyal Tekanan Cuff Secara Paralel

## Gambaran Project

Project ini merupakan simulasi pemrosesan sinyal tekanan cuff menggunakan Python. Program ini membuat data tekanan sintetis yang terinspirasi dari sistem pengukuran tekanan darah, lalu data tersebut diproses menggunakan dua metode, yaitu metode serial dan metode paralel.

Tujuan utama dari project ini adalah menunjukkan penerapan konsep komputasi paralel pada proses pengolahan data sinyal.

## Latar Belakang

Dalam sistem pengukuran tekanan darah, data tekanan dari cuff dapat diproses untuk menganalisis pola sinyal. Jika jumlah data yang diproses cukup besar, komputasi paralel dapat digunakan untuk membagi beban kerja menjadi beberapa bagian kecil agar dapat diproses secara bersamaan.

Project ini terinspirasi dari konsep CuffnCode, tetapi hanya berfokus pada bagian logic code dan simulasi pemrosesan data.

## Fitur Program

- Membuat simulasi sinyal tekanan cuff
- Menambahkan osilasi dan noise pada sinyal
- Memproses sinyal menggunakan metode serial
- Memproses sinyal menggunakan metode paralel
- Membandingkan waktu eksekusi antara metode serial dan paralel
- Membuat grafik sinyal tekanan
- Membuat grafik perbandingan waktu eksekusi
- Mengestimasi nilai systolic dan diastolic menggunakan perhitungan statistik sederhana

## Konsep Komputasi Paralel

Pada metode paralel, data dibagi menjadi beberapa bagian berdasarkan jumlah core CPU yang tersedia. Setiap bagian data diproses oleh proses yang berbeda menggunakan library multiprocessing pada Python.

Setelah semua bagian data selesai diproses, hasil dari setiap proses digabungkan menjadi satu hasil akhir.

## Struktur Project

```text
parallel-cuff-pressure-simulation/
├── main.py
├── requirements.txt
├── README.md
├── docs/
│   └── index.html
└── assets/
    ├── pressure_signal.png
    └── runtime_comparison.png