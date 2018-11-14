

```python
import pandas as pd
import numpy as np
```

## Example 1:
We have a dataset that has about 30 features, we will want to reduce the number of features being used, so that we can train the dataset with lesser complexity


```python
raw_data = pd.read_csv("../data/lesson7/features.csv")
```


```python
print("number of features in table: " + str(len(raw_data.dtypes)-2))
raw_data.head().transpose()
```

    number of features in table: 32





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>total_score</th>
      <td>0.016179</td>
      <td>0.060323</td>
      <td>0.109066</td>
      <td>0.152926</td>
      <td>0.023338</td>
    </tr>
    <tr>
      <th>total_opponent_score</th>
      <td>0.022804</td>
      <td>0.082161</td>
      <td>0.142904</td>
      <td>0.196478</td>
      <td>0.021182</td>
    </tr>
    <tr>
      <th>total_rebounds</th>
      <td>0.014417</td>
      <td>0.054206</td>
      <td>0.096439</td>
      <td>0.135208</td>
      <td>0.014061</td>
    </tr>
    <tr>
      <th>total_off_rebounds</th>
      <td>0.010464</td>
      <td>0.044034</td>
      <td>0.076152</td>
      <td>0.103619</td>
      <td>0.003052</td>
    </tr>
    <tr>
      <th>total_def_rebounds</th>
      <td>0.016552</td>
      <td>0.059696</td>
      <td>0.107389</td>
      <td>0.152259</td>
      <td>0.020003</td>
    </tr>
    <tr>
      <th>total_blocks</th>
      <td>0.003550</td>
      <td>0.013314</td>
      <td>0.032840</td>
      <td>0.053254</td>
      <td>0.009172</td>
    </tr>
    <tr>
      <th>total_assists</th>
      <td>0.011125</td>
      <td>0.051270</td>
      <td>0.093349</td>
      <td>0.134462</td>
      <td>0.029746</td>
    </tr>
    <tr>
      <th>total_steals</th>
      <td>0.014599</td>
      <td>0.054988</td>
      <td>0.099270</td>
      <td>0.141849</td>
      <td>0.025791</td>
    </tr>
    <tr>
      <th>total_turnover</th>
      <td>0.020070</td>
      <td>0.070105</td>
      <td>0.120557</td>
      <td>0.171010</td>
      <td>0.020767</td>
    </tr>
    <tr>
      <th>total_personalfoul</th>
      <td>0.027708</td>
      <td>0.088496</td>
      <td>0.152128</td>
      <td>0.210493</td>
      <td>0.035293</td>
    </tr>
    <tr>
      <th>total_assist_per_fgm</th>
      <td>0.273657</td>
      <td>0.386835</td>
      <td>0.403154</td>
      <td>0.422999</td>
      <td>0.863359</td>
    </tr>
    <tr>
      <th>total_assist_turnover_ratio</th>
      <td>0.184679</td>
      <td>0.311397</td>
      <td>0.362014</td>
      <td>0.381143</td>
      <td>0.618631</td>
    </tr>
    <tr>
      <th>expectation_per_game</th>
      <td>0.223744</td>
      <td>0.289324</td>
      <td>0.346074</td>
      <td>0.381699</td>
      <td>0.614475</td>
    </tr>
    <tr>
      <th>avg_lose_score_by</th>
      <td>0.442812</td>
      <td>0.419435</td>
      <td>0.480444</td>
      <td>0.540254</td>
      <td>0.706714</td>
    </tr>
    <tr>
      <th>avg_win_score_by</th>
      <td>0.023869</td>
      <td>0.344779</td>
      <td>0.281128</td>
      <td>0.213940</td>
      <td>0.600712</td>
    </tr>
    <tr>
      <th>num_season</th>
      <td>0.026087</td>
      <td>0.056522</td>
      <td>0.086957</td>
      <td>0.117391</td>
      <td>0.086957</td>
    </tr>
    <tr>
      <th>is_playoff</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>is_champion</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Season</th>
      <td>2014.000000</td>
      <td>2015.000000</td>
      <td>2016.000000</td>
      <td>2017.000000</td>
      <td>2003.000000</td>
    </tr>
    <tr>
      <th>TeamID</th>
      <td>1101.000000</td>
      <td>1101.000000</td>
      <td>1101.000000</td>
      <td>1101.000000</td>
      <td>1102.000000</td>
    </tr>
    <tr>
      <th>win_rate</th>
      <td>0.095238</td>
      <td>0.183673</td>
      <td>0.236842</td>
      <td>0.267327</td>
      <td>0.428571</td>
    </tr>
    <tr>
      <th>fgp</th>
      <td>0.405508</td>
      <td>0.405128</td>
      <td>0.418441</td>
      <td>0.428437</td>
      <td>0.481149</td>
    </tr>
    <tr>
      <th>fg3p</th>
      <td>0.373333</td>
      <td>0.376096</td>
      <td>0.371569</td>
      <td>0.371444</td>
      <td>0.375643</td>
    </tr>
    <tr>
      <th>total_off_rebounds_percent</th>
      <td>0.282353</td>
      <td>0.289971</td>
      <td>0.281179</td>
      <td>0.272758</td>
      <td>0.198980</td>
    </tr>
    <tr>
      <th>total_def_rebounds_percent</th>
      <td>0.717647</td>
      <td>0.710029</td>
      <td>0.718821</td>
      <td>0.727242</td>
      <td>0.801020</td>
    </tr>
    <tr>
      <th>total_rebound_possession_percent</th>
      <td>0.268371</td>
      <td>0.264589</td>
      <td>0.267126</td>
      <td>0.265856</td>
      <td>0.202422</td>
    </tr>
    <tr>
      <th>total_rebound_possessiongain_percent</th>
      <td>0.773551</td>
      <td>0.766275</td>
      <td>0.788950</td>
      <td>0.790110</td>
      <td>0.726852</td>
    </tr>
    <tr>
      <th>total_block_opp_FGA_percent</th>
      <td>0.027629</td>
      <td>0.025137</td>
      <td>0.032541</td>
      <td>0.037287</td>
      <td>0.042088</td>
    </tr>
    <tr>
      <th>win_rate_away</th>
      <td>0.000000</td>
      <td>0.083333</td>
      <td>0.157895</td>
      <td>0.250000</td>
      <td>0.428571</td>
    </tr>
    <tr>
      <th>win_rate_home</th>
      <td>0.125000</td>
      <td>0.176471</td>
      <td>0.230769</td>
      <td>0.250000</td>
      <td>0.473684</td>
    </tr>
    <tr>
      <th>win_rate_neutral</th>
      <td>0.000000</td>
      <td>0.666667</td>
      <td>0.600000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>win_rate_post</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>win_rate_regular</th>
      <td>0.095238</td>
      <td>0.183673</td>
      <td>0.236842</td>
      <td>0.267327</td>
      <td>0.428571</td>
    </tr>
    <tr>
      <th>win_rate_overall</th>
      <td>0.095238</td>
      <td>0.183673</td>
      <td>0.236842</td>
      <td>0.267327</td>
      <td>0.428571</td>
    </tr>
  </tbody>
