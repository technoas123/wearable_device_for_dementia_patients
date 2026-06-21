# Smart Assistive System for Dementia Patients

An intelligent assistive platform developed to enhance the safety and independence of individuals living with dementia and memory-related conditions. The system combines computer vision, location tracking, and emergency communication technologies to help caregivers monitor and support patients in real time.

The project integrates face recognition, GPS tracking, and SMS-based emergency alerts into a unified Raspberry Pi-based solution capable of identifying familiar visitors, monitoring patient location, and notifying caregivers during emergencies.

* * *

## 🚀 Project Overview

Patients with dementia often face challenges related to memory loss, disorientation, and emergency response. This project aims to address these issues through an embedded system capable of:

-   Recognizing familiar individuals through facial recognition
    
-   Tracking patient location in real time
    
-   Sending emergency alerts with GPS coordinates
    
-   Providing a simple and accessible user interface
    

The system demonstrates how embedded computing, computer vision, and IoT technologies can be applied to healthcare and assisted living applications.

* * *

## ✨ Key Features

### 👤 Face Recognition System

-   Detects and identifies frequently visiting individuals
    
-   Uses OpenCV-based facial recognition
    
-   Maintains a database of known faces
    

### 📍 Real-Time GPS Tracking

-   Integrates a Neo-6M GPS module
    
-   Retrieves live geographic coordinates
    
-   Supports location monitoring and emergency tracking
    

### 🚨 Emergency SOS System

-   Dedicated SOS functionality
    
-   Sends emergency notifications to caregivers
    
-   Includes current GPS location in alerts
    

### 📩 SMS Notifications

-   Twilio API integration
    
-   Automated emergency messaging
    
-   Real-time communication with caregivers
    

### 🖥 User-Friendly Interface

-   Built using Tkinter
    
-   Simple and accessible controls
    
-   Designed for ease of use
    

### 🔧 Embedded Deployment

-   Optimized for Raspberry Pi 4B
    
-   GPIO integration for hardware expansion
    
-   Portable and scalable architecture
    

* * *

## 🏗 System Architecture

    Patient Interaction
            │
            ▼
     Raspberry Pi 4B
            │
     ┌──────┼──────┐
     │      │      │
     ▼      ▼      ▼
    
    Face   GPS    SOS
    Recognition Tracking Alert
    
     │       │       │
     └───┬───┴───┬───┘
         ▼       ▼
    
     Twilio SMS Notification
              │
              ▼
    
          Caregiver
    

* * *

## 🛠 Technologies Used

### Hardware

-   Raspberry Pi 4B
    
-   Neo-6M GPS Module
    

### Software

-   Python
    
-   OpenCV
    
-   Tkinter
    
-   Twilio API
    

### Concepts

-   Computer Vision
    
-   Embedded Systems
    
-   IoT
    
-   Healthcare Technology
    

* * *

## 📂 Project Structure

    wearable_device_for_dementia_patients/
    
    ├── face_dataset.py
    ├── face_training.py
    ├── face_recognition.py
    ├── gps_tracker.py
    ├── sos_alert.py
    ├── gui/
    ├── models/
    ├── datasets/
    ├── assets/
    └── README.md
    

* * *

## ⚙️ Installation

### Clone Repository

    git clone https://github.com/yourusername/wearable_device_for_dementia_patients.git
    

### Install Dependencies

    pip install -r requirements.txt
    

* * *

## 📸 Face Recognition Setup

### 1\. Collect Face Data

    python face_dataset.py
    

### 2\. Train Recognition Model

    python face_training.py
    

### 3\. Start Recognition System

    python face_recognition.py
    

* * *

## 📩 Twilio Configuration

Create a `.env` file:

    ACCOUNT_SID=your_twilio_account_sid
    AUTH_TOKEN=your_twilio_auth_token
    TWILIO_NUMBER=your_twilio_number
    CAREGIVER_NUMBER=recipient_phone_number
    

* * *

## 🎯 Applications

-   Dementia Patient Assistance
    
-   Elderly Care Monitoring
    
-   Healthcare IoT Systems
    
-   Assistive Technologies
    
-   Emergency Response Systems
    

* * *

## 🔮 Future Improvements

-   Medication Reminder System
    
-   Mobile Companion Application
    
-   Voice Assistant Integration
    
-   Fall Detection
    
-   Cloud-Based Monitoring Dashboard
    
-   Geofencing Alerts
    
-   AI-Based Behavioral Analysis
    

* * *

## 👥 Team

-   Ahammed Salahuddeen N Y
    
-   Angel Joy
    
-   Fathima Hanna
    
-   Harikesh S
    

* * *

## 📄 License

Licensed under the MIT License.

* * *

## ❤️ Motivation

This project was developed with the goal of exploring how embedded systems and intelligent technologies can be leveraged to improve quality of life, safety, and independence for individuals living with dementia.
