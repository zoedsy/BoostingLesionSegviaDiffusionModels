import numpy as np
import cv2

img = np.zeros((512, 512, 1), dtype = "uint8")
cv2.imwrite('black_512p.png',img)
