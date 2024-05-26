import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse_f
import glob

# Define the paths to the directories containing the images
dir1 = './pix2pixHD/datasets/skin_redis/test_img'
# dir2 = '/mnt/petrelfs/dushiyi/diffusion-pytorch/ControlNet/image_log/val_pix_100'
dir2 = './pix2pixHD/results/label2skin_redis/test_430/images'

# Initialize lists to store the MSE, PSNR, and SSIM values
mse_list = []
psnr_list = []
ssim_list = []
orin = sorted(glob.glob(os.path.join(dir1,"*.png")))[900:]
# gene = sorted(glob.glob(os.path.join(dir2,"sample*.png")))
gene = sorted(glob.glob(os.path.join(dir2,"ISIC*image.jpg")))[900:]
print("len 1",len(orin))
print("len 2",len(gene))
# imgs_1= sorted(os.listdir(dir1))
# imgs_2 = sorted(os.listdir(dir2))
# Loop through the images in the directories
for i in range(len(orin)):
    img1 = cv2.imread(orin[i])
    img2 = cv2.imread(gene[i])
    img2 = cv2.resize(img2,(512,512))
    img2 = img2[32:480,32:480]

    img1 = cv2.resize(img1,(512,512))
    img1 = img1[32:480,32:480]
    cv2.imwrite("./pix2pixHD/results/label2skin_redis/test_430/image_resize/_%d.png"%i, img2)
    # # Load the first image
    # img1 = cv2.imread(os.path.join(dir1, img1_name))
    
    # # Load the corresponding image from the second directory
    # img2_name = img1_name.replace('_1.', '_2.') # assuming the two directories have matching filenames
    # img2 = cv2.imread(os.path.join(dir2, img2_name))
    
    # Calculate the MSE between the two images
    mse = np.mean((img1 - img2) ** 2)
    # mse = mse_f(img1,img2)

    print("mse",mse)
    mse_list.append(mse)
    
    # Calculate the PSNR between the two images
    psnr = cv2.PSNR(img1, img2)
    psnr_list.append(psnr)
    
    # Calculate the SSIM between the two images
    ssim_val = ssim(img1, img2, multichannel=True)
    ssim_list.append(ssim_val)

# Calculate the average MSE, PSNR, and SSIM over all images
avg_mse = np.mean(mse_list)
avg_psnr = np.mean(psnr_list)
avg_ssim = np.mean(ssim_list)

# Print the results
print(f"Average MSE: {avg_mse:.2f}")
print(f"Average PSNR: {avg_psnr:.2f}")
print(f"Average SSIM: {avg_ssim:.2f}")