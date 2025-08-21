# 📝 To-Do List CLI dengan Python

Proyek **To-Do List** berbasis Command Line Interface (CLI) menggunakan Python.  
Data tugas disimpan dalam file **JSON** sehingga tidak hilang saat program ditutup.  
Dengan tampilan tabel rapi menggunakan **tabulate**.

---

## 📦 Requirements
- Python 3.8+
- Library tambahan:
  - [tabulate](https://pypi.org/project/tabulate/) (untuk tampilan tabel)

---

## 📌 Fitur
- Menambah tugas baru
- Mengubah tugas yang sudah ada
- Menghapus tugas (dengan konfirmasi)
- Melihat daftar tugas dalam bentuk tabel
- Menandai / membatalkan status tugas (selesai atau belum selesai)
- Menyimpan data otomatis ke `todos.json`
- Memuat kembali data saat program dijalankan ulang
- Validasi input agar tidak error

---

## 🛠️ Instalasi & Menjalankan
1. Clone repository ini:
   ```bash
   git clone https://github.com/xdendix/python-todo-list.git
   cd todo-list
2. Buat virtual environment (opsional tapi disarankan):
   - python -m venv todo-list
   - source todo-list/bin/activate   # Linux/Mac
   - todo-list\Scripts\activate      # Windows

3. Install dependencies:
   - pip install -r requirements.txt

4. Jalankan program:
   - python main.py
---

## 🚀 Cara Menggunakan
========== To-Do List ==========

1. Tambah Tugas
2. Ubah Tugas
3. Hapus Tugas
4. Lihat Tugas
5. Tandai / Batalkan Status Tugas
6. Keluar
   
- Pilih 1 → menambah tugas baru
- Pilih 2 → mengubah tugas (judul)
- Pilih 3 → menghapus tugas (ada konfirmasi)
- Pilih 4 → melihat semua tugas dalam bentuk tabel
- Pilih 5 → menandai atau membatalkan status tugas (selesai/belum selesai)
- Pilih 6 → keluar dari program

---

## 💾 Penyimpanan Data
- Semua tugas disimpan otomatis ke file todos.json
- Contoh isi file todos.json:
  ```bash
  [
    {"judul": "Belajar Python", "status": false},
    {"judul": "Belanja Harian", "status": true}
  ]

---

## 📸 Preview
Daftar Tugas:
  ```bash
  +----+--------+-----------------+------------+
  | No | Status | Judul           | Prioritas  |
  +----+--------+-----------------+------------+
  |  1 | ❌     | Belajar Python  | -          |
  |  2 | ✔️     | Belanja Harian | -          |
  |  3 | ❌     | Kerjakan PR     | -          |
  +----+--------+-----------------+------------+

