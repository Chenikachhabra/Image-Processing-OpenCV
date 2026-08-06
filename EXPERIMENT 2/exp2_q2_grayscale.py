import cv2
import numpy as np

# Read color image
img = cv2.imread("image2.png")

if img is None:
    print("Error: image2.png not found")
    exit()

# OpenCV reads image in BGR order
B = img[:, :, 0].astype(float)
G = img[:, :, 1].astype(float)
R = img[:, :, 2].astype(float)


# ------------------------------------
# CASE 1: Mean of R, G and B channels
# ------------------------------------

gray_mean = (R + G + B) / 3

gray_mean = gray_mean.astype(np.uint8)

cv2.imshow("Original Color Image", img)
cv2.imshow("Grayscale - Mean Average", gray_mean)

cv2.imwrite("grayscale_mean.jpg", gray_mean)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ------------------------------------
# CASE 2: User-defined RGB weightages
# ------------------------------------

wr = float(input("Enter Red weight (0 to 1): "))
wg = float(input("Enter Green weight (0 to 1): "))
wb = float(input("Enter Blue weight (0 to 1): "))

# Check individual weights
if not (0 <= wr <= 1 and
        0 <= wg <= 1 and
        0 <= wb <= 1):

    print("Each weight must be between 0 and 1")
    exit()

# Check total weight
if not np.isclose(wr + wg + wb, 1.0):

    print("Sum of R, G and B weights must be equal to 1")
    exit()

# Weighted grayscale conversion
gray_weighted = (
    wr * R +
    wg * G +
    wb * B
)

gray_weighted = gray_weighted.astype(np.uint8)

cv2.imshow("Original Color Image", img)
cv2.imshow("Weighted Grayscale Image", gray_weighted)

cv2.imwrite("grayscale_weighted.jpg", gray_weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()