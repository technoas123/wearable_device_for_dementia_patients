import face_recognition
import os
import pickle

# Path to the dataset
dataset_dir = r"C:\Users\ahamm\OneDrive\Documents\MY PROJECTS\Mini Project\FaceRecognitionProject\face_dataset1"

# Lists to store face encodings, labels, and additional details
known_face_encodings = []
known_face_labels = []
known_face_details = []  # Store additional details (e.g., name, relationship, etc.)

# Loop through each person's folder
for person_name in os.listdir(dataset_dir):
    person_dir = os.path.join(dataset_dir, person_name)
    if not os.path.isdir(person_dir):
        continue

    # Load details for the person (e.g., from a text file)
    details_file = os.path.join(person_dir, "details.txt")
    if os.path.exists(details_file):
        with open(details_file, "r") as f:
            details = f.read().strip().split(",")  # Format: Name, Relationship, etc.
    else:
        details = [person_name, "N/A", "N/A"]  # Default details if file not found

    # Loop through each image of the person
    for image_name in os.listdir(person_dir):
        if image_name.endswith(".jpg") or image_name.endswith(".png"):
            image_path = os.path.join(person_dir, image_name)
            image = face_recognition.load_image_file(image_path)

            # Get face encodings for the image
            face_encodings = face_recognition.face_encodings(image)
            if len(face_encodings) > 0:
                known_face_encodings.append(face_encodings[0])
                known_face_labels.append(person_name)
                known_face_details.append(details)  # Add details for this person

# Save the trained model and details to a file
model_path = "face_recognition_model.pkl"
with open(model_path, "wb") as f:
    pickle.dump((known_face_encodings, known_face_labels, known_face_details), f)

print(f"Model trained and saved to {model_path}")