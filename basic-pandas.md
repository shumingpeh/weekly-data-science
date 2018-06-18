

```python
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

# Pandas
- what is data frame?
- creation of data frame
- reading csvs
- data manipulation (query, create new column, conditional columns, joins)
- chaining

## What is dataframe?
- a combination of series
- what is series?
    - it is a one dimensional structure


```python
## example of a series
example_series = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
example_series
```




    0                7
    1       Heisenberg
    2             3.14
    3      -1789710578
    4    Happy Eating!
    dtype: object




```python
example_series = pd.Series([7, 'Singapore', 3.14, -1789710578, 'Happy Saturday!'],
              index=['A', 'Z', 'C', 'Y', 'E'])
example_series
```




    A                  7
    Z          Singapore
    C               3.14
    Y        -1789710578
    E    Happy Saturday!
    dtype: object




```python
print(example_series[['A']])

print(example_series[['A','B','C']])
```

    A    7
    dtype: object
    A       7
    B     NaN
    C    3.14
    dtype: object


## Creation of dataframe
- list
- dictionary
- csv
- excel

### List


```python
list_example = [['2010','2011','2012']]

print(pd.DataFrame(['2010','2011','2012']))
print()

pd.DataFrame(list_example,columns=['A','G','Z'])
```

          0
    0  2010
    1  2011
    2  2012
    





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>G</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2010</td>
      <td>2011</td>
      <td>2012</td>
    </tr>
  </tbody>
</table>
</div>




```python
raw_data = [('Jones LLC', 150, 200, 50),
         ('Alpha Co', 200, 210, 90),
         ('Blue Inc', 140, 215, 95)]
column_name = ['account', 'Jan', 'Feb', 'Mar']
df_list = pd.DataFrame(sales, columns=labels)
df_list
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>account</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jones LLC</td>
      <td>150</td>
      <td>200</td>
      <td>50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alpha Co</td>
      <td>200</td>
      <td>210</td>
      <td>90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Blue Inc</td>
      <td>140</td>
      <td>215</td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>



### Dictionary


```python
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
football
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>losses</th>
      <th>team</th>
      <th>wins</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>Bears</td>
      <td>11</td>
      <td>2010</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>Bears</td>
      <td>8</td>
      <td>2011</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>Bears</td>
      <td>10</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>Packers</td>
      <td>15</td>
      <td>2011</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Packers</td>
      <td>11</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>5</th>
      <td>10</td>
      <td>Lions</td>
      <td>6</td>
      <td>2010</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Lions</td>
      <td>10</td>
      <td>2011</td>
    </tr>
    <tr>
      <th>7</th>
      <td>12</td>
      <td>Lions</td>
      <td>4</td>
      <td>2012</td>
    </tr>
  </tbody>
</table>
</div>



### CSV


```python
raw_data = pd.read_csv("../car-hire-projects/data/prefunnel_sessions.csv").drop(['Unnamed: 0'],1)

raw_data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>country</th>
      <th>which_device</th>
      <th>medium_grouped</th>
      <th>which_page_altered</th>
      <th>sessions</th>
      <th>funnel_sessions</th>
      <th>par</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>affiliate</td>
      <td>homepage</td>
      <td>2</td>
      <td>1</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>cpc</td>
      <td>landingpage</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>organic</td>
      <td>homepage</td>
      <td>3</td>
      <td>3</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>organic</td>
      <td>landingpage</td>
      <td>2</td>
      <td>2</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>windows</td>
      <td>affiliate</td>
      <td>homepage</td>
      <td>5</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



### Excel


```python
ncaa = pd.read_excel('Book1.xlsx', 'Sheet1')
ncaa.head(2)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20180101</td>
      <td>0.257626</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20180102</td>
      <td>0.361488</td>
    </tr>
  </tbody>
</table>
</div>



## Data Manipulation
- general stuff
- query
- column creation
- group by, aggregate functions
- conditional columns and values
- joins, append and concatentate
- pivot table

### General Stuff


```python
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
```

           date     value
    0  20180101  0.257626
    1  20180102  0.361488
    2  20180103  0.530100
    3  20180104  0.878999
    4  20180105  0.927968
           date     value
    0  20180101  0.257626
    1  20180102  0.361488
            date     value
    11  20180112  0.170648
    12  20180113  0.425049
    13  20180114  0.234976
    14  20180115  0.112915
    15  20180116  0.533506
            date     value
    14  20180115  0.112915
    15  20180116  0.533506
                   date      value
    count  1.600000e+01  16.000000
    mean   2.018011e+07   0.468379
    std    4.760952e+00   0.273009
    min    2.018010e+07   0.112915
    25%    2.018010e+07   0.251964
    50%    2.018011e+07   0.408800
    75%    2.018011e+07   0.582456
    max    2.018012e+07   0.927968
    date       int64
    value    float64
    dtype: object
           date     value
    3  20180104  0.878999
    4  20180105  0.927968
           value
    0   0.257626
    1   0.361488
    2   0.530100
    3   0.878999
    4   0.927968
    5   0.346599
    6   0.144388
    7   0.922274
    8   0.392552
    9   0.729304
    10  0.525677
    11  0.170648
    12  0.425049
    13  0.234976
    14  0.112915
    15  0.533506
           date which_device which_page_altered
    0  20180301   mobile_web           homepage
    3  20180301   mobile_web        landingpage
    4  20180301      windows           homepage
    6  20180301      windows             others





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>medium_grouped</th>
      <th>sessions</th>
      <th>par</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20180301</td>
      <td>affiliate</td>
      <td>2</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20180301</td>
      <td>cpc</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20180301</td>
      <td>organic</td>
      <td>3</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20180301</td>
      <td>organic</td>
      <td>2</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20180301</td>
      <td>affiliate</td>
      <td>5</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



### Query
- selection of rows and etc


```python
print(raw_data[raw_data.sessions == 1].head(3))

