from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom

# Directory containing data and images
in_dir = "ex1-IntroductionToImageAnalysis/data/"

# X-ray image
im_name = "metacarpals.png"

# Read the image.
# Here the directory and the image name is concatenated
# by "+" to give the full path to the image.
im_org = io.imread(in_dir + im_name)

#Exercise 2
print(im_org.shape)

#Exercise 3
print(im_org.dtype)

#Exercise 4
# io.imshow(im_org)
# plt.title('Metacarpal image')
# io.show()

#Exercise 5 & 6
# io.imshow(im_org, cmap="cubehelix")
# plt.title('Metacarpal image (with colormap)')
# io.show()

#Exercise 7
# max = np.max(im_org)
# min = np.min(im_org)

# print("Highest pixel value, " + max.astype(str))
# print("Lowest pixel value, " + min.astype(str))

# io.imshow(im_org, vmin=min, vmax=max)
# plt.title('Metacarpal image (with gray level scaling)')
# io.show()

#Exercise 8
plt.hist(im_org.ravel(), bins=256)
plt.title('Image histogram')
io.show()