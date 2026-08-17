"""
1.	Which function is not used for removing missing data in Pandas Module?
a.	fillna( ).
b.	replace( ).
c.	interpolate( ).
d.	isnull( ).
Ans:d
2.	Which function is used for detect missing data in Pandas Module?
a.	isnull( )
b.	replace( ).
c.	dropna( )
d.	fillna( ).
Ans:a
3.	Which one is not true iterating rows from dataframe from Pandas?
a.	iteritem( ) – access key-value pair of items.
b.	iterrows( ) – access key-row pair.
c.	itertuples( )- access rows as tuple.
d.	itercolumns( ) - access key-columns pair.
Ans:d
4.	Which one is invalid str function used for processing Dataframe?
a.	str.lower( ).
b.	str.contains().
c.	str.title( ).
d.	str.reverse( ).
Ans:d
5.	Which is not used to remove whitespace for Dataframe?
a.	str.strip().
b.	str.rstrip( ).
c.	str.lstrip( ).
d.	str.astrip( ).
Ans:d
"""
#2
import pandas as pd
import numpy as np
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#a
df = pd.DataFrame({
'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
'salesman_id':[5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.nan]})
print("Original Orders DataFrame:")
print(df)
#b Print Missing values of the dataframe:
print("\nMissing values of the said dataframe:")
print(df.isna())
print(df.isna().any())
#c convert from datadrame to csv1.csv file and read csv file by pandas
df.to_csv("csv1.csv",index=False)
df1=pd.read_csv("csv1.csv",skiprows=0)
print(df1)
#d Identify the columns which have at least one missing value 
print("\nIdentify the columns which have at least one missing value:")
print(df1.isna().any())
#e Count the number of missing values in each column
print("\ncount the number of missing values in each column:")
print(df1.isna().sum())
#f Replace the missing values with NaN:
print("\nReplace the missing values with NaN:")
result = df1.replace({"?": np.nan, "--": np.nan})
print(result)
#g Drop the rows where at least one element is missing: 
print("\nDrop the rows where at least one element is missing:")
result = df1.dropna()
print(result)
#h Drop the columns where at least one element is missing:
print("\nDrop the columns where at least one element is missing:")
result = df1.dropna(axis='columns')
print(result)
#i Drop the rows where all elements are missing
print("\nDrop the rows where all elements are missing:")
result = df1.dropna(how='all')
print(result)
#j Keep the rows with at least 2 NaN values of the said DataFrame 
print("\nKeep the rows with at least 2 NaN values of the said DataFrame:")
result = df1.dropna(thresh=2)
print(result)
#k Replace NaN value with mean value
print("Using mean to replace NaN:")
df['salesman_id'].fillna(int(df['salesman_id'].mean()), inplace=True)
print(df)
#l print Total missing values in a dataframe 
print("\nTotal missing values in a dataframe:")
tot_missing_vals = df1.isnull().sum().sum()
print(tot_missing_vals)


