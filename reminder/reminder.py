import tkinter as tk
from tkinter import simpledialog, messagebox
import time
import threading

# Global variables
reminder_times = []

# Function to get medication times from the user
def get_medication_times():
    global reminder_times
    while True:
        time_str = simpledialog.askstring("Input", "Enter medication time (HH:MM, 24-hour format):")
        if not time_str:
            break
        try:
            # Convert input to hours and minutes
            hours, minutes = map(int, time_str.split(':'))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                reminder_times.append((hours, minutes))
            else:
                messagebox.showerror("Error", "Invalid time. Please enter a valid time in HH:MM format.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter time in HH:MM format.")

# Function to check medication time
def check_medication_time():
    while True:
        # Get the current time
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        # Check if it's time for medication
        for med_time in reminder_times:
            if (current_hour, current_minute) == med_time:
                # Trigger medication reminder
                flash_red_screen()
                time.sleep(60)  # Wait for 1 minute to avoid multiple triggers

        # Check every 30 seconds
        time.sleep(30)

# Function to flash a red screen with reminder text
def flash_red_screen():
    # Create a fullscreen red window
    flash_window = tk.Tk()
    flash_window.attributes("-fullscreen", True)
    flash_window.configure(bg="red")

    # Add reminder text
    reminder_label = tk.Label(
        flash_window,
        text="Time to take your medication!",
        font=("Arial", 50),
        fg="white",
        bg="red"
    )
    reminder_label.pack(expand=True)

    # Flash the window for 5 seconds
    flash_window.update()
    time.sleep(5)
    flash_window.destroy()

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Get medication times from the user
get_medication_times()

# Start the medication reminder check in a separate thread
if reminder_times:
    medication_thread = threading.Thread(target=check_medication_time, daemon=True)
    medication_thread.start()

    # Show a confirmation message
    messagebox.showinfo("Reminder Set", f"Medication reminders set for: {reminder_times}")

    # Run the Tkinter event loop
    root.mainloop()
else:
    messagebox.showinfo("No Reminders", "No medication times were entered. Exiting.")