</table>
</div>



#### Remove away columns that are not required in training of model


```python
rawdata = (
    raw_data
    .drop(['Season','TeamID'],1)
)
```

### Before applying PCA to the dataset, we will have to remove correlated features
- why?
    - In presence of correlated variables, the variance explained by a particular component gets inflated.
    - We have more unnecessary eigen values, which increases the variance incorrectly


```python
corr = rawdata.corr()
```

### Remove features that have correlation than 0.7


```python
features_table = (
    rawdata
    .drop(['total_score','total_opponent_score','total_rebounds','total_blocks','total_assist_turnover_ratio','expectation_per_game',
           'win_rate','fg3p','win_rate_overall','total_off_rebounds_percent','total_def_rebounds_percent','total_rebound_possession_percent','total_rebound_possessiongain_percent'
          ],1)
    .fillna(0)
)
```


```python
print("Number of features left: " + str(len(features_table.dtypes)))
```

    Number of features left: 19


### Apply PCA to `features_table`


```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from sklearn.decomposition import PCA
```


```python
pca = PCA()#PCA(n_components = 19) # number of features
pca.fit(features_table) # fit the features table into PCA
```




    PCA(copy=True, iterated_power='auto', n_components=None, random_state=None,
      svd_solver='auto', tol=0.0, whiten=False)




```python
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance')
```




    Text(0,0.5,'cumulative explained variance')




![png](PCA%20Example_files/PCA%20Example_14_1.png)



```python
np.cumsum(np.round(pca.explained_variance_ratio_, decimals=5)*100)
```




    array([ 53.87 ,  75.75 ,  83.114,  87.838,  91.951,  94.629,  96.187,
            97.186,  97.912,  98.579,  98.959,  99.237,  99.497,  99.675,
            99.829,  99.913,  99.963,  99.984, 100.   ])



### Assuming we would like to cut off at 95% variance
- 7 variables retained


```python
pca = PCA(n_components=7)
pca.fit(features_table)
```




    PCA(copy=True, iterated_power='auto', n_components=7, random_state=None,
      svd_solver='auto', tol=0.0, whiten=False)



### Get back original data from the 7 features selected


```python
post_pca_array = pca.fit_transform(features_table)
X_new = pca.inverse_transform(post_pca_array)
```


```python
X_new.shape
```




    (5172, 19)



#### `post_pca_array` will be the dimension reduction matrix that will be used in classification or regression moving forward
- notice how PCA doesnt drop any of the columns but instead of 19 columns its being compressed to 7 column (or components)
