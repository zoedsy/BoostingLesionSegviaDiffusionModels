# # from PIL import Image, ImageDraw

# # def ellipse(output_path):
# #     image = Image.new("RGB", (400, 400), "white")
# #     draw = ImageDraw.Draw(image)
# #     draw.ellipse((25, 50, 175, 200), fill="red")
# #     draw.ellipse((100, 150, 275, 300), outline="black", width=5,
# #                  fill="yellow")
# #     image.save(output_path)

# # if __name__ == "__main__":
# #     ellipse("ellipse.jpg")


# import the necessary packages
#generate new shapes(location mostly centered)
import numpy as np
import cv2
import elasticdeform
import random
from skimage import measure
random.seed(0)
f = open('log.txt','a')
num_png = -1
for i in range(0, 15000):
    # Create canvas and draw a white circle at the center of the canvas with
    # increasing radii - from 25 pixels to 150 pixels
    # concentric circles
    canvas = np.zeros((512, 512), dtype="uint8")
    white = (255, 255)
    # randomly generate a radius size between 5 and 200, generate a random
    # color, and then pick a random point on our canvas where the circle
    # will be drawn
    pt = np.random.randint(236, high=286, size = (2,))
    
    radius = np.random.randint(15, high=min(pt))
    
    # pt = np.random.randint(0, high=400, size = (2,))
    
    # canvas = cv2.GaussianBlur(canvas, (0,0), sigmaX=15, sigmaY=15, borderType = cv2.BORDER_DEFAULT)
    
    canvas = cv2.GaussianBlur(canvas, (0,0), sigmaX=5, sigmaY=5, borderType = cv2.BORDER_DEFAULT)
    #this is circle so why
    cv2.circle(canvas, tuple(pt), radius, white, -1)
    sigma = 25
    points = 100
    canvas = elasticdeform.deform_random_grid(canvas, sigma=sigma, points=points ,order=0 , axis=(0,1))    
    f.write("shape canvas"+str(canvas.shape)+"\n")
    f.write("sigma"+str(sigma)+"\n")
    f.write("points"+str(points)+"\n")

    #already adjust the parameters
    size = radius//2
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size,size))
    canvas = cv2.morphologyEx(canvas, cv2.MORPH_OPEN, kernel)
    canvas = cv2.morphologyEx(canvas, cv2.MORPH_CLOSE, kernel)
    f.write("after close and open shape"+str(canvas.shape)+"\n")  
    # break
    
    label, num = measure.label(canvas, background=0, return_num=True)
    if num!=1:
        continue
    num_png=num_png+1
    print("num_conn num_png", num, num_png)
    if num_png==10000:
        break
    # Show our masterpiece
    # save_path = "./shape_generating/generated_shapes/synthetic_label_%04d.png"%num_png
    # save_path = "./shape_generating/generated_shapes_new/new_synthetic_label_%04d.png"%num_png
    save_path = "./shape_generating/generated_shapes_new_plus_1000/new_synthetic_label_%04d.png"%(num_png+2000)


    cv2.imwrite(save_path, canvas)
    # break
    
f.close()


# generate shapes based on raw shapes


# #generate new shapes(location mostly centered)
# #img_write ./shape_generating/generated_shape_template_based

# import numpy as np
# import cv2
# import elasticdeform
# import random
# from skimage import measure
# random.seed(0)
# f = open('log_template.txt','a')
# num_png = 0

# img_root = "./pix2pixHD/datasets/skin_redis/test_label_raw/ISIC_0000001_segmentation.png"
# canvas = cv2.imread(img_root,-1)
# print(canvas.shape)
# for i in range(0, 1500):

#     # canvas = np.zeros((512, 512), dtype="uint8")
#     # white = (255, 255)
#     # randomly generate a radius size between 5 and 200, generate a random
#     # color, and then pick a random point on our canvas where the circle
#     # will be drawn
#     # pt = np.random.randint(236, high=286, size = (2,))
    
#     # radius = np.random.randint(15, high=min(pt))
    
#     # pt = np.random.randint(0, high=400, size = (2,))
    
#     # canvas = cv2.GaussianBlur(canvas, (0,0), sigmaX=15, sigmaY=15, borderType = cv2.BORDER_DEFAULT)
    
#     # canvas = cv2.GaussianBlur(canvas, (0,0), sigmaX=5, sigmaY=5, borderType = cv2.BORDER_DEFAULT)
#     #this is circle so why
#     # cv2.circle(canvas, tuple(pt), radius, white, -1)
#     sigma = 25
#     points = 100
#     # canvas = elasticdeform.deform_random_grid(canvas, sigma=sigma, points=points ,order=0 , axis=(0,1))    
#     f.write("shape canvas"+str(canvas.shape)+"\n")
#     f.write("sigma"+str(sigma)+"\n")
#     f.write("points"+str(points)+"\n")
#     print("shape canvas"+str(canvas.shape)+"\n")
#     print("sigma"+str(sigma)+"\n")
#     print("points"+str(points)+"\n")

#     # size = radius//2
#     size=20
#     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size,size))
#     canvas = cv2.morphologyEx(canvas, cv2.MORPH_OPEN, kernel)
#     canvas = cv2.morphologyEx(canvas, cv2.MORPH_CLOSE, kernel)
#     f.write("after close and open shape"+str(canvas.shape)+"\n") 
#     print("after close and open shape"+str(canvas.shape)+"\n") 
#     # break
    
#     label, num = measure.label(canvas, background=0, return_num=True)
#     # if num!=1:
#     #     continue
#     num_png=num_png+1
#     print("num_conn num_png", num, num_png)
#     if num_png==1000:
#         break
#     # Show our masterpiece
#     # save_path = "./shape_generating/generated_shapes/synthetic_label_%04d.png"%num_png
#     # save_path = "./shape_generating/generated_shapes_new/new_synthetic_label_%04d.png"%num_png
#     save_path = "./shape_generating/generated_shape_template_based/new_synthetic_label_%04d.png"%num_png
#     cv2.imwrite(save_path, canvas)
#     break
    
# f.close()



