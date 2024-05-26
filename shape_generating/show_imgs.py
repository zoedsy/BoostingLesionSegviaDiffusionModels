import matplotlib.pyplot as plt
import glob
import os
import cv2
img_root = "./shape_generating/generated_shapes_new"

paths = sorted(glob.glob(os.path.join(img_root,"*.png")))

plt.figure()
for i in range(1,32):
    img = cv2.imread(paths[i])
    plt.subplot(4,8,i)
plt.imshow("whole.png")
