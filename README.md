# Smart Assistive System for Dementia Patients

An intelligent assistive system designed to help **Dimentia patients** by using **face recognition** for identifying frequent visitors, **real-time GPS tracking**, and an **SOS emergency alert system** for caregivers.


## Features

- **Face Recognition for Identifying Visitors** – Identifies frequently visiting people.
- **Real-Time GPS Tracking** – Fetches live location data from the **Neo-6M GPS module**.
- **SOS Emergency Alert System** – Sends an emergency SMS with GPS coordinates.
- **Twilio SMS Integration** – Uses the **Twilio API** for instant alerts.
- **Raspberry Pi Compatibility** – Works on **Raspberry Pi 4B** with remappable GPIO pins.
- **User-Friendly GUI** – A **Tkinter-based** interface with an **SOS button**.
- **Customizable Caregiver Contact** – Modify the caregiver’s phone number easily.
- **Secure Face Recognition Data** – Stores and processes visitor face data.
- **Error Handling & Debugging** – Displays errors via **Tkinter message boxes**.
- **Portable & Expandable** – Can be **integrated into wearable or IoT devices**.


## Installation & Setup
**Clone the repo or download and extract the filew**

### Face Detection Setup

1. Collect Face Data

Run face_dataset.py to collect images of known faces.

2. Train the Model

Use face_training.py to train the system with stored images.

3. Run the Recognition System

Start face_recognition.py to detect and identify visitors.

## Twilio Setup
1. Get Twilio Credentials

Sign up at Twilio and get:

Account SID

Auth Token

Twilio Number

2. Store Credentials Securely

Add them to a .env file:


ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
TWILIO_NUMBER=your_twilio_phone_number
CAREGIVER_NUMBER=recipient_phone_number

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Team

- Ahammed Salahuddeen N Y 
- Angel Joy
- Fathima Hanna
- Harikesh S