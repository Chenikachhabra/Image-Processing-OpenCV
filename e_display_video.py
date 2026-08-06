import cv2

# Open video
cap = cv2.VideoCapture("video.mp4")

while True:

    # Read one frame
    ret, frame = cap.read()

    # If video ends, stop
    if not ret:
        break

    # Display current frame
    cv2.imshow("Video", frame)

    # Press q to stop video
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release video
cap.release()

# Close windows
cv2.destroyAllWindows()