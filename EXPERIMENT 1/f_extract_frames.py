import cv2
import os

# Open video
cap = cv2.VideoCapture("video.mp4")

# Create a folder named frames
os.makedirs("frames", exist_ok=True)

frame_count = 0

while True:

    # Read frame
    ret, frame = cap.read()

    # Stop when video ends
    if not ret:
        break

    # Save current frame as image
    cv2.imwrite(
        f"frames/frame_{frame_count}.jpg",
        frame
    )

    frame_count += 1

# Release video
cap.release()

print("Frames extracted successfully!")
print("Total frames:", frame_count)