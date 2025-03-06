import serial
import os
from twilio.rest import Client
from tkinter import messagebox


# Twilio credentials
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
CAREGIVER_NUMBER = os.getenv('CAREGIVER_NUMBER')

# Initialize Twilio client
twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Function to get GPS location from Neo-6M module
def get_gps_location():
    try:
        # Open serial connection to GPS module
        ser = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)
        
        while True:
            # Read a line of data from the GPS module
            data = ser.readline().decode('utf-8', errors='ignore')
            
            # Check if the data is a valid NMEA sentence
            if data.startswith('$GPGGA'):
                # Parse the NMEA sentence
                parts = data.split(',')
                if parts[2] and parts[4]:  # Check if latitude and longitude are available
                    latitude = float(parts[2][:2]) + float(parts[2][2:]) / 60  # Convert to decimal degrees
                    if parts[3] == 'S':
                        latitude = -latitude
                    longitude = float(parts[4][:3]) + float(parts[4][3:]) / 60  # Convert to decimal degrees
                    if parts[5] == 'W':
                        longitude = -longitude
                    return latitude, longitude
    except serial.SerialException as e:
        messagebox.showerror("GPS Error", f"Failed to connect to GPS module: {e}")
        return None, None
    except Exception as e:
        messagebox.showerror("GPS Error", f"Failed to fetch GPS data: {e}")
        return None, None
    finally:
        if 'ser' in locals():
            ser.close()

# Function to send SOS alert
def send_sos_alert():
    latitude, longitude = get_gps_location()
    if latitude is None or longitude is None:
        messagebox.showerror("Error", "Failed to fetch GPS location.")
        return
    
    message = f"Emergency! Patient needs help. Location: Latitude {latitude:.6f}, Longitude {longitude:.6f}"
    
    try:
        # Send SMS using Twilio
        twilio_client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=CAREGIVER_NUMBER
        )
        messagebox.showinfo("SOS Alert", "Emergency alert sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send alert: {e}")