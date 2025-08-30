# 📝 To-Do List CLI dengan Python

Proyek **To-Do List** berbasis Command Line Interface (CLI) menggunakan Python.  
Data tugas disimpan dalam file **JSON** sehingga tidak hilang saat program ditutup.  
Dengan tampilan tabel rapi menggunakan **tabulate** dan pengalaman pengguna yang lebih baik.

**✨ Fitur Baru:** Implementasi class-based dengan `TodoManager` untuk struktur kode yang lebih terorganisir dan mudah dikembangkan.

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
- ✅ Mengubah deadline tugas (format YYYY-MM-DD)
- ✅ Menghapus tugas (dengan konfirmasi)
- ✅ Melihat daftar tugas dalam bentuk tabel yang terurut berdasarkan prioritas
- ✅ Menandai / membatalkan status tugas (selesai atau belum selesai)
- ✅ **Pencarian tugas fleksibel** dengan berbagai kriteria, termasuk deadline
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

## 🏗️ Struktur Kode Baru

Proyek ini sekarang menggunakan **class-based approach** dengan `TodoManager` yang mengelola semua operasi CRUD:

```python
class TodoManager:
    def __init__(self):  # Otomatis memuat data dari storage
    def tambah_tugas(self, tugas: str, prioritas: str, deadline: str = "") -> bool
    def ubah_tugas(self, index: int, tugas_baru: str, deadline: str | None = None) -> bool
    def ubah_prioritas(self, index: int, prioritas_baru: str) -> bool
    def ubah_deadline(self, index: int, deadline_baru: str) -> bool
    def hapus_tugas(self, index: int) -> bool
    def toggle_status(self, index: int) -> bool
    def cari_tugas(self, **kwargs) -> List[Dict[str, Any]]
    def get_todos(self) -> List[Dict[str, Any]]
    def refresh_data(self)
    def save_data(self)
```

**Keuntungan struktur baru:**
- ✅ Encapsulation yang lebih baik
- ✅ Kode lebih terorganisir dan mudah dipelihara
- ✅ Mudah untuk menambahkan fitur baru
- ✅ Testing yang lebih komprehensif

## 🧪 Testing

Proyek ini sekarang memiliki **test unit komprehensif** dalam bahasa Indonesia:

```bash
# Menjalankan semua test
python -m unittest test_todo_manager_simple.py

# Test yang tersedia:
- Test inisialisasi TodoManager
- Test tambah tugas dengan berbagai skenario
- Test ubah tugas dan deadline
- Test hapus tugas dengan konfirmasi
- Test toggle status tugas
- Test pencarian tugas berdasarkan berbagai kriteria
- Test validasi prioritas dan deadline
```

## 🚀 Cara Menggunakan

```
========== To-Do List ==========

1. Tambah Tugas
2. Ubah Tugas
3. Ubah Prioritas
4. Ubah Deadline
5. Hapus Tugas
6. Lihat Tugas
7. Tandai / Batalkan Status Tugas
8. Cari Tugas
9. Keluar
```

- **Pilih 1** → Menambah tugas baru dengan opsi prioritas (High/Medium/Low)
- **Pilih 2** → Mengubah judul tugas yang sudah ada
- **Pilih 3** → Mengubah prioritas tugas (High/Medium/Low)
- **Pilih 4** → Mengubah deadline tugas (format YYYY-MM-DD)
- **Pilih 5** → Menghapus tugas (dengan konfirmasi y/n)
- **Pilih 6** → Melihat semua tugas dalam bentuk tabel yang terurut
- **Pilih 7** → Menandai atau membatalkan status tugas (selesai/belum selesai)
- **Pilih 8** → **Pencarian tugas** dengan berbagai kriteria
- **Pilih 9** → Keluar dari program

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
    "prioritas": "High",
    "deadline": "2024-01-15"
  },
  {
    "judul": "Belanja Harian", 
    "status": true,
    "prioritas": "Medium",
    "deadline": ""
  }
]
```

---

## 📸 Preview
```
Daftar Tugas: 
+----+--------+-----------------+------------+------------+
| No | Status | Judul           | Prioritas  | Deadline   |
+====+========+=================+============+============+
|  1 | ❌     | Belajar Python  | High       | 2024-01-15 |
+----+--------+-----------------+------------+------------+
|  2 | ✔️     | Belanja Harian | Medium     | -          |
+----+--------+-----------------+------------+------------+
|  3 | ❌     | Kerjakan PR     | Low        | 2023-12-01 |
+----+--------+-----------------+------------+------------+
```

---

## 🎯 Contoh Penggunaan
1. **Menambah tugas**: Pilih 1 → "Meeting penting" → Prioritas "High" → Deadline "2024-01-15"
2. **Mengubah prioritas**: Pilih 3 → Pilih nomor tugas → "Medium"
3. **Mengubah deadline**: Pilih 4 → Pilih nomor tugas → "2024-01-20"
4. **Menandai selesai**: Pilih 7 → Pilih nomor tugas → Status berubah menjadi ✔️
5. **Validasi error**: Input nomor di luar range → "Error: Nomor tugas tidak valid"
6. **Pencarian tugas**: Pilih 8 → Anda akan diberikan opsi untuk mencari berdasarkan:
   - **Kata kunci**: Cari tugas yang mengandung kata tertentu
   - **Prioritas**: Filter berdasarkan High, Medium, atau Low
   - **Status**: Filter berdasarkan selesai atau belum selesai
   - **Deadline**: Filter berdasarkan tanggal tertentu
   - **Kombinasi**: Gabungkan beberapa kriteria pencarian sekaligus

**Contoh penggunaan pencarian:**
- Cari semua tugas dengan prioritas "High" yang belum selesai
- Cari tugas yang mengandung kata "meeting" 
- Cari tugas yang sudah selesai dengan prioritas "Medium"
- Cari tugas dengan deadline 2024-01-15
- Cari tugas berdasarkan kombinasi kriteria tertentu

