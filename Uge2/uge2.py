import numpy as np

in_dir = "ex1b-PCA/data/"

txt_name = "irisdata.txt"

#Exercise 1
iris_data = np.loadtxt(in_dir + txt_name, comments="%")
# x is a matrix with 50 rows and 4 columns
x = iris_data[0:50, 0:4]

n_feat = x.shape[1]
n_obs = x.shape[0]
print(f"Number of features: {n_feat} and number of observations: {n_obs}")


sep_l = x[:, 0]
sep_w = x[:, 1]
pet_l = x[:, 2]
pet_w = x[:, 3]

# Use ddof = 1 to make an unbiased estimate
print(f"Sepal Length variance: {sep_l.var(ddof=1)}")
print(f"Sepal Width variance: {sep_w.var(ddof=1)}")
print(f"Petal Length variance: {pet_l.var(ddof=1)}")
print(f"Petal Width variance: {pet_w.var(ddof=1)}")


print(f"Måkse variance: {np.var(x)}")


# Exercise 3
print("########## Excercise 3 ##########")
#print(np.cov(x))

temp = 0

for j in range(len(sep_l)):
    temp = temp + (sep_l[j]*sep_w[j])


# print(f"The temp variable: {temp}")
temp = 1/(n_obs-1)*temp

print("The covariance between sepal length and width:")
print(np.sqrt(temp))
print()


temp = 0
for j in range(len(sep_l)):
    temp = temp + (sep_l[j]*pet_l[j])
temp = 1/(n_obs-1)*temp
print("The covariance between sepal length and petal length:")
print(np.sqrt(temp))
print()

# Exercise 4
print("########## Excercise 4 ##########")

import seaborn
import pandas
import matplotlib.pyplot as plt

plt.figure() # Added this to make sure that the figure appear
# Transform the data into a Pandas dataframe
d = pandas.DataFrame(x, columns=['Sepal length', 'Sepal width',
							 'Petal length', 'Petal width'])
seaborn.pairplot(d)
plt.show()

temp = (-0.2)*(-0.2) + 0.3*0.3

print(np.sqrt(temp))
