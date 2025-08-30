from todo_app.storage import load_todos
from todo_app.crud import TodoManager
from todo_app.ui import tampilkan_tugas


# ========== MENU UTAMA ==========
def main():
    todo_manager = TodoManager()

    while True:
        print("\n" + "=" * 10 + " To-Do List " + "=" * 10 + "\n")
        print("1. Tambah Tugas")
        print("2. Ubah Tugas")
        print("3. Ubah Prioritas")
        print("4. Ubah Deadline")
        print("5. Hapus Tugas")
        print("6. Lihat Tugas")
        print("7. Tandai / Batalkan Status Tugas")
        print("8. Cari Tugas")
        print("9. Keluar")

        try:
            pilihan = int(input("\nMasukkan pilihan (1-9): "))
        except ValueError:
            print("\nError: Masukkan angka 1-9.")
            continue

        if pilihan == 1:
            tugas = input("\nMasukkan tugas baru: ")
            prioritas = input(
                "Masukkan prioritas (High/Medium/Low, default=Medium): "
            ).capitalize()
            if not prioritas:
                prioritas = "Medium"
            deadline = input("Masukkan deadline (format YYYY-MM-DD, opsional): ")
            todo_manager.tambah_tugas(tugas, prioritas, deadline)

        elif pilihan == 2:
            tampilkan_tugas(todo_manager.get_todos())
            if not todo_manager.get_todos():
                continue
            try:
                index = int(input("\nMasukkan nomor tugas yang ingin diubah: "))
                if index < 1 or index > len(todo_manager.get_todos()):
                    print("\nError: Nomor tugas tidak valid.")
                    continue
                tugas_baru = input("Masukkan tugas baru: ")
                deadline = input("Masukkan deadline baru (format YYYY-MM-DD, kosongkan untuk tidak diubah): ")
                if deadline == "":
                    deadline = None
                todo_manager.ubah_tugas(index, tugas_baru, deadline)
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 3:
            tampilkan_tugas(todo_manager.get_todos())
            if not todo_manager.get_todos():
                continue
            try:
                index = int(
                    input("\nMasukkan nomor tugas yang ingin diubah prioritasnya: ")
                )
                if index < 1 or index > len(todo_manager.get_todos()):
                    print("\nError: Nomor tugas tidak valid.")
                    continue
                prioritas_baru = input("Masukkan prioritas baru: ").capitalize()
                todo_manager.ubah_prioritas(index, prioritas_baru)
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 4:
            tampilkan_tugas(todo_manager.get_todos())
            if not todo_manager.get_todos():
                continue
            try:
                index = int(input("\nMasukkan nomor tugas yang ingin diubah deadline: "))
                if index < 1 or index > len(todo_manager.get_todos()):
                    print("\nError: Nomor tugas tidak valid.")
                    continue
                deadline_baru = input("Masukkan deadline baru (format YYYY-MM-DD, kosongkan untuk menghapus): ")
                todo_manager.ubah_deadline(index, deadline_baru)
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 5:
            tampilkan_tugas(todo_manager.get_todos())
            if not todo_manager.get_todos():
                continue
            try:
                index = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
                if index < 1 or index > len(todo_manager.get_todos()):
                    print("\nError: Nomor tugas tidak valid.")
                    continue
                todo_manager.hapus_tugas(index)
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 6:
            tampilkan_tugas(todo_manager.get_todos())

        elif pilihan == 7:
            tampilkan_tugas(todo_manager.get_todos())
            if not todo_manager.get_todos():
                continue
            try:
                index = int(
                    input("\nMasukkan nomor tugas yang ingin diubah statusnya: ")
                )
                if index < 1 or index > len(todo_manager.get_todos()):
                    print("\nError: Nomor tugas tidak valid.")
                    continue
                todo_manager.toggle_status(index)
            except ValueError:
                print("\nError: input tidak valid.")

        elif pilihan == 8:
            print("\n=== PENCARIAN TUGAS ===")
            print("1. Cari berdasarkan kata kunci")
            print("2. Cari berdasarkan prioritas")
            print("3. Cari berdasarkan status")
            print("4. Cari berdasarkan deadline")
            print("5. Cari dengan kombinasi kriteria")

            try:
                pilihan_cari = int(input("\nPilih jenis pencarian (1-5): "))
            except ValueError:
                print("\nError: Masukkan angka 1-5.")
                continue

            if pilihan_cari == 1:
                kata_kunci = input("Masukkan kata kunci: ")
                todo_manager.cari_tugas(kata_kunci=kata_kunci)

            elif pilihan_cari == 2:
                print("\nPrioritas: High, Medium, Low")
                prioritas = input("Masukkan prioritas: ")
                todo_manager.cari_tugas(prioritas=prioritas)

            elif pilihan_cari == 3:
                print("\nStatus: selesai, belum selesai")
                status = input("Masukkan status: ")
                todo_manager.cari_tugas(status=status)

            elif pilihan_cari == 4:
                deadline = input("Masukkan deadline (format YYYY-MM-DD): ")
                todo_manager.cari_tugas(deadline=deadline)

            elif pilihan_cari == 5:
                kata_kunci = input("Masukkan kata kunci (kosongkan jika tidak perlu): ")
                prioritas = input("Masukkan prioritas (kosongkan jika tidak perlu): ")
                status = input("Masukkan status (selesai/belum selesai, kosongkan jika tidak perlu): ")
                deadline = input("Masukkan deadline (YYYY-MM-DD, kosongkan jika tidak perlu): ")
                todo_manager.cari_tugas(
                    kata_kunci=kata_kunci,
                    prioritas=prioritas,
                    status=status,
                    deadline=deadline,
                )

            else:
                print("\nError: Pilihan hanya 1-5.")

        elif pilihan == 9:
            print("\nTerima kasih telah menggunakan To-Do List.")
            break

        else:
            print("\nError: Pilihan hanya 1-9.")


if __name__ == "__main__":
    main()
