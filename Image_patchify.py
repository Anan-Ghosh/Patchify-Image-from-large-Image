import numpy as np
from matplotlib import pyplot as plt
from patchify import patchify
from PIL import Image
import os
import cv2

folder = input("folder: ")


for img in os.listdir(folder):
    file = f"{folder}\\{img}"
    print(file)
    im = Image.open(file)
    im = im.resize((height, width), Image.ANTIALIAS) # resize the image shape
    im.convert("L").save(file) #convert into grayscale
    im = np.asarray(Image.open(file))
    patches_img = patchify(im, (patchify_size, patchify_size), step=patchify_size) #patchify the image

    for i in range(patches_img.shape[0]):
        for j in range(patches_img.shape[1]):
            single_patches_img = patches_img[i, j, :, :]
            single_patches_img = Image.fromarray(single_patches_img)
            single_patches_img.save("Path_Name"+"_"+str(i)+str(j)+str(img))
