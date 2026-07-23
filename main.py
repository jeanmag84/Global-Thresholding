#importing Libs necessaries
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Your Image") # We need Choose a Image first.


# We need Convert Image correctly for GRAY
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)


# Value we can change for Value Tresh
limiar = 100


val, thresh = cv2.threshold(gray, limiar, 255, cv2.THRESH_BINARY)

# Look your new image :)
plt.imshow(thresh, cmap='gray')
plt.show()
