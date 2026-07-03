import sqlite3

def init_db():
    #Creates the reminders table if it doesn't exist.
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            message TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )
    """)
    conn.commit()
    conn.close()

def save_reminder(date, time_str, message):
    #Saves a new reminder to the database.
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reminders (date, time, message) VALUES (?, ?, ?)",
        (date, time_str, message)
    )
    conn.commit()
    conn.close()

def get_pending_reminders():
    # Fetches all active reminders that haven't triggered yet.
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, time, message FROM reminders WHERE status = 'pending'")
    rows = cursor.fetchall()
    conn.close()
    return rows

def mark_as_triggered(reminder_id):
    # Updates a reminder's status so it doesn't fire repeatedly.
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE reminders SET status = 'triggered' WHERE id = ?", (reminder_id,))
    conn.commit()
    conn.close()