import sqlite3
from config import DB_PATH
from db import queries


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_TASKS)
    try:
        cursor.execute("ALTER TABLE tasks ADD COLUMN status TEXT DEFAULT 'в процессе'")
    except sqlite3.OperationalError:
        pass
    conn.commit()
    conn.close()


def get_tasks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, created_at, status FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks



def add_task_db(task):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, created_at, status) VALUES (?, CURRENT_TIMESTAMP, 'в процессе')", (task,))
    conn.commit()
    task_id = cursor.lastrowid
    cursor.execute("SELECT created_at, status FROM tasks WHERE id = ?", (task_id,))
    created_at, status = cursor.fetchone()
    conn.close()
    return task_id, created_at, status


def update_task_db(task_id, new_task):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_TASK, (new_task, task_id))
    conn.commit()
    conn.close()


def delete_task_db(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (task_id,))
    conn.commit()
    conn.close()

def update_task_db_status(task_id, new_status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    conn.close()



