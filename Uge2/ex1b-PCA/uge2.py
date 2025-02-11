import numpy as np

in_dir = "ex1b-PCA/data/"

txt_name = "iris_data.txt"

#Exercise 1
iris_data = np.loadtxt(in_dir + txt_name, comments="%")
# x is a matrix with 50 rows and 4 columns
x = iris_data[0:50, 0:4]