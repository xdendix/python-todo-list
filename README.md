# 📝 To-Do List CLI dengan Python

Proyek sederhana **To-Do List** berbasis **Command Line Interface (CLI)** menggunakan Python.  
Data tugas disimpan dalam file **JSON** sehingga tidak hilang saat program ditutup.

---

## 📦 Requirements
- Python **3.8+**
- Tidak perlu library tambahan (hanya modul bawaan Python: `json`, `os`)

---

## 📌 Fitur
- Melihat daftar tugas
- Menambah tugas baru
- Menghapus tugas
- Menyimpan data otomatis ke `todos.json`
- Memuat kembali data saat program dijalankan ulang
- Validasi input & konfirmasi saat menghapus tugas

---

## 🛠️ Instalasi & Menjalankan
1. Clone repository ini:
   ```bash
   git clone https://github.com/username/python-todo-list.git
   cd python-todo-list
2. Jalankan Program:
   python main.py

## 🚀 Cara Menggunakan
========== To-Do-List ==========
1. Tampilkan Tugas
2. Tambah Tugas
3. Hapus Tugas
4. Keluar
   
Pilih 1 → menampilkan daftar tugas
Pilih 2 → menambahkan tugas baru
Pilih 3 → menghapus tugas (dengan konfirmasi)
Pilih 4 → keluar dari program

## 💾 Penyimpanan Data
- Semua tugas disimpan otomatis ke file todos.json
- Contoh isi file todos.json:

[  
  "Belajar Python,
  "Baca buku",
  "Main game"
]

## 📸 Preview
========== To-Do-List ==========
1. Tampilkan Tugas
2. Tambah Tugas
3. Hapus Tugas
4. Keluar

Masukkan pilihan: 2
Masukkan tugas hari ini: Belajar Python

Belajar Python berhasil ditambahkan dan disimpan.