```

           date    country which_device medium_grouped which_page_altered  \
    1  20180301  (not set)   mobile_web            cpc        landingpage   
    5  20180301  (not set)      windows      affiliate        landingpage   
    6  20180301  (not set)      windows      affiliate             others   
    
       sessions  funnel_sessions  par  
    1         1                1  1.0  
    5         1                0  0.0  
    6         1                0  0.0  



```python
print(raw_data[(raw_data.sessions == 1) & (raw_data.medium_grouped == 'organic')].head(3))
```

            date  country which_device medium_grouped which_page_altered  \
    29  20180301  Andorra   mobile_web        organic           homepage   
    31  20180301  Andorra      windows        organic           homepage   
    32  20180301   Angola   mobile_web        organic           homepage   
    
        sessions  funnel_sessions  par  
    29         1                1  1.0  
    31         1                0  0.0  
    32         1                1  1.0  



```python
### a much simpler way of doing
raw_data.query("sessions == 1 & medium_grouped == 'organic'").head(3)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>country</th>
      <th>which_device</th>
      <th>medium_grouped</th>
      <th>which_page_altered</th>
      <th>sessions</th>
      <th>funnel_sessions</th>
      <th>par</th>
      <th>testing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>29</th>
      <td>20180301</td>
      <td>Andorra</td>
      <td>mobile_web</td>
      <td>organic</td>
      <td>homepage</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>31</th>
      <td>20180301</td>
      <td>Andorra</td>
      <td>windows</td>
      <td>organic</td>
      <td>homepage</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>32</th>
      <td>20180301</td>
      <td>Angola</td>
      <td>mobile_web</td>
      <td>organic</td>
      <td>homepage</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Column creation


```python
def multiplier(df,column1,column2):
    value = df[column1] * df[column2]
    return value
```


```python
raw_data['transformed_variable'] = multiplier(raw_data,'sessions','sessions')
```


```python
raw_data.head(2)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>country</th>
      <th>which_device</th>
      <th>medium_grouped</th>
      <th>which_page_altered</th>
      <th>sessions</th>
      <th>funnel_sessions</th>
      <th>par</th>
      <th>testing</th>
      <th>transformed_variable</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>affiliate</td>
      <td>homepage</td>
      <td>2</td>
      <td>1</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>cpc</td>
      <td>landingpage</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Group By


```python
raw_data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>country</th>
      <th>which_device</th>
      <th>medium_grouped</th>
      <th>which_page_altered</th>
      <th>sessions</th>
      <th>funnel_sessions</th>
      <th>par</th>
      <th>testing</th>
      <th>transformed_variable</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>affiliate</td>
      <td>homepage</td>
      <td>2</td>
      <td>1</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>cpc</td>
      <td>landingpage</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>organic</td>
      <td>homepage</td>
      <td>3</td>
      <td>3</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>organic</td>
      <td>landingpage</td>
      <td>2</td>
      <td>2</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>windows</td>
      <td>affiliate</td>
      <td>homepage</td>
      <td>5</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python
(
    raw_data
    .groupby(['medium_grouped'])
    .sum()
    ['sessions']
    .reset_index()
    .head()
)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>medium_grouped</th>
      <th>sessions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>(not set)</td>
      <td>2634</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3rdparty</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>about_section</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>affiliate</td>
      <td>80777</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b2b</td>
      <td>5277</td>
    </tr>
  </tbody>
</table>
</div>




