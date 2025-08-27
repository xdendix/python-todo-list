from todo_app.storage import load_todos
from todo_app.crud import (
    tambah_tugas,
    ubah_tugas,
    ubah_prioritas,
    hapus_tugas,
    toggle_status,
    cari_tugas,
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
        print("7. Cari Tugas")
        print("8. Keluar")

        try:
            pilihan = int(input("\nMasukkan pilihan (1-8): "))
        except ValueError:
            print("\nError: Masukkan angka 1-8.")
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
                index = int(
                    input("\nMasukkan nomor tugas yang ingin diubah prioritasnya: ")
                )
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
            print("\n=== PENCARIAN TUGAS ===")
            print("1. Cari berdasarkan kata kunci")
            print("2. Cari berdasarkan prioritas")
            print("3. Cari berdasarkan status")
            print("4. Cari dengan kombinasi kriteria")
            
            try:
                pilihan_cari = int(input("\nPilih jenis pencarian (1-4): "))
            except ValueError:
                print("\nError: Masukkan angka 1-4.")
                continue
                
            if pilihan_cari == 1:
                kata_kunci = input("Masukkan kata kunci: ")
                cari_tugas(todos, kata_kunci=kata_kunci)
                
            elif pilihan_cari == 2:
                print("\nPrioritas: High, Medium, Low")
                prioritas = input("Masukkan prioritas: ")
                cari_tugas(todos, prioritas=prioritas)
                
            elif pilihan_cari == 3:
                print("\nStatus: selesai, belum selesai")
                status = input("Masukkan status: ")
                cari_tugas(todos, status=status)
                
            elif pilihan_cari == 4:
                kata_kunci = input("Masukkan kata kunci (kosongkan jika tidak perlu): ")
                prioritas = input("Masukkan prioritas (kosongkan jika tidak perlu): ")
                status = input("Masukkan status (selesai/belum selesai, kosongkan jika tidak perlu): ")
                cari_tugas(todos, kata_kunci=kata_kunci, prioritas=prioritas, status=status)
                
            else:
                print("\nError: Pilihan hanya 1-4.")

        elif pilihan == 8:
            print("\nTerima kasih telah menggunakan To-Do List.")
            break

        else:
            print("\nError: Pilihan hanya 1-8.")


if __name__ == "__main__":
    main()
