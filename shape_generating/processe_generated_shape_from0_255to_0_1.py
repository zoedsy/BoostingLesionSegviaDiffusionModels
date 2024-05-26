import glob
import os
import cv2
from PIL import Image
import numpy as np
from skimage import filters
from skimage import color
import matplotlib.pyplot as plt

#this is to change the binarized img to 0,1 intensity ones
#process the generated shapes
# i = "./shape_generating/generated_shapes/synthetic_label_0999.png"
# root_write = "./shape_generating/processed_generated_shapes"
# img=Image.open(i)
# img=cv2.imread(i)
# B,G,R = cv2.split(img)
# B=(B/255).astype(int)
# # B[B==127]=1
# print("B",B)
# # B[B!=0]=1
# # B[B==0]=0
# cv2.imwrite(os.path.join(root_write,i.split("/")[-1]),B)
# ls= np.unique(img).tolist()
# print("ls",ls)
# results = ls.count(img.all())
# print("results",results)

# print("unique",np.unique(results))
# print("max",results.max())
# print("min",results.min())
# print("shape",results.shape)
# print("sum",results.sum())






#process new generated labels

# root = "./shape_generating/generated_shapes_new"
# root_write = "./shape_generating/processed_generated_shapes_new"

# root = "./shape_generating/test_label_transform"
# root_write = "./shape_generating/processed_test_label_transform"
# if not os.path.exists(root_write):
#     os.mkdir(root_write)
root = "./shape_generating/generated_shapes_new_plus_1000"
root_write = "./shape_generating/processed_generated_shapes_plus_1000"
paths = sorted(glob.glob(os.path.join(root,"*.png")))
for i in paths: 
    print("i",i)
    img=Image.open(i)
    img=cv2.imread(i)
    B,G,R = cv2.split(img)
    B=(B/255).astype(int)
    # B[B==127]=1 
    print("B",B)
    # B[B!=0]=1
    # B[B==0]=0
    cv2.imwrite(os.path.join(root_write,i.split("/")[-1]),B)
    ls= np.unique(img).tolist()
    # print("ls",ls)
    # break
    # results = ls.count(img.all())
    # print("results",results)

    # print("unique",np.unique(results))
    # print("max",results.max())
    # print("min",results.min())
    # print("shape",results.shape)
    # print("sum",results.sum())















  

