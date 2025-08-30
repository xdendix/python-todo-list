from todo_app.storage import save_todos, load_todos
from todo_app.utils import validate_date_format, format_deadline_display
from typing import List, Dict, Any


class TodoManager:
    def __init__(self):
        self.todos: List[Dict[str, Any]] = load_todos()

    def save_data(self):
        save_todos(self.todos)

    def tambah_tugas(self, tugas: str, prioritas: str = "Medium", deadline: str = "") -> bool:
        tugas = tugas.strip()
        if not tugas:
            print("\nError: Tugas tidak boleh kosong.")
            return False

        if any(existing["judul"].lower() == tugas.lower() for existing in self.todos):
            print("\nError: Tugas sudah ada.")
            return False

        prioritas = prioritas.capitalize()
        if prioritas not in ["High", "Medium", "Low"]:
            print("\nError: Prioritas hanya boleh High/Medium/Low.")
            return False

        if deadline and not validate_date_format(deadline):
            print("\nError: Format deadline tidak valid. Gunakan format YYYY-MM-DD.")
            return False

        self.todos.append(
            {"judul": tugas, "status": False, "prioritas": prioritas, "deadline": deadline}
        )
        self.save_data()
        print(
            f"\nTugas '{tugas}' berhasil ditambahkan dengan (Prioritas: {prioritas}, Deadline: {deadline if deadline else '-'})"
        )
        return True

    def ubah_tugas(self, index: int, tugas_baru: str, deadline: str | None = None) -> bool:
        if 0 < index <= len(self.todos):
            tugas_baru = tugas_baru.strip()
            if not tugas_baru:
                print("\nError: Tugas tidak boleh kosong.")
                return False

            tugas_baru_lower = tugas_baru.lower()
            tugas_lama = self.todos[index - 1]["judul"]

            for existing in self.todos:
                if (
                    existing["judul"].lower() == tugas_baru_lower
                    and existing["judul"] != tugas_lama
                ):
                    print("\nError: Tugas sudah ada.")
                    return False

            self.todos[index - 1]["judul"] = tugas_baru

            if deadline is not None:
                if deadline and not validate_date_format(deadline):
                    print("\nError: Format deadline tidak valid. Gunakan format YYYY-MM-DD.")
                    return False
                if deadline == "":
                    self.todos[index - 1].pop("deadline", None)
                else:
                    self.todos[index - 1]["deadline"] = deadline

            self.save_data()
            print(f"\nTugas berhasil diubah menjadi: {tugas_baru}")
            if deadline is not None:
                print(f"Deadline: {deadline if deadline else 'dihapus'}")
            return True
        else:
            print("\nError: Nomor tugas tidak valid.")
            return False

    def ubah_prioritas(self, index: int, prioritas_baru: str) -> bool:
        if not (0 < index <= len(self.todos)):
            print("\nError: Nomor tugas tidak valid.")
            return False

        prioritas_baru = prioritas_baru.capitalize()
        if prioritas_baru not in ["High", "Medium", "Low"]:
            print("\nError: Prioritas hanya boleh High/Medium/Low.")
            return False

        self.todos[index - 1]["prioritas"] = prioritas_baru
        self.save_data()
        print(
            f"\nPrioritas tugas '{self.todos[index - 1]['judul']}' berhasil diubah menjadi {prioritas_baru}."
        )
        return True

    def hapus_tugas(self, index: int) -> bool:
        if 0 < index <= len(self.todos):
            tugas = self.todos[index - 1]
            konfirmasi = input(
                f"\nApakah Anda yakin ingin menghapus '{tugas['judul']}'? (y/n): "
            ).lower()
            if konfirmasi == "y":
                self.todos.pop(index - 1)
                self.save_data()
                print(f"\n{tugas['judul']} berhasil dihapus.")
                return True
            else:
                print("\nPenghapusan dibatalkan.")
                return False
        else:
            print("\nError: Nomor tugas tidak valid.")
            return False

    def toggle_status(self, index: int) -> bool:
        if 0 < index <= len(self.todos):
            self.todos[index - 1]["status"] = not self.todos[index - 1]["status"]
            self.save_data()
            status = "selesai" if self.todos[index - 1]["status"] else "belum selesai"
            print(f"\nTugas '{self.todos[index - 1]['judul']}' ditandai {status}.")
            return True
        else:
            print("\nError: Nomor tugas tidak valid.")
            return False

    def ubah_deadline(self, index: int, deadline_baru: str) -> bool:
        if not (0 < index <= len(self.todos)):
            print("\nError: Nomor tugas tidak valid.")
            return False

        if deadline_baru and not validate_date_format(deadline_baru):
            print("\nError: Format deadline tidak valid. Gunakan format YYYY-MM-DD.")
            return False

        if deadline_baru == "":
            self.todos[index - 1].pop("deadline", None)
        else:
            self.todos[index - 1]["deadline"] = deadline_baru

        self.save_data()
        print(f"\nDeadline tugas '{self.todos[index - 1]['judul']}' berhasil diubah menjadi {deadline_baru if deadline_baru else 'tidak ada'}.")
        return True

    def cari_tugas(self, kata_kunci: str = "", prioritas: str = "", status: str = "", deadline: str = "") -> List[Dict[str, Any]]:
        hasil = self.todos.copy()

        if kata_kunci:
            kata_kunci = kata_kunci.lower()
            hasil = [t for t in hasil if kata_kunci in t["judul"].lower()]

        if prioritas:
            prioritas = prioritas.capitalize()
            if prioritas in ["High", "Medium", "Low"]:
                hasil = [t for t in hasil if t["prioritas"] == prioritas]

        if status:
            if status.lower() == "selesai":
                hasil = [t for t in hasil if t["status"]]
            elif status.lower() == "belum selesai":
                hasil = [t for t in hasil if not t["status"]]

        if deadline:
            if validate_date_format(deadline):
                hasil = [t for t in hasil if t.get("deadline") == deadline]
            else:
                print("\nWarning: Format deadline tidak valid untuk pencarian.")

        if not hasil:
            print("\nTidak ada tugas yang sesuai dengan kriteria pencarian.")
        else:
            print(f"\nHasil pencarian ({len(hasil)} tugas ditemukan):")
            for i, tugas in enumerate(hasil, 1):
                status_text = "✔️ Selesai" if tugas["status"] else "❌ Belum selesai"
                deadline_text = format_deadline_display(tugas.get("deadline", ""))
                print(
                    f"{i}. {tugas['judul']} (Prioritas: {tugas['prioritas']}, Status: {status_text}, Deadline: {deadline_text})"
                )

        return hasil

    def get_todos(self) -> List[Dict[str, Any]]:
        return self.todos

    def refresh_data(self):
        self.todos = load_todos()
