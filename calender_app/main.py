import threading
import database
from ui import CalendarApp
from reminders import check_reminders_loop

def main():
    # 1. Initialize DB file and tables
    database.init_db()

    """
     2. Start the reminder monitor thread asynchronously 
     daemon=True makes sure this thread kills itself when the UI is closed.
    """
    monitor_thread = threading.Thread(target=check_reminders_loop, daemon=True)
    monitor_thread.start()

    # 3. Run UI application
    app = CalendarApp()
    app.mainloop()

if __name__ == "__main__":
    main()