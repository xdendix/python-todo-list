from tabulate import tabulate


def tampilkan_tugas(todos):
    prioritas_order = {"High": 1, "Medium": 2, "Low": 3}
    todos.sort(key=lambda x: prioritas_order.get(x.get("prioritas", "Medium"), 4))
    if not todos:
        print("\nBelum ada tugas.")
    else:
        table = []
        for i, tugas in enumerate(todos, start=1):
            status = "✔️" if tugas["status"] else "❌"
            prioritas = tugas.get("prioritas")
            table.append([i, status, tugas["judul"], prioritas])

        print("\nDaftar Tugas: ")
        print(
            tabulate(
                table, headers=["No", "Status", "Judul", "Prioritas"], tablefmt="grid"
            )
        )
