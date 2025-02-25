import numpy as np
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

sep_l = x[:, 0]
sep_w = x[:, 1]
pet_l = x[:, 2]
pet_w = x[:, 3]

# Use ddof = 1 to make an unbiased estimate
var_sep_l = sep_l.var(ddof=1)
var_sep_w = sep_w.var(ddof=1)
var_pet_l = pet_l.var(ddof=1)
var_pet_w = pet_w.var(ddof=1)
print(var_sep_l,var_sep_w,var_pet_l,var_pet_w)

sum = 0
for i in range(len(sep_l)):
    sum += sep_l[i] * sep_w[i]

sum = sum / (len(sep_l)-1.0)
sep_covar = np.sqrt(sum)
print("sep_covar:",sep_covar)

import seaborn as sns
import pandas as pd

plt.figure() # Added this to make sure that the figure appear
# Transform the data into a Pandas dataframe
d = pd.DataFrame(x, columns=["Sepal length", "Sepal width",
							 "Petal length", "Petal width"])
sns.pairplot(d)
plt.show()

mn = np.mean(x, axis=0)
data = x - mn




print("EXAMPLE:",np.cov(x))