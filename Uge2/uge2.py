import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


in_dir = "ex1b-PCA/data/"

txt_name = "irisdata.txt"

#Exercise 1
iris_data = np.loadtxt(in_dir + txt_name, comments="%")
# x is a matrix with 50 rows and 4 columns
x = iris_data[0:50, 0:4]

n_feat = x.shape[1]
n_obs = x.shape[0]
print(f"Number of features: {n_feat} and number of observations: {n_obs}")

#Exercise 2
sep_l = x[:, 0]
sep_w = x[:, 1]
pet_l = x[:, 2]
pet_w = x[:, 3]

print(sep_l)
print(sep_w)
print(pet_l)
print(pet_w)

#Exercise 3
var_sep_l = sep_l.var(ddof=1)
var_sep_w = sep_w.var(ddof=1)
var_pet_l = pet_l.var(ddof=1)
var_pet_w = pet_w.var(ddof=1)

cov_sep = np.sqrt(1/(n_obs-1) * np.sum((sep_l) * (sep_w)))
cov_pet = np.sqrt(1/(n_obs-1) * np.sum((pet_l) * (pet_w)))

print(f"Covariance between sepal length and sepal width: {cov_sep}")

#Exercise 4
plt.figure() # Added this to make sure that the figure appear 
#Transform the data into a Pandas dataframe
d = pd.DataFrame(x, columns=["Sepal length", "Sepal width",
							 "Petal length", "Petal width"])
sns.pairplot(d)
plt.show()

#Exercise 5
mn = np.mean(x, axis=0)
data = x - mn

