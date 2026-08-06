import cv2
import numpy as np

# Read image in grayscale
gray = cv2.imread("image2.png", cv2.IMREAD_GRAYSCALE)

if gray is None:
    print("Error: image2.png not found")
    exit()

# -------------------------
# CASE 1: Mean as threshold
# -------------------------

mean_threshold = np.mean(gray)

print("Mean threshold value:", mean_threshold)

binary_mean = np.where(
    gray > mean_threshold,
    255,
    0
).astype(np.uint8)

cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Binary Image - Mean Threshold", binary_mean)

cv2.imwrite("binary_mean.jpg", binary_mean)

cv2.waitKey(0)
cv2.destroyAllWindows()


# -------------------------
# CASE 2: User threshold
# -------------------------

threshold = int(input("Enter threshold value between 0 and 255: "))

if threshold < 0 or threshold > 255:
    print("Threshold must be between 0 and 255")
    exit()

binary_user = np.where(
    gray > threshold,
    255,
    0
).astype(np.uint8)

cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Binary Image - User Threshold", binary_user)

cv2.imwrite("binary_user.jpg", binary_user)

cv2.waitKey(0)
cv2.destroyAllWindows()