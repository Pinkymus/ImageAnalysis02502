## Exercise 1
# This is done using sin rules lol

## Exercise 2


def camera_b_distance(f, g):
    """
    camera_b_distance returns the distance (b) where the CCD should be placed
    when the object distance (g) and the focal length (f) are given
    :param f: Focal length
    :param g: Object distance
    :return: b, the distance where the CCD should be placed
    """
    return -(g * f) / (f - g)  # Simplified by maple


""""
>>> camera_b_distance(0.015,0.1)
0.01764705882352941
>>> camera_b_distance(0.015,1)
0.015228426395939085
>>> camera_b_distance(0.015,5)
0.015045135406218654
>>> camera_b_distance(0.015,15)
0.015015015015015015
>>> 
"""  # When d increases b approaches f

## Exersice 3

# - 1 
"""
    >>> camera_b_distance(0.005,1.8)
    0.005013927576601671 #(meter)
"""
# - 2  
    # 0.0036
# - 3 
    # 0.01 mm 
# - 4
    # 360 px
# - 5
    # 65 degress fov
# - 6
    # 51 degress fov
