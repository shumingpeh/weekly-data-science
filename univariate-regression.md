

```python
%matplotlib inline
import pandas as pd
import sqlalchemy as sa
import numpy as np
import string
import sqlalchemy as sa
import statsmodels.stats.api as sms
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
import plotly 
import plotly.offline as offline
import datetime
from scipy.stats.stats import spearmanr
from plotly import tools
from ggplot import *
import statsmodels.formula.api as sm
import sklearn
import scipy.stats as stats
from sklearn import datasets, linear_model
from sklearn.cross_validation import KFold
from sklearn.linear_model import LinearRegression
import sklearn.preprocessing as pp

warnings.filterwarnings("ignore")
```


```python
rawdata = pd.read_csv("data/weight-height.csv")
```


```python
firstpassresult = sm.ols(formula="Height ~ Weight", data=rawdata).fit()
print(firstpassresult.summary())

```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                 Height   R-squared:                       0.855
    Model:                            OLS   Adj. R-squared:                  0.855
    Method:                 Least Squares   F-statistic:                 5.904e+04
    Date:                Fri, 31 Aug 2018   Prob (F-statistic):               0.00
    Time:                        21:49:31   Log-Likelihood:                -18002.
    No. Observations:               10000   AIC:                         3.601e+04
    Df Residuals:                    9998   BIC:                         3.602e+04
    Df Model:                           1                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept     48.4779      0.075    645.773      0.000      48.331      48.625
    Weight         0.1108      0.000    242.975      0.000       0.110       0.112
    ==============================================================================
    Omnibus:                        4.617   Durbin-Watson:                   1.992
    Prob(Omnibus):                  0.099   Jarque-Bera (JB):                4.615
    Skew:                          -0.053   Prob(JB):                       0.0995
    Kurtosis:                       3.000   Cond. No.                         844.
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



```python
firstpassresult.mse_total
```




    14.803472640312716




```python
regr = linear_model.LinearRegression()
```


```python
x_values = rawdata.Weight.values
y_values = rawdata.Height.values
```


```python
regr.fit([x_values],[y_values])
```




    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)


