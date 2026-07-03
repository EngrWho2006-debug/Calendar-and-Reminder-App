#  Desktop Calendar & Reminder Application

A lightweight, reliable desktop application built with Python that allows users to pick dates, schedule specific reminder times, and receive real-time native OS desktop notifications. The app uses a background worker thread to manage countdown checks and saves all data locally via SQLite so reminders persist even after closing the program.

---

##  Features

- **Interactive GUI Calendar:** Clean date picker using `tkcalendar`.
- **Precise 24-Hour Time Configuration:** Dropdown pickers for hours and minutes.
- **Persistent Local Database:** Built on SQLite to keep track of past and upcoming reminders.
- **Background Worker Engine:** Multi-threaded polling system that monitors scheduled timestamps without lagging the user interface.
- **Native OS Push Notifications:** Uses `plyer` to deliver slide-out popups directly via Windows, macOS, or Linux toast managers.

---
## Author

Pragya Singh

---

##  Project Architecture

```text
Calender and Reminder App/
│
├── calender_app/         # Core application directory
│   ├── database.py       # SQLite connection layer and schema execution
│   ├── reminders.py      # Background thread polling loop and OS notification router
│   ├── ui.py             # Tkinter window layout, theme setup, and validation logic
│   └── main.py           # Application bootstrap and engine entry point
│
├── .gitignore            # Tells Git to exclude localized caches and virtual envs
└── README.md             # Project documentation (this file)

