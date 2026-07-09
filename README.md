# 🧮 Kalkulator Pintar GUI (Python & Tkinter)

Aplikasi kalkulator desktop sederhana namun bertenaga yang dibangun menggunakan bahasa pemrograman Python dan pustaka antarmuka grafis **Tkinter**. Proyek ini dirancang menggunakan pendekatan **Object-Oriented Programming (OOP)** untuk memastikan struktur kode yang bersih, rapi, dan mudah dikembangkan.

## ✨ Fitur Utama

- **Antarmuka Responsif & Rapi:** Menggunakan sistem tata letak `.grid()` untuk menyusun tombol secara simetris layaknya kalkulator fisik.
- **Operasi Matematika Lengkap:** Mendukung penjumlahan (`+`), pengurangan (`-`), perkalian (`x`), dan pembagian (`/`).
- **Fitur Spesial Lanjutan:**
  - `Backspace (<=)`: Menghapus satu karakter terakhir dari belakang secara dinamis menggunakan teknik *string slicing*.
  - `Clear All (AC)`: Mengosongkan seluruh layar input dalam satu klik.
  - `Persen (%)`: Menghitung nilai persentase secara otomatis dengan konversi *pembagian 100* di latar belakang.
  - `Toggle Positif/Negatif (+/-)`: Mengubah angka di layar menjadi minus (`-`) atau sebaliknya secara instan.
- **Sistem Penerjemah Karakter:** Pengguna tetap melihat simbol ramah visual seperti `x` dan `,`, sementara sistem otomatis menerjemahkannya menjadi `*` dan `.` agar dapat diproses oleh mesin eksekusi Python.
- **Keamanan Input (Error Handling):** Dilengkapi blok `try-except` untuk mencegah aplikasi *crash* jika terjadi pembagian dengan angka nol (*Division by Zero*) atau kesalahan sintaks matematika (*Syntax Error*).

## 🚀 Prasyarat

Sebelum menjalankan aplikasi ini, pastikan komputer Anda sudah terinstal:
- **Python 3.x**

Aplikasi ini murni menggunakan pustaka bawaan Python (`tkinter`, `random`, `json`), sehingga Anda tidak perlu menginstal pustaka eksternal tambahan untuk menjalankannya secara lokal.

## 📦 Cara Menjalankan Aplikasi

1. Unduh atau salin file kode utama (misalnya bernama `Kalkulator.py`).
2. Buka Terminal atau Command Prompt (CMD) di folder tempat file tersebut berada.
3. Jalankan perintah berikut:
   ```bash
   python Kalkulator.py
