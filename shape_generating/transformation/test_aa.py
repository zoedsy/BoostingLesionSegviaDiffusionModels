import albumentations as A
import cv2
transform = A.Compose([
    A.RandomCrop(width=512, height=512),
    A.Rotate(p=1),
    A.ElasticTransform(p=1)
])

# Read an image with OpenCV and convert it to the RGB colorspace
image = cv2.imread("Canvas.png")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Augment an image
transformed = transform(image=image)
transformed_image = transformed["image"]

# about the generated image shape
print(transformed_image.shape)


# about how to change after doing this
cv2.imwrite("Canvas_trans.png",transformed_image)


