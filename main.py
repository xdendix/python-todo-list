from todo_app.storage import load_todos
from todo_app.crud import (
    tambah_tugas,
    ubah_tugas,
    ubah_prioritas,
    hapus_tugas,
    toggle_status,
)
from todo_app.ui import tampilkan_tugas


# ========== MENU UTAMA ==========
def main():
    todos = load_todos()

    while True:
        print("\n" + "=" * 10 + " To-Do List " + "=" * 10 + "\n")
        print("1. Tambah Tugas")
        print("2. Ubah Tugas")
        print("3. Ubah Prioritas")
        print("4. Hapus Tugas")
        print("5. Lihat Tugas")
        print("6. Tandai / Batalkan Status Tugas")
        print("7. Keluar")

        try:
            pilihan = int(input("\nMasukkan pilihan (1-7): "))
        except ValueError:
            print("\nError: Masukkan angka 1-7.")
            continue

        if pilihan == 1:
            tugas = input("\nMasukkan tugas baru: ")
            prioritas = input(
                "Masukkan prioritas (High/Medium/Low, default=Medium): "
            ).capitalize()
            if not prioritas:
                prioritas = "Medium"
            todos = tambah_tugas(todos, tugas, prioritas)

        elif pilihan == 2:
            tampilkan_tugas(todos)
            if not todos:
                continue
            try:
                index = int(input("\nMasukkan nomor tugas yang ingin diubah: "))
                if index < 1 or index > len(todos):
                    print("\nError: Nomor tugas tidak valid.")
                    continue
                tugas_baru = input("Masukkan tugas baru: ")
                todos = ubah_tugas(todos, index, tugas_baru)
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 3:
            tampilkan_tugas(todos)
            if not todos:
                continue
            try:
                index = int(input("\nMasukkan nomor tugas yang ingin diubah prioritasnya: "))
                if index < 1 or index > len(todos):
                    print("\nError: Nomor tugas tidak valid.")
                    continue
                prioritas_baru = input("Masukkan prioritas baru: ").capitalize()
                todos = ubah_prioritas(todos, index, prioritas_baru)
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 4:
            tampilkan_tugas(todos)
            if not todos:
                continue
            try:
                index = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
                if index < 1 or index > len(todos):
                    print("\nError: Nomor tugas tidak valid.")
                    continue
                todos = hapus_tugas(todos, index)
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 5:
            tampilkan_tugas(todos)

        elif pilihan == 6:
            tampilkan_tugas(todos)
            if not todos:
                continue
            try:
                index = int(
                    input("\nMasukkan nomor tugas yang ingin diubah statusnya: ")
                )
                if index < 1 or index > len(todos):
                    print("\nError: Nomor tugas tidak valid.")
                    continue
                todos = toggle_status(todos, index)
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 7:
            print("\nTerima kasih telah menggunakan To-Do List.")
            break

        else:
            print("\nError: Pilihan hanya 1-7.")


if __name__ == "__main__":
    main()
