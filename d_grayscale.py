import cv2

# Read colored image
img = cv2.imread("image.png")

# Convert colored image into grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display original image
cv2.imshow("Colored Image", img)

# Display grayscale image
cv2.imshow("Grayscale Image", gray_img)

# Save grayscale image
cv2.imwrite("grayscale_image.jpg", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()