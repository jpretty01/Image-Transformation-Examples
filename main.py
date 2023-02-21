import cv2
import numpy as np
import os 

# Getting the file path for both images
subject1 = os.path.join(os.path.dirname(__file__), 'Bank.jpg')

# Load the "Banknotes" image
img = cv2.imread(subject1)



# Define the transformation matrices
# Translation: move the image 50 pixels to the right and 100 pixels down
T = np.float32([[1, 0, 50], [0, 1, 100]])
# Rotation: rotate the image by 30 degrees clockwise around its center
R = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), 30, 1)
# Scaling: scale the image by a factor of 1.5 along both axes
S = np.float32([[1.5, 0, 0], [0, 1.5, 0]])

# Apply the transformations to the image
translated = cv2.warpAffine(img, T, (img.shape[1], img.shape[0]))
rotated = cv2.warpAffine(img, R, (img.shape[1], img.shape[0]))
scaled = cv2.warpAffine(img, S, (img.shape[1], img.shape[0]))

# Display the transformed images
cv2.imshow("Translated image", translated)
cv2.imshow("Rotated image", rotated)
cv2.imshow("Scaled image", scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
