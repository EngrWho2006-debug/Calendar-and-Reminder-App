import time
from datetime import datetime
from plyer import notification
import database

def check_reminders_loop():
    # Background loop that checks for due reminders every 10 seconds.
    while True:
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M")

        # Fetch active reminders from DB
        reminders = database.get_pending_reminders()

        for rem_id, rem_date, rem_time, message in reminders:
            # Check if current time matches or has passed the scheduled time
            if rem_date == current_date and current_time >= rem_time:
                # Trigger OS notification
                notification.notify(
                    title="📅 Task Reminder!",
                    message=message,
                    app_name="CalendarApp",
                    timeout=10
                )
                # Update DB state
                database.mark_as_triggered(rem_id)
        
        # Sleep to save CPU cycles
        time.sleep(10)