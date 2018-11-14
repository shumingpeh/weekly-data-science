
# coding: utf-8



import pandas as pd
import numpy as np


# ## Example 1:
# We have a dataset that has about 30 features, we will want to reduce the number of features being used, so that we can train the dataset with lesser complexity



raw_data = pd.read_csv("../data/lesson7/features.csv")




print("number of features in table: " + str(len(raw_data.dtypes)-2))
raw_data.head().transpose()


# #### Remove away columns that are not required in training of model



rawdata = (
    raw_data
    .drop(['Season','TeamID'],1)
)


# ### Before applying PCA to the dataset, we will have to remove correlated features
# - why?
#     - In presence of correlated variables, the variance explained by a particular component gets inflated.
#     - We have more unnecessary eigen values, which increases the variance incorrectly



corr = rawdata.corr()


# ### Remove features that have correlation than 0.7



features_table = (
    rawdata
    .drop(['total_score','total_opponent_score','total_rebounds','total_blocks','total_assist_turnover_ratio','expectation_per_game',
           'win_rate','fg3p','win_rate_overall','total_off_rebounds_percent','total_def_rebounds_percent','total_rebound_possession_percent','total_rebound_possessiongain_percent'
          ],1)
    .fillna(0)
)




print("Number of features left: " + str(len(features_table.dtypes)))


# ### Apply PCA to `features_table`



get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from sklearn.decomposition import PCA




pca = PCA()#PCA(n_components = 19) # number of features
pca.fit(features_table) # fit the features table into PCA




plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance')




np.cumsum(np.round(pca.explained_variance_ratio_, decimals=5)*100)


# ### Assuming we would like to cut off at 95% variance
# - 7 variables retained



pca = PCA(n_components=7)
pca.fit(features_table)


# ### Get back original data from the 7 features selected



post_pca_array = pca.fit_transform(features_table)
X_new = pca.inverse_transform(post_pca_array)




X_new.shape


# #### `post_pca_array` will be the dimension reduction matrix that will be used in classification or regression moving forward
# - notice how PCA doesnt drop any of the columns but instead of 19 columns its being compressed to 7 column (or components)
