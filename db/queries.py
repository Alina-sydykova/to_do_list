CREATE_TABLE_TASKS = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT 'в процессе'
    );
"""

SELECT_TASKS = "SELECT id, task, created_at, status FROM tasks ORDER BY created_at DESC"

INSERT_TASK = "INSERT INTO tasks (task) VALUES (?)"

UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"

DELETE_TASK = "DELETE FROM tasks WHERE id = ?"

UPDATE_TASK_STATUS = "UPDATE tasks SET status = ? WHERE id = ?"
