Smart Assistive System for Dementia Patients

An intelligent assistive system designed to help Alzheimer’s patients by using face recognition for identifying frequent visitors, real-time GPS tracking, and an SOS emergency alert system for caregivers.

Features

Face Recognition for Identifying Visitors – Helps patients recognize known individuals by identifying frequently visiting people.

Real-Time GPS Tracking – Fetches live location data from the Neo-6M GPS module to track the user’s position.

SOS Emergency Alert System – Sends an emergency alert with GPS coordinates via SMS to a designated caregiver.

Twilio SMS Integration – Uses the Twilio API to send instant alerts.

Raspberry Pi Compatibility – Works on Raspberry Pi 4B, with remappable GPIO pins for flexibility.

User-Friendly GUI – A simple Tkinter-based interface featuring an SOS button for emergencies.

Customizable Caregiver Contact – Allows modification of the recipient’s phone number.

Secure Face Recognition Data – Maintains a database of known faces for accurate identification.

Error Handling & Debugging – Displays errors using Tkinter message boxes for easy troubleshooting.

Portable & Expandable – Can be integrated into wearable or IoT devices and expanded with voice alerts or cloud integration.



---

Installation & Setup

1. Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install Dependencies

pip install opencv-python numpy twilio pigpio

Ensure you have OpenCV, NumPy, Twilio, and PiGPIO installed for the face recognition and GPS tracking features.

3. Enable Raspberry Pi Serial Interface

Enable the UART interface for GPS communication:

sudo raspi-config

Go to Interfacing Options > Serial

Disable login shell access, but enable serial hardware

Reboot the Raspberry Pi


sudo reboot

4. Start PiGPIO Daemon

sudo pigpiod

5. Run the Smart Assistive System

python3 main.py


---

Face Recognition Setup

1. Collect Face Data

Run the face data collection script (face_dataset.py) to store known faces.



2. Train the Model

Use face_training.py to train the system on collected images.



3. Run the Recognition System

Start face_recognition.py to identify visitors.





---

Twilio SMS Configuration

1. Get Twilio Credentials

Sign up at Twilio and obtain your Account SID, Auth Token, and Twilio Number.



2. Update Environment Variables

Store credentials securely in a .env file:


ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
TWILIO_NUMBER=your_twilio_phone_number
CAREGIVER_NUMBER=recipient_phone_number




---

File Structure

📂 Smart-Assistive-System
│── 📄 Ui.py                # Main application script
│── 📄 face_recognition.py     # Face recognition module
│── 📄 gps_tracking.py         # GPS tracking module
│── 📄 sos_alert.py            # SMS alert system
│── 📂 facedata/                   # Stores trained face data
│── 📂 models/                 # Pre-trained face recognition models
│── 📄 README.md               # Project documentation


---

Contributing

1. Fork the repository


2. Create a new branch (git checkout -b feature-name)


3. Commit your changes (git commit -m "Add new feature")


4. Push to your branch (git push origin feature-name)


5. Open a Pull Request




---

License

This project is licensed under the MIT License.


---

Acknowledgments

Twilio API for SMS alerts

OpenCV for face recognition

Raspberry Pi Foundation for hardware support



---

The Team

Ahammed Salahuddeen N Y 
Angel Joy 
Fathima Hanna
Harikesh S

---


