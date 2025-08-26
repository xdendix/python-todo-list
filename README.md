# 📝 To-Do List CLI dengan Python

Proyek **To-Do List** berbasis Command Line Interface (CLI) menggunakan Python.  
Data tugas disimpan dalam file **JSON** sehingga tidak hilang saat program ditutup.  
Dengan tampilan tabel rapi menggunakan **tabulate** dan pengalaman pengguna yang lebih baik.

---

## 📦 Requirements
- Python 3.8+
- Library tambahan:
  - [tabulate](https://pypi.org/project/tabulate/) (untuk tampilan tabel)

---

## 📌 Fitur
- ✅ Menambah tugas baru dengan prioritas (High/Medium/Low)
- ✅ Mengubah tugas yang sudah ada
- ✅ Mengubah prioritas tugas
- ✅ Menghapus tugas (dengan konfirmasi)
- ✅ Melihat daftar tugas dalam bentuk tabel yang terurut berdasarkan prioritas
- ✅ Menandai / membatalkan status tugas (selesai atau belum selesai)
- ✅ Menyimpan data otomatis ke `todos.json`
- ✅ Memuat kembali data saat program dijalankan ulang
- ✅ **Validasi input yang lebih baik** untuk mencegah error
- ✅ **Penanganan error yang konsisten** dengan pesan yang informatif
- ✅ **UI/UX yang lebih baik** dengan menu yang jelas dan responsif

---

## 🛠️ Instalasi & Menjalankan
1. Clone repository ini:
   ```bash
   git clone https://github.com/xdendix/python-todo-list.git
   cd todo-list
   ```
2. Buat virtual environment (opsional tapi disarankan):
   ```bash
   python -m venv todo-list
   source todo-list/bin/activate   # Linux/Mac
   # atau
   todo-list\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan program:
   ```bash
   python main.py
   ```

---

## 🚀 Cara Menggunakan

```
========== To-Do List ==========

1. Tambah Tugas
2. Ubah Tugas
3. Ubah Prioritas
4. Hapus Tugas
5. Lihat Tugas
6. Tandai / Batalkan Status Tugas
7. Keluar
```

- **Pilih 1** → Menambah tugas baru dengan opsi prioritas (High/Medium/Low)
- **Pilih 2** → Mengubah judul tugas yang sudah ada
- **Pilih 3** → Mengubah prioritas tugas (High/Medium/Low)
- **Pilih 4** → Menghapus tugas (dengan konfirmasi y/n)
- **Pilih 5** → Melihat semua tugas dalam bentuk tabel yang terurut
- **Pilih 6** → Menandai atau membatalkan status tugas (selesai/belum selesai)
- **Pilih 7** → Keluar dari program

**Fitur UI/UX yang ditingkatkan:**
- Tabel tugas diurutkan berdasarkan prioritas (High → Medium → Low)
- Pesan error yang jelas dan informatif
- Validasi input untuk mencegah crash aplikasi
- Konfirmasi sebelum operasi penghapusan

---

## 💾 Penyimpanan Data
- Semua tugas disimpan otomatis ke file `todos.json`
- Format data yang disimpan:
```json
[
  {
    "judul": "Belajar Python",
    "status": false,
    "prioritas": "High"
  },
  {
    "judul": "Belanja Harian", 
    "status": true,
    "prioritas": "Medium"
  }
]
```

---

## 📸 Preview
```
Daftar Tugas: 
+----+--------+-----------------+------------+
| No | Status | Judul           | Prioritas  |
+====+========+=================+============+
|  1 | ❌     | Belajar Python  | High       |
+----+--------+-----------------+------------+
|  2 | ✔️     | Belanja Harian | Medium     |
+----+--------+-----------------+------------+
|  3 | ❌     | Kerjakan PR     | Low        |
+----+--------+-----------------+------------+
```

---

## 🎯 Contoh Penggunaan
1. **Menambah tugas**: Pilih 1 → "Meeting penting" → Prioritas "High"
2. **Mengubah prioritas**: Pilih 3 → Pilih nomor tugas → "Medium"
3. **Menandai selesai**: Pilih 6 → Pilih nomor tugas → Status berubah menjadi ✔️
4. **Validasi error**: Input nomor di luar range → "Error: Nomor tugas tidak valid"

