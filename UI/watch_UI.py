import tkinter as tk
from tkinter import ttk
import subprocess

def run_face_recognition():
    try:
        #script_path = script_path_here
        subprocess.Popen(['python', script_path])
    except Exception as e:
        print(f"Error: {e}")

def run_gps_navigation():
    try:
        #script_path = script_path_here
        subprocess.Popen(['python', script_path])
    except Exception as e:
        print(f"Error: {e}")

def add_face_to_dataset():
    try:
        #script_path = script_path_here
        subprocess.Popen(['python', script_path])
    except Exception as e:
        print(f"Error: {e}")

def check_database():
    try:
        #script_path = script_path_here
        subprocess.Popen(['python', script_path])
    except Exception as e:
        print(f"Error: {e}")

def sos_alert():
    try:
        # Replace with actual emergency call logic if needed
        print("SOS Alert Triggered!")
    except Exception as e:
        print(f"Error: {e}")

# UI Setup
root = tk.Tk()
root.title("Smart Watch UI")
root.geometry("320x350")
root.configure(bg="black")

welcome_label = tk.Label(root, text="Smart Watch", font=("Helvetica", 16), fg="white", bg="black")
welcome_label.pack(pady=10)

btn_face_recognition = ttk.Button(root, text="Face Recognition", command=run_face_recognition)
btn_face_recognition.pack(pady=5)

btn_gps = ttk.Button(root, text="GPS Navigation", command=run_gps_navigation)
btn_gps.pack(pady=5)

btn_add_face = ttk.Button(root, text="Add Face to Dataset", command=add_face_to_dataset)
btn_add_face.pack(pady=5)

btn_check_database = ttk.Button(root, text="Check Database", command=check_database)
btn_check_database.pack(pady=5)

# SOS Button (Red)
btn_sos = tk.Button(root, text="SOS Emergency", command=sos_alert, fg="white", bg="red", font=("Helvetica", 12, "bold"))
btn_sos.pack(pady=10)

btn_exit = ttk.Button(root, text="Exit", command=root.quit)
btn_exit.pack(pady=5)

root.mainloop()
