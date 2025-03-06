📌 Smart Assistive System

A real-time emergency alert system using a OpenCV, GPS module (Neo-6M), Raspberry Pi, and Twilio SMS API, OpenRouteService navigation API to notify caregivers of a patient's location in distress.

📝 Table of Contents
📌 Smart Assistive System
📝 Table of Contents
📖 Overview
🎯 Features
🖥️ Tech Stack
🚀 Installation & Setup
1️⃣ Clone the Repository
2️⃣ Install Dependencies
3️⃣ Set Up Environment Variables
4️⃣ Run the Application
📸 Screenshots
🚀 Future Enhancements
🤝 Contributing
📜 License
📞 Contact
📖 Overview
This Smart Assistive System is designed to help the users get the info about the people via face recognition system. Caregivers can track and assist patients in distress by sending an SOS alert with live GPS coordinates via SMS. It runs on a Raspberry Pi connected to a Neo-6M GPS module, and uses Twilio API to send alerts.

🎯 Features
✅ Face-recognition system of trained faces
✅ Real-time GPS tracking (Neo-6M)
✅ SOS button to send emergency alerts
✅ OpenRouteService API for easy navigation towards pre stored places
✅ Twilio SMS integration for caregiver notifications
✅ Medication Reminder System
✅ User-friendly GUI built with Tkinter
✅ Plug-and-play support for Raspberry Pi

🖥️ Tech Stack
Programming Language: Python
Hardware: Raspberry Pi, Neo-6M GPS Module
GUI: Tkinter
API: Twilio SMS, OenRouteService navigation API
Libraries: serial, tkinter, twilio, python-dotenv, opencv, face_recognition, pyttsx3, pickle, openrouteservice
🚀 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/smart-assistive-system.git
cd smart-assistive-system
2️⃣ Install Dependencies
Ensure Python and pip are installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
(Add all necessary dependencies in requirements.txt)

ACCOUNT_SID=your_twilio_sid
AUTH_TOKEN=your_twilio_auth_token
TWILIO_NUMBER=your_twilio_number
CAREGIVER_NUMBER=caregiver_phone_number

4️⃣ Run the Application
bash
Copy
Edit
python app.py

🚀 Future Enhancements
🔹 Add voice-based SOS activation
🔹 Implement location history tracking
🔹 Develop a mobile app for caregivers

🤝 Contributing
Contributions are welcome!

Fork the repo
Create a new branch (git checkout -b feature-name)
Commit changes (git commit -m "Added new feature")
Push the branch (git push origin feature-name)
Open a Pull Request
📜 License
This project is licensed under the MIT License. See LICENSE for details.

👨‍💻Team
Ahammed Salahuddeen N Y
Angel Joy
Fathima Hanna
Harikesh S
