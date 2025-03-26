# Kalkulator Nilai Akhir Mahasiswa

## Deskripsi Program

Kalkulator Nilai Akhir Mahasiswa adalah sebuah program yang digunakan untuk menghitung nilai akhir mahasiswa berdasarkan beberapa komponen penilaian, serta menentukan grade dan status kelulusan. Program ini juga menampilkan statistik dari seluruh nilai mahasiswa yang dimasukkan (mean dan median). Program ini dibuat untuk memenuhi tugas Praktikum Kecerdasan Buatan pertemuan ke-3.

## Fitur Aplikasi

1. Menghitung nilai akhir berdasarkan nilai kuis, UTS, UAS, dan proyek.
2. Menentukan grade berdasarkan nilai akhir.
3. Menampilkan status kelulusan dengan (lulus atau mengulang).
4. Menampilkan daftar nilai mahasiswa yang telah diinputkan.
5. Menampilkan statistik nilai akhir:
   - Jumlah mahasiswa
   - Rata-rata nilai akhir
   - Median nilai akhir
   - Nilai tertinggi
   - Nilai terendah

## Tech Stack

Program ini dibuat menggunakan bahasa Python dengan struktur data dictionary untuk menyimpan informasi nilai mahasiswa. Untuk struktur kontrol, digunakan perulangan while True agar pengguna dapat memasukkan data sebanyak mungkin, serta percabangan if-elif-else untuk menentukan grade dan status kelulusan mahasiswa.

Library yang digunakan dalam program ini meliputi:
- **statistics**, digunakan untuk perhitungan statistik seperti rata-rata dan median.
- **colorama**, digunakan untuk memberikan warna pada output teks di agar mempermudah identifikasi status kelulusan.
- **sys**, digunakan untuk menghentikan program setelah seluruh proses selesai.

## Cara Install

1. Clone repository ini atau download file .py.
2. Pastikan Python sudah terinstall di perangkat Anda.
3. Install library colorama dengan menjalankan perintah:
   ```sh
   pip install colorama
4. Jalankan program pada Code Editor dengan perintah:
   ```sh
   python Tugas-2-Praktikum-KB.py.py
   
