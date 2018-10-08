
# coding: utf-8



get_ipython().magic('matplotlib inline')
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




rawdata = pd.read_csv("data/weight-height.csv")




firstpassresult = sm.ols(formula="Height ~ Weight", data=rawdata).fit()
print(firstpassresult.summary())




firstpassresult.mse_total




regr = linear_model.LinearRegression()




x_values = rawdata.Weight.values
y_values = rawdata.Height.values




regr.fit([x_values],[y_values])

