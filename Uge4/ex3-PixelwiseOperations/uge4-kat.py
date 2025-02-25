from skimage.util import img_as_float
from skimage.util import img_as_ubyte
from skimage import color, io, measure, img_as_ubyte
import cv2

import matplotlib.pyplot as plt #importing matplotlib
import numpy as np

# Exercise 1: 
# Start by reading the image and inspect the histogram. 
# Is it a bimodal histogram? 
#   Hmm well it has some peaks at the end, and a smaller one at the beginning
# Do you think it will be possible to segment it so only the bones are visible?
#   probably

img = plt.imread('Uge4/ex3-PixelwiseOperations/data/vertebra.png') #reads image data

#plt.hist(img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k') #calculating histogram
#plt.title('Image histogram')
#io.show()



# Exercise 2: 
# Compute the minimum and maximum values of the image. 
# Is the full scale of the gray-scale spectrum used or can we enhance the appearance of the image?
#   NO
print("Minimum float value:",img[..., 0].min())
print("Maximum float value:",img[..., 0].max(), "\n")


# Exercise 3:
# In scale 255
# Read the image vertebra.png and compute and show the minumum and maximum values.
print("Min pixel value:",img_as_ubyte(img).min())
print("Max pixel value:",img_as_ubyte(img).max())



# Exercise 4: 
# Use img_as_ubyte on the float image you computed in the previous exercise. 
# Compute the Compute the minimum and maximum values of this image. 
# Are they as expected?

# Exercise 5: Implement a Python function called histogram_stretch. It can, for example, follow this example:
def histogram_stretch(img_in):
    """
    Stretches the histogram of an image 
    :param img_in: Input image
    :return: Image, where the histogram is stretched so the min values is 0 and the maximum value 255
    """
    # img_as_float will divide all pixel values with 255.0
    img_float = img_as_float(img_in)
    min_val = img_float.min()
    max_val = img_float.max()
    min_desired = 0.0
    max_desired = 1.0
	
    diff = max_val - min_val
    # Do something here
    # shift and scale, shift by minimum value scale by the gradient
    img_out = []
    for row in img_float:
        new_row = []
        for pixle in row:
            new_row.append((1.0/diff)*(pixle - min_val))
        img_out.append(new_row)
    # img_as_ubyte will multiply all pixel values with 255.0 before converting to unsigned byte
    return img_as_ubyte(img_out)

img_strech = histogram_stretch(img)


print("New min pixel value:",(img_strech).min())
print("New max pixel value:",(img_strech).max())

#plt.hist(img_strech.ravel(), bins=256) #calculating histogram
#plt.title('Image histogram')
#io.show()

def show_in_moved_window(win_name, img):
    """
    Show an image in a window, where the position of the window can be given
    """
    cv2.namedWindow(win_name)
    cv2.imshow(win_name, img)


#Exercise 6: Test your histogram_stretch on the vertebra.png image. 
# Show the image before and after the histogram stretching. 
# What changes do you notice in the image? 
# Are the important structures more visible?

'''
stop = False
print("Press 'q' to end the show")
while not stop:
    show_in_moved_window("Before", img)
    show_in_moved_window("After", img_strech)

    if cv2.waitKey(1) == ord('q'):
        stop = True
'''

# Exercise 7: Implement a function, gamma_map(img, gamma), that:

# Converts the input image to float
# Do the gamma mapping on the pixel values
# Returns the resulting image as an unsigned byte image.

def gamma_map(img, gamma):
    img_float = img_as_float(img)

    img_out = []

    for row in img_float:
        new_row = []
        for pixle in row:
            new_row.append(np.power(pixle, gamma))
        img_out.append(new_row)
    # img_as_ubyte will multiply all pixel values with 255.0 before converting to unsigned byte
    return img_as_ubyte(img_out)


img_gamma = img_as_float(gamma_map(img, 5))

'''
stop = False
print("Press 'q' to end the show")

while not stop:
    show_in_moved_window("Gamma 5", img_gamma)
    show_in_moved_window("Gamma 20", img_as_float(gamma_map(img, 20)))

    if cv2.waitKey(1) == ord('q'):
        stop = True
'''


# Exercise 9: 
# Implement a function, threshold_image :

def threshold_image(img_in, thres):
    """
    Apply a threshold in an image and return the resulting image
    :param img_in: Input image
    :param thres: The treshold value in the range [0, 255]
    :return: Resulting image (unsigned byte) where background is 0 and foreground is 255
    """
    img_out = []
    for row in img_in:
        new_row = []
        for pixle in row:
            new_row.append((pixle if pixle > thres else 0))
        img_out.append(new_row)

    return img_out

img_thres = threshold_image(img_strech, 100)



plt.imshow(img_thres)
io.show()