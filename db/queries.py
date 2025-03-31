CREATE_TABLE_TASKS = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status INTEGER DEFAULT 0  -- Изменение: поле для статуса
    );
"""

SELECT_TASKS = "SELECT id, task, status FROM tasks ORDER BY created_at DESC"

SELECT_COMPLETED = "SELECT id, task, status FROM tasks WHERE status = 1 ORDER BY created_at DESC"

SELECT_INCOMPLETED = "SELECT id, task, status FROM tasks WHERE status = 0 ORDER BY created_at DESC"

SELECT_IN_PROGRESS = "SELECT id, task, status FROM tasks WHERE status = 2 ORDER BY created_at DESC"

INSERT_TASK = "INSERT INTO tasks (task) VALUES (?)"

UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"

UPDATE_TASK_STATUS = "UPDATE tasks SET status = ? WHERE id = ?"

DELETE_TASK = "DELETE FROM tasks WHERE id = ?"

DELETE_COMPLETED_TASKS = "DELETE FROM tasks WHERE status = 1"

