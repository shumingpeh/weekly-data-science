
# coding: utf-8



get_ipython().magic('matplotlib inline')
import pandas as pd
import sqlalchemy as sa
import numpy as np
import string
import yaml
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

offline.init_notebook_mode()

#ignore warnings for strings
warnings.filterwarnings("ignore")


# ## Read dataset



raw_data = pd.read_csv("../car-hire-projects/data/prefunnel_sessions.csv").drop(['Unnamed: 0'],1)
raw_data.head()




# total sessions, simple plotting
total_sessions = (
    raw_data
    .groupby(['date'])
    .agg({"sessions":"sum","funnel_sessions":"sum"})
    .reset_index()
)

total_sessions.head()




plt.plot(total_sessions.date,total_sessions.sessions)
plt.bar(total_sessions.date,total_sessions.funnel_sessions)
plt.show()


# ## setting defaults
# - size
# - ticks
# - title



plt.figure(figsize=(20,10))

plt.plot(total_sessions.date,total_sessions.sessions)
plt.plot(total_sessions.date,total_sessions.funnel_sessions)

plt.ylim(0,45000)
plt.legend(loc='upper left', frameon=False)
plt.xlabel("date")
plt.ylabel("sessions type")
plt.title("Prefunnel and funnel sessions")

plt.yticks(np.linspace(0,45000,11,endpoint=True))



plt.show()


# ## Having other plots
# - scatter
# - bar



plt.figure(figsize=(15,5))

plt.scatter(total_sessions.date,total_sessions.sessions)
# plt.plot(total_sessions.date,total_sessions.funnel_sessions)

# plt.ylim(0,45000)
# plt.legend(loc='bottom left', frameon=False)
plt.xlabel("date")
plt.ylabel("sessions type")
plt.title("Prefunnel and funnel sessions")

# plt.yticks(np.linspace(0,45000,11,endpoint=True))

plt.show()




plt.figure(figsize=(15,5))

plt.bar(total_sessions.date,total_sessions.sessions)
# plt.plot(total_sessions.date,total_sessions.funnel_sessions)

# plt.ylim(0,45000)
# plt.legend(loc='bottom left', frameon=False)
plt.xlabel("date")
plt.ylabel("sessions type")
plt.title("Prefunnel and funnel sessions")

# plt.yticks(np.linspace(0,45000,11,endpoint=True))

plt.show()


# ## Subplots



plt.figure(figsize=(15,8))

plt.subplot(1, 3, 1)
plt.barh(total_sessions.date, total_sessions.sessions)
plt.title("example")

plt.subplot(1, 3, 2)
plt.barh(total_sessions.date, total_sessions.sessions)
plt.title("example")
plt.xticks(rotation=45)

plt.subplot(1, 3, 3)
plt.barh(total_sessions.date, total_sessions.sessions)
plt.title("example")
plt.xticks(rotation=45)


plt.tight_layout()




# df_ = (
#     df.loc[df['event_index'] <= 20]
#     .groupby('event_index')
#     .agg(np.sum)
# )


fig, [ax1, ax2] = plt.subplots(2, figsize=(5, 10))

(total_sessions.funnel_sessions / total_sessions.sessions.sum()).plot(ax=ax1)
(total_sessions.funnel_sessions / total_sessions.sessions.sum()).plot(logy=True, ax=ax2)

ax1.set_title('Proportion of sessions at varying length of user timeline')
ax1.set_ylabel('Proportion of sessions')
ax1.set_xlabel('Touchpoint index on user timeline')
ax2.set_title('Proportion of sessions at varying length of user timeline (log scale)')

ax2.set_xlabel('Touchpoint index on user timeline (log)')
ax2.set_ylabel('Proportion of sessions');


# ## Using functions to plot out something




def get_redirect_distribution(channelname='criteo-retargeting'):
    # function that looks at the proportion of sessions, conversions, and conversion rate for a specific channel.
    subset = df.loc[df.channel == channelname]
    fig, [ax1, ax2, ax3] = plt.subplots(3, figsize=(10,22))
    
    subset = subset.loc[subset.event_index < 15].reset_index()
    (
        subset.sessions / subset.sessions.sum()
    ).plot(kind='bar', title='distribution of sessions {}'.format(channelname), ax=ax1)
    (
        subset.conversions / subset.conversions.sum()
    ).plot(kind='bar', title='distribution of conversions {}'.format(channelname), ax=ax2)
    
    (
        subset.conversions / subset.sessions
    ).plot(kind='bar', title='conversion rate {}'.format(channelname), ax=ax3)
    ax3.legend(loc='best')
    return subset




first="ghi"
second="yuyu"
f'abc {first} abc {second} abc'


# ## ggplot



# ggplot(genericdf.reset_index(), aes(x='whichdate', weight = 'retentionrate',fill='whichdate')) + geom_bar(stat='identity') + ggtitle("Overall Retention, main sources")




rawdata = (
    pd.read_csv("../RGT-exploratory-data-analysis/data/peak_hour_of_day.csv")
    .pipe(lambda x:x.assign(category=np.where(
        x.year == 2016, 'first', np.where(x.year == 2017, 'second', 'third'))
    )))




rawdata.head()




g = ggplot(rawdata.query("country == 'HK'"), aes(x='hour',y='num_users',color='category')) +geom_line() + facet_wrap("month") + theme(plot_margin = dict(right = 10, top=3))
g




ggplot(rawdata.query("country == 'HK'"), aes(x='hour', weight = 'num_users',fill='category')) +geom_bar(stat='identity') + facet_wrap('month')

