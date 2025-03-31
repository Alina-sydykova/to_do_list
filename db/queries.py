CREATE_TABLE_TASKS = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completed INTEGER DEFAULT 0
    );
"""

SELECT_TASKS = "SELECT id, task, created_at, completed FROM tasks ORDER BY created_at DESC"

SELECT_COMPLETED = "SELECT id, task, created_at, completed FROM tasks WHERE completed = 1 ORDER BY created_at DESC"

SELECT_INCOMPLETED = "SELECT id, task, created_at, completed FROM tasks WHERE completed = 0 ORDER BY created_at DESC"

INSERT_TASK = "INSERT INTO tasks (task) VALUES (?)"

UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"

DELETE_TASK = "DELETE FROM tasks WHERE id = ?"

UPDATE_TASK_STATUS = "UPDATE tasks SET completed = ? WHERE id = ?"

DELETE_COMPLETED_TASKS = "DELETE FROM tasks WHERE completed = 1"


