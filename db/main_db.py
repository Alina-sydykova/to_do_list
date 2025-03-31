import sqlite3


CREATE_TABLE_TASKS = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completed INTEGER DEFAULT 0
    );
"""

class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    def init_db(self):
        """Создание таблицы задач, если она еще не существует."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(CREATE_TABLE_TASKS)
            conn.commit()

    def get_tasks(self, filter_type="all"):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            if filter_type == 'completed':
                cursor.execute("SELECT id, task, completed FROM tasks WHERE completed = 1 ORDER BY created_at DESC")
            elif filter_type == "incompleted":
                cursor.execute("SELECT id, task, completed FROM tasks WHERE completed = 0 ORDER BY created_at DESC")
            else:
                cursor.execute("SELECT id, task, completed FROM tasks ORDER BY created_at DESC")
            
            return cursor.fetchall()

    def add_task_db(self, task):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
            return cursor.lastrowid

    def update_task_db(self, task_id, task_text=None, completed=None):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            if task_text is not None:
                cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (task_text, task_id))
            if completed is not None:
                cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))

    def delete_task_db(self, task_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    def delete_completed_tasks(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE completed = 1")


main_db = Database("tasks.db")
