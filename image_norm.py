from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
import numpy as np 

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.6087, 0.6015, 0.5598), (0.1883, 0.1921, 0.2182))
])

image_path = "/../../../Volumes/joeham/logging_camera_down/image_data/left_frame_37090.0.jpg"

img = Image.open(image_path)

img_np = np.array(img)

plt.hist(img_np.ravel(), bins=50, density=True)
plt.xlabel("pixel values")
plt.ylabel("relative frequency")
plt.title("distribution of pixels")
plt.show()


img_tensor = transform(img)
mean, std = img_tensor.mean([1,2]), img_tensor.std([1,2])

print("Mean: " + str(mean))
print("Std: " + str(std))