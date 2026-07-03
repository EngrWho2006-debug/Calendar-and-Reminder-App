import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
import database

class CalendarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Calendar & Reminder App")
        self.geometry("450x550")
        self.config(padx=15, pady=15)
        
        self.create_widgets()

    def create_widgets(self):
        # 1. Calendar
        tk.Label(self, text="Select Date:", font=("Arial", 11, "bold")).pack(anchor="w", pady=2)
        # Formatted to YYYY-MM-DD for easier DB sorting
        self.cal = Calendar(self, selectmode='day', date_pattern='yyyy-mm-dd')
        self.cal.pack(fill="x", expand=True, pady=5)

        # 2. Time Picker Frame
        tk.Label(self, text="Select Time (24h format):", font=("Arial", 11, "bold")).pack(anchor="w", pady=2)
        time_frame = tk.Frame(self)
        time_frame.pack(fill="x", pady=5)

        # Hours Dropdown (00-23)
        self.hour_cb = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(24)], width=5, state="readonly")
        self.hour_cb.set("12")
        self.hour_cb.pack(side="left", padx=2)
        
        tk.Label(time_frame, text=":").pack(side="left")

        # Minutes Dropdown (00-59)
        self.min_cb = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(60)], width=5, state="readonly")
        self.min_cb.set("00")
        self.min_cb.pack(side="left", padx=2)

        # 3. Reminder Text Info
        tk.Label(self, text="Reminder Message:", font=("Arial", 11, "bold")).pack(anchor="w", pady=5)
        self.msg_entry = tk.Entry(self, font=("Arial", 11), width=40)
        self.msg_entry.pack(fill="x", pady=2)

        # 4. Save Button
        save_btn = tk.Button(self, text="🔔 Save Reminder", bg="#007BFF", fg="white", 
                             font=("Arial", 11, "bold"), command=self.add_reminder)
        save_btn.pack(fill="x", pady=15)

    def add_reminder(self):
        date = self.cal.get_date()
        time_str = f"{self.hour_cb.get()}:{self.min_cb.get()}"
        message = self.msg_entry.get().strip()

        if not message:
            messagebox.showwarning("Missing Info", "Please enter a reminder text.")
            return

        # Save to SQLite DB
        database.save_reminder(date, time_str, message)
        
        messagebox.showinfo("Success", f"Reminder saved for {date} at {time_str}!")
        self.msg_entry.delete(0, tk.END) # Clear text input