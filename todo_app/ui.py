from tabulate import tabulate
from todo_app.utils import format_deadline_display


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
            deadline = format_deadline_display(tugas.get("deadline", ""))
            table.append([i, status, tugas["judul"], prioritas, deadline])

        print("\nDaftar Tugas: ")
        print(
            tabulate(
                table, 
                headers=["No", "Status", "Judul", "Prioritas", "Deadline"], 
                tablefmt="grid"
            )
        )
