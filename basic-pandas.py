
# coding: utf-8



get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# # Pandas
# - what is data frame?
# - creation of data frame
# - reading csvs
# - data manipulation (query, create new column, conditional columns, joins)
# - chaining

# ## What is dataframe?
# - a combination of series
# - what is series?
#     - it is a one dimensional structure



## example of a series
example_series = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
example_series




example_series = pd.Series([7, 'Singapore', 3.14, -1789710578, 'Happy Saturday!'],
              index=['A', 'Z', 'C', 'Y', 'E'])
example_series




print(example_series[['A']])

print(example_series[['A','B','C']])


# ## Creation of dataframe
# - list
# - dictionary
# - csv
# - excel

# ### List



list_example = [['2010','2011','2012']]

print(pd.DataFrame(['2010','2011','2012']))
print()

pd.DataFrame(list_example,columns=['A','G','Z'])




raw_data = [('Jones LLC', 150, 200, 50),
         ('Alpha Co', 200, 210, 90),
         ('Blue Inc', 140, 215, 95)]
column_name = ['account', 'Jan', 'Feb', 'Mar']
df_list = pd.DataFrame(sales, columns=labels)
df_list


# ### Dictionary



data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
football


# ### CSV



raw_data = pd.read_csv("../car-hire-projects/data/prefunnel_sessions.csv").drop(['Unnamed: 0'],1)

raw_data.head()


# ### Excel



ncaa = pd.read_excel('Book1.xlsx', 'Sheet1')
ncaa.head(2)


# ## Data Manipulation
# - general stuff
# - query
# - column creation
# - group by, aggregate functions
# - conditional columns and values
# - joins, append and concatentate
# - pivot table

# ### General Stuff



print(ncaa.head())
print(ncaa.head(2))
print(ncaa.tail())
print(ncaa.tail(2))
print(ncaa.describe())
print(ncaa.dtypes)
print(ncaa[3:5])
print(ncaa.iloc[:,1:3])

print(raw_data.iloc[[0,3,4,6], [0,2,4]])


raw_data[['date','medium_grouped','sessions','par']].head()


# ### Query
# - selection of rows and etc



print(raw_data[raw_data.sessions == 1].head(3))




print(raw_data[(raw_data.sessions == 1) & (raw_data.medium_grouped == 'organic')].head(3))




### a much simpler way of doing
raw_data.query("sessions == 1 & medium_grouped == 'organic'").head(3)


# ### Column creation



def multiplier(df,column1,column2):
    value = df[column1] * df[column2]
    return value




raw_data['transformed_variable'] = multiplier(raw_data,'sessions','sessions')




raw_data.head(2)


# ### Group By



raw_data.head()




(
    raw_data
    .groupby(['medium_grouped'])
    .sum()
    ['sessions']
    .reset_index()
    .head()
)




(
    raw_data
    .groupby(['medium_grouped'])
    .agg({"sessions":"sum","funnel_sessions":"sum"})
    .reset_index()
    .head()
)


# ### Conditional columns and values



raw_data.head()




raw_data['which_page_altered'] = (
    np.where(raw_data.medium_grouped == 'organic',"special_homepage",
             np.where(raw_data.which_device == 'mobile_web',"not_special_homepage",raw_data.medium_grouped))




raw_data.head(10)


# ### Join, append and concatenate



data = pd.read_csv("../multi-touch-attribution-garage-markov-variant/data/simulated_scenarios/csv/dataset_top_25_channels__current_state.csv")




data.head(10)




df_revenue_user = (
    data
    .query("event_type == 'conversion'")
    .groupby(['user_id'])
    .agg({"value":"sum"})
    .reset_index()
    .rename(columns={"value":"revenue","user_id":"userid"})
)

df_revenue_user.head()




combined_df = (
    data
    .query("event_type == 'touchpoint'")
    .groupby(['user_id'])
    .agg({"value":"count"})
    .reset_index()
    .rename(columns={"value":"touchpoints"})
    .merge(df_revenue_user, how='left',left_on=['user_id'],right_on=['userid'])
    .fillna(0)
    .drop(['userid'],1)
)

combined_df.head()

