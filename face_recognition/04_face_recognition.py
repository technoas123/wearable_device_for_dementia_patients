import face_recognition
import cv2
import pickle
import os
import numpy as np
import pyttsx3
import time

# Define the absolute path to the model file
project_dir = os.path.dirname(os.path.abspath(__file__))  # Get the project directory
model_path = os.path.join(project_dir, "face_recognition_model.pkl")  # Absolute path to the model file

# Check if the model file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}. Please run train_model.py first.")

# Load the trained model and details
try:
    with open(model_path, "rb") as f:
        known_face_encodings, known_face_labels, known_face_details = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Set a custom threshold for face recognition
RECOGNITION_THRESHOLD = 0.5  # Adjust this value (default is 0.6)

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible")
    exit()

# Initialize text-to-speech engine
try:
    engine = pyttsx3.init()
    print("Text-to-speech engine initialized.")
except Exception as e:
    print(f"Error initializing text-to-speech engine: {e}")
    engine = None

# Variable to store the last recognized name and details
last_name = None
last_details = None
last_announcement_time = 0  # Track the last time the name was spoken
announcement_interval = 5  # Speak the name every 5 seconds

print("Recognizing faces. Press 'q' to quit...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Convert the frame from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all face locations and encodings in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the face with known faces
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = face_distances.argmin()

        # Use a custom threshold to determine if it's a match
        if face_distances[best_match_index] < RECOGNITION_THRESHOLD:
            name = known_face_labels[best_match_index]
            details = known_face_details[best_match_index]  # Get details for the recognized face

            # Speak the name and details if it's a new person
            if name != last_name and engine:
                # Announce the name and details
                announcement = f"Recognized {name}. {details[0]}, {details[1]}, {details[2]} years old."
                engine.say(announcement)
                engine.runAndWait()
                last_name = name
                last_details = details
                last_announcement_time = time.time()  # Reset the announcement timer

            # Speak the name repeatedly at the specified interval
            if name == last_name and engine:
                current_time = time.time()
                if current_time - last_announcement_time >= announcement_interval:
                    engine.say(f"Recognized {name}")
                    engine.runAndWait()
                    last_announcement_time = current_time  # Reset the announcement timer

            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Draw the name below the face
            cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Display details in a separate window (like an ID card)
            id_card = np.zeros((300, 500, 3), dtype=np.uint8)  # Create a blank image for the ID card
            cv2.putText(id_card, "ID Card", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(id_card, f"Name: {details[0]}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            cv2.putText(id_card, f"Relationship: {details[1]}", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            cv2.putText(id_card, f"Age: {details[2]}", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            cv2.imshow("ID Card", id_card)  # Show the ID card in a separate window
        else:
            name = "Unknown"

    # Display the frame
    cv2.imshow("Face Recognition", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()