import cv2
import os

# Getting the file path for both images
bank_note = os.path.join(os.path.dirname(__file__), 'bank.jpg')

# Load the "Banknotes" image
img = cv2.imread(bank_note)

# Convert the image to grayscale and apply a binary threshold using Otsu's method
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the thresholded image
cv2.imshow("Thresholded image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
