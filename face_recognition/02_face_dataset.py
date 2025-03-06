import cv2
import os

# Create a directory to store the dataset
dataset_dir = "face_dataset1"
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# Ask for the person's name
person_name = input("Enter the person's name: ")
person_dir = os.path.join(dataset_dir, person_name)
if not os.path.exists(person_dir):
    os.makedirs(person_dir)

# Initialize webcam
cap = cv2.VideoCapture(0)
count = 0

print("Capturing images. Press 'q' to quit...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow("Capture Dataset", frame)

    # Save the frame as an image
    img_path = os.path.join(person_dir, f"{count}.jpg")
    cv2.imwrite(img_path, frame)
    count += 1

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
print(f"Dataset saved in {person_dir}")