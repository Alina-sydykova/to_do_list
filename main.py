import flet as ft
from db import main_db

def main(page: ft.Page):
    page.title = 'Todo List'
    page.padding = 40
    page.bgcolor = ft.Colors.GREY_600
    page.theme_mode = ft.ThemeMode.DARK

    task_list = ft.Column(spacing=10, expand=True)

    def load_tasks():
        task_list.controls.clear()
        for task_id, task_text, created_at, status in main_db.get_tasks():
            task_list.controls.append(create_task_row(task_id, task_text, created_at, status))
        page.update()

    def create_task_row(task_id, task_text, created_at, status):
        task_field = ft.TextField(value=task_text, expand=True, dense=True, read_only=True)
        date_text = ft.Text(created_at, color=ft.Colors.GREY_400, size=20)
        status_text = ft.Text(status, color=ft.Colors.GREEN_400, size=16)

        def enable_edit(e):
            task_field.read_only = False
            page.update()

        def save_edit(e):
            main_db.update_task_db(task_id, task_field.value)
            task_field.read_only = True
            page.update()

        def change_status(e):
            new_status = "Завершено" if status == "В процессе" else "В процессе"  
            main_db.update_task_db_status(task_id, new_status)
            status_text.value = new_status
            page.update()

        row = ft.Row([
            ft.Column([task_field, date_text, status_text], expand=True),
            ft.Row([
                ft.IconButton(ft.Icons.EDIT, icon_color=ft.Colors.YELLOW_400, on_click=enable_edit),
                ft.IconButton(ft.Icons.SAVE, icon_color=ft.Colors.GREEN_400, on_click=save_edit),
                ft.IconButton(ft.Icons.CHECK, icon_color=ft.Colors.BLUE_400, on_click=change_status),
            ], alignment=ft.MainAxisAlignment.END)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        return row

    def sort_tasks(e):
        tasks = main_db.get_tasks()
        tasks.sort(key=lambda x: (x[3], x[2]))  # Сортировка по статусу и дате
        task_list.controls.clear()
        for task_id, task_text, created_at, status in tasks:
            task_list.controls.append(create_task_row(task_id, task_text, created_at, status))
        page.update()

    def add_task(e):
        if task_input.value.strip():
            task_id, created_at, status = main_db.add_task_db(task_input.value)
            task_list.controls.append(create_task_row(task_id, task_input.value, created_at, status))
            task_input.value = ""
            page.update()

    task_input = ft.TextField(hint_text='Добавьте задачу', expand=True, dense=True, on_submit=add_task)
    add_button = ft.ElevatedButton("Добавить", on_click=add_task, icon=ft.Icons.ADD)
    sort_button = ft.ElevatedButton("Сортировать", on_click=sort_tasks)

    page.add(
        ft.Column([
            ft.Row([task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            sort_button,
            task_list
        ], expand=True)
    )

    load_tasks()
    page.update()

if __name__ == '__main__':
    main_db.init_db()
    ft.app(target=main)
