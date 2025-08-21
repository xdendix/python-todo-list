import json
from json.decoder import JSONDecodeError
from tabulate import tabulate


FILE_NAME = "todos.json"


# ========== UTILITAS ==========
def load_todos():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        return []


def save_todos(todos):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(todos, file, indent=4)
    except IOError:
        print("\nError: Gagal menyimpan data.")


# ========== CRUD FUNGSI ==========
def tambah_tugas(todos, tugas: str):
    tugas = tugas.strip()
    if not tugas:
        print("\nError: Tugas tidak boleh kosong.")
        return todos

    if any(existing["judul"].lower() == tugas.lower() for existing in todos):
        print("\nError: Tugas sudah ada.")
        return todos

    todos.append({"judul": tugas, "status": False})
    save_todos(todos)
    print(f"\nTugas '{tugas}' berhasil ditambahkan.")
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


def tampilkan_tugas(todos):
    if not todos:
        print("\nBelum ada tugas.")
    else:
        table = []
        for i, tugas in enumerate(todos, start=1):
            status = "✔️" if tugas["status"] else "❌"
            prioritas = tugas.get("prioritas", "-")
            table.append([i, status, tugas["judul"], prioritas])

        print("\nDaftar Tugas: ")
        print(
            tabulate(
                table, headers=["No", "Status", "Judul", "Prioritas"], tablefmt="grid"
            )
        )


# ========== MENU UTAMA ==========
def main():
    todos = load_todos()

    while True:
        print("\n" + "=" * 10 + " To-Do List " + "=" * 10 + "\n")
        print("1. Tambah Tugas")
        print("2. Ubah Tugas")
        print("3. Hapus Tugas")
        print("4. Lihat Tugas")
        print("5. Tandai / Batalkan Status Tugas")
        print("6. Keluar")

        try:
            pilihan = int(input("\nMasukkan pilihan (1-6): "))
        except ValueError:
            print("\nError: Masukkan angka 1-6.")
            continue

        if pilihan == 1:
            tugas = input("\nMasukkan tugas baru: ")
            todos = tambah_tugas(todos, tugas)

        elif pilihan == 2:
            tampilkan_tugas(todos)
            try:
                index = int(input("\nMasukkan nomor tugas yang ingin diubah: "))
                tugas_baru = input("Masukkan tugas baru: ")
                todos = ubah_tugas(todos, index, tugas_baru)
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 3:
            tampilkan_tugas(todos)
            try:
                index = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
                todos = hapus_tugas(todos, index)
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 4:
            tampilkan_tugas(todos)

        elif pilihan == 5:
            tampilkan_tugas(todos)
            try:
                index = int(
                    input("\nMasukkan nomor tugas yang ingin diubah statusnya: ")
                )
                todos = toggle_status(todos, index)
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 6:
            print("\nTerima kasih telah menggunakan To-Do List.")
            break

        else:
            print("\nError: Pilihan hanya 1-6.")


if __name__ == "__main__":
    main()
