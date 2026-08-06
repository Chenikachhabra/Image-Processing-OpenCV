import cv2

# Read original image
img = cv2.imread("image.png")

# Convert and save in different formats
cv2.imwrite("converted_image.jpg", img)
cv2.imwrite("converted_image.tiff", img)
cv2.imwrite("converted_image.bmp", img)
cv2.imwrite("converted_image.webp", img)

print("Image converted successfully!")