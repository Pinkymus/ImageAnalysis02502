from skimage import io,util,exposure
from skimage.util import img_as_float
from skimage.util import img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np

from skimage.filters import threshold_otsu

im_org = io.imread("data/vertebra.png")

min_val = im_org.min()
max_val = im_org.max()
print("Min:",min_val,"Max:",max_val)

img_float = img_as_float(im_org)
min_val = img_float.min()
max_val = img_float.max()
print("Min:",min_val,"Max:",max_val)

plt.hist(im_org.ravel(),bins=256)
plt.title("Histogram of vertebra")
plt.show()


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


    img_out = np.vectorize(lambda x: (x - min_val)*(max_desired - min_desired) / (max_val - min_val) + min_desired)(img_float)
    # img_as_ubyte will multiply all pixel values with 255.0 before converting to unsigned byte
    return img_as_ubyte(img_out)

io.imshow(histogram_stretch(im_org))
io.show()


def gamma_map(img, gamma):
    img_float = img_as_float(img)

    return img_as_ubyte(np.vectorize(lambda x: np.power(x,gamma))(img_float))

io.imshow(gamma_map(im_org,2.0))
io.show()


def threshold_image(img_in, thres):

    apply = np.vectorize(lambda x: 255 if x > thres else 0)

    return apply(img_in)

io.imshow(threshold_image(im_org,140))
io.show()


thres = threshold_otsu(im_org)

io.imshow(threshold_image(im_org,thres))
io.show()