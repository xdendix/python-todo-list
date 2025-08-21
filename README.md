# 📝 To-Do List CLI dengan Python

Proyek sederhana **To-Do List** berbasis Command Line Interface (CLI) menggunakan Python.  
Data tugas disimpan dalam file **JSON** sehingga tidak hilang saat program ditutup.  
Dengan tampilan tabel rapi menggunakan **tabulate**.

---

## 📦 Requirements
- Python 3.8+
- Library tambahan:
  - [tabulate](https://pypi.org/project/tabulate/) (untuk tampilan tabel)

---

## 📌 Fitur
- Melihat daftar tugas dalam bentuk tabel
- Menambah tugas baru
- Menghapus tugas
- Mengubah tugas
- Menandai status tugas (selesai / belum selesai)
- Menyimpan data otomatis ke `todos.json`
- Memuat kembali data saat program dijalankan ulang
- Validasi input & konfirmasi saat menghapus tugas
- (Coming soon) Prioritas tugas (High/Medium/Low)
- (Coming soon) Deadline tugas

---

## 🛠️ Instalasi & Menjalankan
1. Clone repository ini:
   ```bash
   git clone https://github.com/xdendix/python-todo-list.git
   cd todo-list
2. Jalankan Program:
   python main.py

---

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

---

## 💾 Penyimpanan Data
- Semua tugas disimpan otomatis ke file todos.json
- Contoh isi file todos.json:

[
    "Belajar Python",
    "Baca buku",
    "Main game"
]

---

## 📸 Preview
========== To-Do-List ==========
1. Tampilkan Tugas
2. Tambah Tugas
3. Hapus Tugas
4. Keluar

Masukkan pilihan: 2
Masukkan tugas hari ini: Belajar Python

Belajar Python berhasil ditambahkan dan disimpan.
