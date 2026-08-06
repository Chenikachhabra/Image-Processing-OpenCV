import cv2

# Read the image
img = cv2.imread("image.png")

# Display the image
cv2.imshow("Original Image", img)

# Save/write the image
cv2.imwrite("saved_image.jpg", img)

# Wait until any key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()