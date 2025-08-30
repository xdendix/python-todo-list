import unittest
import json
import os
import tempfile
from unittest.mock import patch, mock_open
from todo_app.crud import TodoManager
from todo_app.storage import save_todos, load_todos


class TestTodoManager(unittest.TestCase):
    """Test class untuk TodoManager"""
    
    def setUp(self):
        """Setup sebelum setiap test"""
        # Buat file temporary untuk testing
        self.temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json')
        self.temp_filename = self.temp_file.name
        self.temp_file.close()
        
        # Reset file storage ke list kosong
        with open(self.temp_filename, 'w') as f:
            f.write('[]')
        
        # Patch FILE_NAME di config untuk menggunakan file temporary
        self.patcher = patch('todo_app.config.FILE_NAME', self.temp_filename)
        self.patcher.start()
        
        # Inisialisasi TodoManager
        self.todo_manager = TodoManager()
    
    def tearDown(self):
        """Cleanup setelah setiap test"""
        self.patcher.stop()
        if os.path.exists(self.temp_filename):
            os.unlink(self.temp_filename)
    
    def test_inisialisasi_todo_manager(self):
        """Test inisialisasi TodoManager dengan data kosong"""
        self.assertEqual(len(self.todo_manager.get_todos()), 0)
        self.assertIsInstance(self.todo_manager.get_todos(), list)
    
    def test_tambah_tugas_berhasil(self):
        """Test menambahkan tugas baru dengan sukses"""
        result = self.todo_manager.tambah_tugas("Belajar Python", "High")
        self.assertTrue(result)
        self.assertEqual(len(self.todo_manager.get_todos()), 1)
        
        tugas = self.todo_manager.get_todos()[0]
        self.assertEqual(tugas["judul"], "Belajar Python")
        self.assertEqual(tugas["prioritas"], "High")
        self.assertFalse(tugas["status"])
        self.assertNotIn("deadline", tugas)
    
    def test_tambah_tugas_dengan_deadline(self):
        """Test menambahkan tugas dengan deadline yang valid"""
        result = self.todo_manager.tambah_tugas("Belajar JavaScript", "Medium", "2025-12-31")
        self.assertTrue(result)
        
        tugas = self.todo_manager.get_todos()[0]
        self.assertEqual(tugas["judul"], "Belajar JavaScript")
        self.assertEqual(tugas["prioritas"], "Medium")
        self.assertEqual(tugas["deadline"], "2025-12-31")
    
    def test_tambah_tugas_deadline_invalid(self):
        """Test menambahkan tugas dengan deadline format tidak valid"""
        result = self.todo_manager.tambah_tugas("Tugas Invalid", "Low", "31-12-2025")
        self.assertFalse(result)
        self.assertEqual(len(self.todo_manager.get_todos()), 0)
    
    def test_tambah_tugas_kosong(self):
        """Test menambahkan tugas dengan judul kosong"""
        result = self.todo_manager.tambah_tugas("", "High")
        self.assertFalse(result)
        self.assertEqual(len(self.todo_manager.get_todos()), 0)
    
    def test_tambah_tugas_duplikat(self):
        """Test menambahkan tugas yang sudah ada"""
        self.todo_manager.tambah_tugas("Tugas Sama", "Medium")
        result = self.todo_manager.tambah_tugas("tugas sama", "High")  # Case insensitive
        self.assertFalse(result)
        self.assertEqual(len(self.todo_manager.get_todos()), 1)
    
    def test_ubah_tugas_berhasil(self):
        """Test mengubah judul tugas dengan sukses"""
        self.todo_manager.tambah_tugas("Tugas Lama", "Low")
        result = self.todo_manager.ubah_tugas(1, "Tugas Baru")
        self.assertTrue(result)
        
        tugas = self.todo_manager.get_todos()[0]
        self.assertEqual(tugas["judul"], "Tugas Baru")
    
    def test_ubah_tugas_dengan_deadline(self):
        """Test mengubah tugas dengan deadline baru"""
        self.todo_manager.tambah_tugas("Tugas", "Medium")
        result = self.todo_manager.ubah_tugas(1, "Tugas Diubah", "2025-11-15")
        self.assertTrue(result)
        
        tugas = self.todo_manager.get_todos()[0]
        self.assertEqual(tugas["judul"], "Tugas Diubah")
        self.assertEqual(tugas["deadline"], "2025-11-15")
    
    def test_ubah_tugas_hapus_deadline(self):
        """Test menghapus deadline dari tugas"""
        self.todo_manager.tambah_tugas("Tugas", "Medium", "2025-10-10")
        result = self.todo_manager.ubah_tugas(1, "Tugas Sama", "")
        self.assertTrue(result)
        
        tugas = self.todo_manager.get_todos()[0]
        self.assertEqual(tugas["judul"], "Tugas Sama")
        self.assertNotIn("deadline", tugas)
    
    def test_ubah_tugas_index_invalid(self):
        """Test mengubah tugas dengan index tidak valid"""
        result = self.todo_manager.ubah_tugas(999, "Tugas Baru")
        self.assertFalse(result)
    
    def test_ubah_deadline_berhasil(self):
        """Test mengubah deadline tugas dengan sukses"""
        self.todo_manager.tambah_tugas("Tugas", "High")
        result = self.todo_manager.ubah_deadline(1, "2025-09-30")
        self.assertTrue(result)
        
        tugas = self.todo_manager.get_todos()[0]
        self.assertEqual(tugas["deadline"], "2025-09-30")
    
    def test_ubah_deadline_hapus(self):
        """Test menghapus deadline dari tugas"""
        self.todo_manager.tambah_tugas("Tugas", "High", "2025-08-15")
        result = self.todo_manager.ubah_deadline(1, "")
        self.assertTrue(result)
        
        tugas = self.todo_manager.get_todos()[0]
        self.assertNotIn("deadline", tugas)
    
    def test_ubah_deadline_invalid(self):
        """Test mengubah deadline dengan format tidak valid"""
        self.todo_manager.tambah_tugas("Tugas", "Medium")
        result = self.todo_manager.ubah_deadline(1, "30-09-2025")
        self.assertFalse(result)
    
    def test_ubah_prioritas_berhasil(self):
        """Test mengubah prioritas tugas"""
        self.todo_manager.tambah_tugas("Tugas", "Low")
        result = self.todo_manager.ubah_prioritas(1, "High")
        self.assertTrue(result)
        
        tugas = self.todo_manager.get_todos()[0]
        self.assertEqual(tugas["prioritas"], "High")
    
    def test_ubah_prioritas_invalid(self):
        """Test mengubah prioritas dengan nilai tidak valid"""
        self.todo_manager.tambah_tugas("Tugas", "Medium")
        result = self.todo_manager.ubah_prioritas(1, "Very High")
        self.assertFalse(result)
        
        tugas = self.todo_manager.get_todos()[0]
        self.assertEqual(tugas["prioritas"], "Medium")  # Prioritas tidak berubah
    
    def test_hapus_tugas_berhasil(self):
        """Test menghapus tugas dengan konfirmasi"""
        self.todo_manager.tambah_tugas("Tugas Dihapus", "Medium")
        
        with patch('builtins.input', return_value='y'):
            result = self.todo_manager.hapus_tugas(1)
        
        self.assertTrue(result)
        self.assertEqual(len(self.todo_manager.get_todos()), 0)
    
    def test_hapus_tugas_batal(self):
        """Test membatalkan penghapusan tugas"""
        self.todo_manager.tambah_tugas("Tugas Tidak Dihapus", "Low")
        
        with patch('builtins.input', return_value='n'):
            result = self.todo_manager.hapus_tugas(1)
        
        self.assertFalse(result)
        self.assertEqual(len(self.todo_manager.get_todos()), 1)
    
    def test_toggle_status_berhasil(self):
        """Test mengubah status tugas"""
        self.todo_manager.tambah_tugas("Tugas", "Medium")
        
        # Test dari belum selesai ke selesai
        result = self.todo_manager.toggle_status(1)
        self.assertTrue(result)
        self.assertTrue(self.todo_manager.get_todos()[0]["status"])
        
        # Test dari selesai ke belum selesai
        result = self.todo_manager.toggle_status(1)
        self.assertTrue(result)
        self.assertFalse(self.todo_manager.get_todos()[0]["status"])
    
    def test_cari_tugas_berdasarkan_kata_kunci(self):
        """Test pencarian tugas berdasarkan kata kunci"""
        self.todo_manager.tambah_tugas("Belajar Python", "High")
        self.todo_manager.tambah_tugas("Belajar JavaScript", "Medium")
        self.todo_manager.tambah_tugas("Makan Siang", "Low")
        
        hasil = self.todo_manager.cari_tugas(kata_kunci="belajar")
        self.assertEqual(len(hasil), 2)
        self.assertEqual(hasil[0]["judul"], "Belajar Python")
        self.assertEqual(hasil[1]["judul"], "Belajar JavaScript")
    
    def test_cari_tugas_berdasarkan_prioritas(self):
        """Test pencarian tugas berdasarkan prioritas"""
        self.todo_manager.tambah_tugas("Tugas 1", "High")
        self.todo_manager.tambah_tugas("Tugas 2", "Medium")
        self.todo_manager.tambah_tugas("Tugas 3", "High")
        
        hasil = self.todo_manager.cari_tugas(prioritas="High")
        self.assertEqual(len(hasil), 2)
        for tugas in hasil:
            self.assertEqual(tugas["prioritas"], "High")
    
    def test_cari_tugas_berdasarkan_status(self):
        """Test pencarian tugas berdasarkan status"""
        self.todo_manager.tambah_tugas("Tugas 1", "Medium")
        self.todo_manager.tambah_tugas("Tugas 2", "Low")
        self.todo_manager.toggle_status(1)  # Tandai tugas 1 sebagai selesai
        
        hasil_selesai = self.todo_manager.cari_tugas(status="selesai")
        self.assertEqual(len(hasil_selesai), 1)
        self.assertTrue(hasil_selesai[0]["status"])
        
        hasil_belum_selesai = self.todo_manager.cari_tugas(status="belum selesai")
        self.assertEqual(len(hasil_belum_selesai), 1)
        self.assertFalse(hasil_belum_selesai[0]["status"])
    
    def test_refresh_data(self):
        """Test memuat ulang data dari storage"""
        self.todo_manager.tambah_tugas("Tugas Awal", "High")
        
        # Simulasikan perubahan data di luar TodoManager
        with open(self.temp_filename, 'w') as f:
            json.dump([{"judul": "Tugas Baru", "status": False, "prioritas": "Medium"}], f)
        
        self.todo_manager.refresh_data()
        self.assertEqual(len(self.todo_manager.get_todos()), 1)
        self.assertEqual(self.todo_manager.get_todos()[0]["judul"], "Tugas Baru")


if __name__ == "__main__":
    unittest.main()
