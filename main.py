# Program To-Do List sederhana untuk menambah, menampilkan, dan menghapus tugas harian.
import json
import os

FILE_NAME = "todos.json"


def load_todos():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_todos(todos):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(todos, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error: Gagal menyimpan tugas - {e}")
        return False


def tampilkan_tugas(todos):
    if not todos:
        print("\nBelum ada tugas.")
        return
    print("\nDaftar Tugas:\n")
    for i, tugas in enumerate(todos, start=1):
        print(f"{i}. {tugas}")


def tambah_tugas(todos, tugas: str):
    todos.append(tugas)
    save_todos(todos)  # simpan file
    print(f"\n{tugas} berhasil ditambahkan dan disimpan.")
    
    return todos


def ubah_tugas(todos):
    if not todos:
        print("Tidak ada tugas untuk diubah.")
        return todos

    tampilkan_tugas(todos)

    try:
        index = int(input("\nMasukkan nomor tugas yang ingin diubah: "))
        if not (1 <= index <= len(todos)):
            print("\nError: Nomor tugas tidak ada.")
            return todos

        tugas_lama = todos[index - 1]
        print(f"\nTugas lama: {tugas_lama}")

        tugas_baru = input("Masukkan tugas baru: ").strip()

        is_valid, message = validate_task(tugas_baru)
        if not is_valid:
            print(f"\nError: {message}")
            return todos

        # cek apakah sama dengan tugas lama
        if tugas_baru == tugas_lama:
            print("\nTugas tidak berubah.")
            return todos

        # cek duplikat
        tugas_baru_lower = tugas_baru.lower()
        for existing in todos:
            if existing.lower() == tugas_baru_lower and existing != tugas_lama:
                print(f"\nTugas '{tugas_baru}' sudah ada dalam daftar.")
                return todos

        todos[index - 1] = tugas_baru
        if save_todos(todos):
            print(
                f"\nTugas berhasil diubah dari '{tugas_lama}' menjadi '{tugas_baru}'."
            )

    except ValueError:
        print("\nError: Input harus berupa angka.")

    return todos


def hapus_tugas(todos, index: int):
    # Hapus tugas
    if 0 < index <= len(todos):
        tugas = todos.pop(index - 1)
        save_todos(todos)  # simpan file sehabis dihapus
        print(f"\n{tugas} berhasil dihapus.")
    else:
        print("\nError: Input tidak valid.")
        
    return todos


def validate_task(task):
    if not task or len(task.strip()) == 0:
        return False, "Tugas tidak boleh kosong"
    if len(task) > 100:
        return False, "Tugas terlalu panjang (maks 100 karakter)"
    return True, task.strip()


# Program utama
def tampilan_utama_program():
    todos = load_todos()  # load dari file saat mulai
    while True:
        print("\n" + "To-Do-List".center(34, "=") + "\n")
        print("1. Tampilkan Tugas")
        print("2. Tambah Tugas")
        print("3. Ubah Tugas")
        print("4. Hapus Tugas")
        print("5. Keluar")

        while True:
            pilihan_input = input("\nMasukkan pilihan: ")
            if pilihan_input.strip() == "":
                print("\nError: Pilihan tidak boleh kosong.")
                continue
            try:
                pilihan = int(pilihan_input)
                break
            except ValueError:
                print("\nError: Input tidak valid.")

        if pilihan == 1:
            tampilkan_tugas(todos)

        elif pilihan == 2:
            tugas = input("\nMasukkan tugas hari ini: ").strip()
            is_valid, message = validate_task(tugas)
            if not is_valid:
                print(f"\nError: {message}")
            else:
                tambah_tugas(todos, message)
                tampilkan_tugas(todos)

        elif pilihan == 3:
            ubah_tugas(todos)

        elif pilihan == 4:
            tampilkan_tugas(todos)
            try:
                index = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
                if not (1 <= index <= len(todos)):
                    print("\nError: Nomor tugas tidak ada.")
                    continue
                while True:
                    konfirmasi = input(
                        "\nApakah yakin ingin menghapus? (y/n): "
                    ).lower()
                    if konfirmasi == "y":
                        hapus_tugas(todos, index)
                        break
                    elif konfirmasi == "n":
                        print("\nBatal menghapus tugas.")
                        break
                    else:
                        print("\nError: Pilihan hanya 'y' dan 'n'")
            except ValueError:
                print("\nError: Input tidak valid.")

        elif pilihan == 5:
            while True:
                konfirmasi = input("\nYakin ingin keluar? (y/n): ").lower()
                if konfirmasi == "y":
                    print("\nTerima kasih.")
                    return
                elif konfirmasi == "n":
                    break
                else:
                    print("\nError: Pilihan hanya 'y' dan 'n'")

        else:
            print("\nError: Masukkan angka dari 1-5 untuk memilih menu.")


if __name__ == "__main__":
    tampilan_utama_program()
