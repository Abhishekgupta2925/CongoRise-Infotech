import tkinter as tk
from tkinter import simpledialog
from datetime import datetime, timedelta
import winsound  # Windows-specific library for sound

class AlarmClockApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarm Clock")

        self.alarm_time = None

        self.label = tk.Label(master, text="Set Alarm Time:")
        self.label.pack()

        self.button_set_alarm = tk.Button(master, text="Set Alarm", command=self.set_alarm)
        self.button_set_alarm.pack()

        self.button_clear_alarm = tk.Button(master, text="Clear Alarm", command=self.clear_alarm)
        self.button_clear_alarm.pack()

        self.label_alarm_time = tk.Label(master, text="")
        self.label_alarm_time.pack()

        self.update_clock()

    def set_alarm(self):
        alarm_time_str = simpledialog.askstring("Set Alarm", "Enter alarm time (HH:MM):")
        if alarm_time_str:
            try:
                alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
                now = datetime.now()
                self.alarm_time = now.replace(hour=alarm_time.hour, minute=alarm_time.minute, second=0, microsecond=0)
                self.label_alarm_time.config(text=f"Alarm set for {self.alarm_time.strftime('%H:%M')}")
            except ValueError:
                self.label_alarm_time.config(text="Invalid time format. Please use HH:MM.")

    def clear_alarm(self):
        self.alarm_time = None
        self.label_alarm_time.config(text="")

    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        if self.alarm_time and datetime.now() >= self.alarm_time:
            self.label_alarm_time.config(text="Alarm!")
            winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC)
            self.clear_alarm()
        else:
            self.label_alarm_time.config(text=current_time)
        self.master.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()
