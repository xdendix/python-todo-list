from todo_app.storage import save_todos


def tambah_tugas(todos, tugas: str, prioritas: str = "Medium"):
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

    # Simpan tugas kalau semua valid
    todos.append({"judul": tugas, "status": False, "prioritas": prioritas})
    save_todos(todos)
    print(f"\nTugas '{tugas}' berhasil ditambahkan dengan prioritas {prioritas}.")
    return todos


def ubah_tugas(todos, index: int, tugas_baru: str):
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


def ubah_prioritas(todos, index: int, prioritas_baru: str):
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


def hapus_tugas(todos, index: int):
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


def toggle_status(todos, index: int):
    if 0 < index <= len(todos):
        todos[index - 1]["status"] = not todos[index - 1]["status"]
        save_todos(todos)
        status = "selesai" if todos[index - 1]["status"] else "belum selesai"
        print(f"\nTugas '{todos[index - 1]['judul']}' ditandai {status}.")
    else:
        print("\nError: Nomor tugas tidak valid.")
    return todos


def cari_tugas(todos, kata_kunci: str = "", prioritas: str = "", status: str = ""):
    """
    Mencari tugas berdasarkan kriteria yang ditentukan.
    
    Args:
        todos: List tugas yang akan dicari
        kata_kunci: Kata kunci untuk pencarian judul (opsional)
        prioritas: Prioritas tugas untuk difilter (High/Medium/Low, opsional)
        status: Status tugas untuk difilter (True untuk selesai, False untuk belum selesai, opsional)
        
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
    
    if not hasil:
        print("\nTidak ada tugas yang sesuai dengan kriteria pencarian.")
    else:
        print(f"\nHasil pencarian ({len(hasil)} tugas ditemukan):")
        for i, tugas in enumerate(hasil, 1):
            status_text = "✔️ Selesai" if tugas["status"] else "❌ Belum selesai"
            print(f"{i}. {tugas['judul']} (Prioritas: {tugas['prioritas']}, Status: {status_text})")
    
    return hasil
