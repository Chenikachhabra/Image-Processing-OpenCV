import cv2

# Read image
img = cv2.imread("image.png")

# Resize image
resized_img = cv2.resize(img, (400, 300))

# Display original image
cv2.imshow("Original Image", img)

# Display resized image
cv2.imshow("Resized Image", resized_img)

# Save resized image
cv2.imwrite("resized_image.jpg", resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()