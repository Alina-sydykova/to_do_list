import sqlite3

def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status INTEGER DEFAULT 0,  -- Статус задачи: 0 - невыполнено, 1 - выполнено, 2 - в работе
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()


def add_task_db(task_text):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task_text,))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

def get_tasks(filter_type):
    conn = get_db_connection()
    cursor = conn.cursor()

    if filter_type == 'completed':
        cursor.execute("SELECT id, task, status FROM tasks WHERE status = 1 ORDER BY created_at DESC")
    elif filter_type == 'inprogress':
        cursor.execute("SELECT id, task, status FROM tasks WHERE status = 2 ORDER BY created_at DESC")
    else:
        cursor.execute("SELECT id, task, status FROM tasks ORDER BY created_at DESC")
    
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task_db(task_id, task_text):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (task_text, task_id))
    conn.commit()
    conn.close()

def update_status_db(task_id, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()

def delete_task_db(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def delete_completed_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE status = 1")
    conn.commit()
    conn.close()
