#%%
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()

# %%
X = pd.DataFrame(iris.data)
y = pd.Series(iris.target)

X.columns = iris.feature_names

df = pd.concat([X,y],axis=1)
# %%