```python
(
    raw_data
    .groupby(['medium_grouped'])
    .agg({"sessions":"sum","funnel_sessions":"sum"})
    .reset_index()
    .head()
)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>medium_grouped</th>
      <th>sessions</th>
      <th>funnel_sessions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>(not set)</td>
      <td>2634</td>
      <td>1197</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3rdparty</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>about_section</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>affiliate</td>
      <td>80777</td>
      <td>18208</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b2b</td>
      <td>5277</td>
      <td>2118</td>
    </tr>
  </tbody>
</table>
</div>



### Conditional columns and values


```python
raw_data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>country</th>
      <th>which_device</th>
      <th>medium_grouped</th>
      <th>which_page_altered</th>
      <th>sessions</th>
      <th>funnel_sessions</th>
      <th>par</th>
      <th>testing</th>
      <th>transformed_variable</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>affiliate</td>
      <td>homepage</td>
      <td>2</td>
      <td>1</td>
      <td>0.5</td>
      <td>0.5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>cpc</td>
      <td>landingpage</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>organic</td>
      <td>homepage</td>
      <td>3</td>
      <td>3</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>organic</td>
      <td>landingpage</td>
      <td>2</td>
      <td>2</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>windows</td>
      <td>affiliate</td>
      <td>homepage</td>
      <td>5</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python
raw_data['which_page_altered'] = (
    np.where(raw_data.medium_grouped == 'organic',"special_homepage",
             np.where(raw_data.which_device == 'mobile_web',"not_special_homepage",raw_data.medium_grouped))
```


```python
raw_data.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>country</th>
      <th>which_device</th>
      <th>medium_grouped</th>
      <th>which_page_altered</th>
      <th>sessions</th>
      <th>funnel_sessions</th>
      <th>par</th>
      <th>testing</th>
      <th>transformed_variable</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>affiliate</td>
      <td>not_special_homepage</td>
      <td>2</td>
      <td>1</td>
      <td>0.500000</td>
      <td>0.5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>cpc</td>
      <td>not_special_homepage</td>
      <td>1</td>
      <td>1</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>organic</td>
      <td>special_homepage</td>
      <td>3</td>
      <td>3</td>
      <td>1.000000</td>
      <td>3.0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>mobile_web</td>
      <td>organic</td>
      <td>special_homepage</td>
      <td>2</td>
      <td>2</td>
      <td>1.000000</td>
      <td>2.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>windows</td>
      <td>affiliate</td>
      <td>affiliate</td>
      <td>5</td>
      <td>0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>25</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>windows</td>
      <td>affiliate</td>
      <td>affiliate</td>
      <td>1</td>
      <td>0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>windows</td>
      <td>affiliate</td>
      <td>affiliate</td>
      <td>1</td>
      <td>0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>windows</td>
      <td>cpc</td>
      <td>cpc</td>
      <td>5</td>
      <td>3</td>
      <td>0.600000</td>
      <td>1.8</td>
      <td>25</td>
    </tr>
    <tr>
      <th>8</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>windows</td>
      <td>direct</td>
      <td>direct</td>
      <td>9</td>
      <td>6</td>
      <td>0.666667</td>
      <td>4.0</td>
      <td>81</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20180301</td>
      <td>(not set)</td>
      <td>windows</td>
      <td>email</td>
      <td>email</td>
      <td>1</td>
      <td>1</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Join, append and concatenate


```python
data = pd.read_csv("../multi-touch-attribution-garage-markov-variant/data/simulated_scenarios/csv/dataset_top_25_channels__current_state.csv")
```


```python
data.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>event_type</th>
      <th>event_id</th>
      <th>channel</th>
      <th>value</th>
      <th>timestamp</th>
      <th>event_type_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>touchpoint</td>
      <td>0</td>
      <td>organic</td>
      <td>0.091366</td>
      <td>1483228800000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>touchpoint</td>
      <td>0</td>
      <td>organic</td>
      <td>0.100503</td>
      <td>1483228800100</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>touchpoint</td>
      <td>1</td>
      <td>sem ggf</td>
      <td>0.110095</td>
      <td>1483228800110</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>touchpoint</td>
      <td>2</td>
      <td>organic</td>
      <td>0.100503</td>
      <td>1483228800120</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>touchpoint</td>
      <td>3</td>
      <td>sem ggf</td>
      <td>0.100086</td>
      <td>1483228800130</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>touchpoint</td>
      <td>0</td>
      <td>organic</td>
      <td>0.091366</td>
      <td>1483228800200</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>conversion</td>
      <td>1</td>
      <td>conversion</td>
      <td>0.550000</td>
      <td>1483228800201</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>touchpoint</td>
      <td>0</td>
      <td>sem ggf</td>
      <td>0.100086</td>
      <td>1483228800300</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4</td>
      <td>touchpoint</td>
      <td>0</td>
      <td>direct</td>
      <td>0.128613</td>
      <td>1483228800400</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>5</td>
      <td>touchpoint</td>
      <td>0</td>
      <td>direct</td>
      <td>0.141474</td>
      <td>1483228800500</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_revenue_user = (
    data
    .query("event_type == 'conversion'")
    .groupby(['user_id'])
    .agg({"value":"sum"})
    .reset_index()
    .rename(columns={"value":"revenue","user_id":"userid"})
)

df_revenue_user.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userid</th>
      <th>revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0.55</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>0.55</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>0.55</td>
    </tr>
    <tr>
      <th>3</th>
      <td>19</td>
      <td>1.10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>0.55</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>touchpoints</th>
      <th>revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>4</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>1</td>
      <td>0.55</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>1</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>


