from todo_app.storage import save_todos
from todo_app.utils import validate_date_format, format_deadline_display
from typing import List, Dict, Any


def tambah_tugas(todos: List[Dict[str, Any]], tugas: str, prioritas: str = "Medium", deadline: str = "") -> List[Dict[str, Any]]:
    tugas = tugas.strip()
    if not tugas:
        print("\nError: Tugas tidak boleh kosong.")
        return todos

    if any(existing["judul"].lower() == tugas.lower() for existing in todos):
        print("\nError: Tugas sudah ada.")
        return todos

    # Validasi prioritas
    prioritas = prioritas.capitalize()
    if prioritas not in ["High", "Medium", "Low"]:
        print("\nError: Prioritas hanya boleh High/Medium/Low.")
        return todos

    # Validasi deadline
    if deadline and not validate_date_format(deadline):
        print("\nError: Format deadline tidak valid. Gunakan format YYYY-MM-DD.")
        return todos

    # Simpan tugas kalau semua valid
    todos.append(
        {"judul": tugas, "status": False, "prioritas": prioritas, "deadline": deadline}
    )
    save_todos(todos)
    print(
        f"\nTugas '{tugas}' berhasil ditambahkan dengan (Prioritas: {prioritas}, Deadline: {deadline if deadline else '-'})."
    )
    return todos


def ubah_tugas(todos: List[Dict[str, Any]], index: int, tugas_baru: str) -> List[Dict[str, Any]]:
    if 0 < index <= len(todos):
        tugas_baru = tugas_baru.strip()
        if not tugas_baru:
            print("\nError: Tugas tidak boleh kosong.")
            return todos

        tugas_baru_lower = tugas_baru.lower()
        tugas_lama = todos[index - 1]["judul"]

        for existing in todos:
            if (
                existing["judul"].lower() == tugas_baru_lower
                and existing["judul"] != tugas_lama
            ):
                print("\nError: Tugas sudah ada.")
                return todos

        todos[index - 1]["judul"] = tugas_baru
        save_todos(todos)
        print(f"\nTugas berhasil diubah menjadi: {tugas_baru}")
    else:
        print("\nError: Nomor tugas tidak valid.")
    return todos


def ubah_prioritas(todos: List[Dict[str, Any]], index: int, prioritas_baru: str) -> List[Dict[str, Any]]:
    # validasi index
    if not (0 < index <= len(todos)):
        print("\nError: Nomor tugas tidak valid.")
        return todos

    # validasi prioritas
    prioritas_baru = prioritas_baru.capitalize()
    if prioritas_baru not in ["High", "Medium", "Low"]:
        print("\nError: Prioritas hanya boleh High/Medium/Low.")
        return todos

    todos[index - 1]["prioritas"] = prioritas_baru
    save_todos(todos)
    print(
        f"\nPrioritas tugas '{todos[index- 1]["judul"]}' berhasil diubah menjadi {prioritas_baru}."
    )
    return todos


def hapus_tugas(todos: List[Dict[str, Any]], index: int) -> List[Dict[str, Any]]:
    if 0 < index <= len(todos):
        tugas = todos[index - 1]
        konfirmasi = input(
            f"\nApakah Anda yakin ingin menghapus '{tugas['judul']}'? (y/n): "
        ).lower()
        if konfirmasi == "y":
            todos.pop(index - 1)
            save_todos(todos)
            print(f"\n{tugas['judul']} berhasil dihapus.")
        else:
            print("\nPenghapusan dibatalkan.")
    else:
        print("\nError: Nomor tugas tidak valid.")
    return todos


def toggle_status(todos: List[Dict[str, Any]], index: int) -> List[Dict[str, Any]]:
    if 0 < index <= len(todos):
        todos[index - 1]["status"] = not todos[index - 1]["status"]
        save_todos(todos)
        status = "selesai" if todos[index - 1]["status"] else "belum selesai"
        print(f"\nTugas '{todos[index - 1]['judul']}' ditandai {status}.")
    else:
        print("\nError: Nomor tugas tidak valid.")
    return todos


def ubah_deadline(todos: List[Dict[str, Any]], index: int, deadline_baru: str) -> List[Dict[str, Any]]:
    """
    Mengubah deadline tugas yang sudah ada.
    
    Args:
        todos: List tugas
        index: Nomor tugas (1-based)
        deadline_baru: Deadline baru dalam format YYYY-MM-DD
        
    Returns:
        List: Daftar tugas yang telah diupdate
    """
    # Validasi index
    if not (0 < index <= len(todos)):
        print("\nError: Nomor tugas tidak valid.")
        return todos

    # Validasi deadline
    if deadline_baru and not validate_date_format(deadline_baru):
        print("\nError: Format deadline tidak valid. Gunakan format YYYY-MM-DD.")
        return todos

    todos[index - 1]["deadline"] = deadline_baru
    save_todos(todos)
    print(f"\nDeadline tugas '{todos[index - 1]['judul']}' berhasil diubah menjadi {deadline_baru if deadline_baru else 'tidak ada'}.")
    return todos

def cari_tugas(todos: List[Dict[str, Any]], kata_kunci: str = "", prioritas: str = "", status: str = "", deadline: str = "") -> List[Dict[str, Any]]:
    """
    Mencari tugas berdasarkan kriteria yang ditentukan.

    Args:
        todos: List tugas yang akan dicari
        kata_kunci: Kata kunci untuk pencarian judul (opsional)
        prioritas: Prioritas tugas untuk difilter (High/Medium/Low, opsional)
        status: Status tugas untuk difilter (selesai/belum selesai, opsional)
        deadline: Deadline untuk difilter (YYYY-MM-DD, opsional)

    Returns:
        List: Daftar tugas yang memenuhi kriteria pencarian
    """
    hasil = todos.copy()

    # Filter berdasarkan kata kunci
    if kata_kunci:
        kata_kunci = kata_kunci.lower()
        hasil = [t for t in hasil if kata_kunci in t["judul"].lower()]

    # Filter berdasarkan prioritas
    if prioritas:
        prioritas = prioritas.capitalize()
        if prioritas in ["High", "Medium", "Low"]:
            hasil = [t for t in hasil if t["prioritas"] == prioritas]

    # Filter berdasarkan status
    if status:
        if status.lower() == "selesai":
            hasil = [t for t in hasil if t["status"]]
        elif status.lower() == "belum selesai":
            hasil = [t for t in hasil if not t["status"]]

    # Filter berdasarkan deadline
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
