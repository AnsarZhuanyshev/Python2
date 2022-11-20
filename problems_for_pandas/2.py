#---------filling empty rows in the csv---------
import pandas as pd 

data_frame = pd.read_csv('2023 QS World University Rankings.csv')

values1 = data_frame["ar score"].mean()##### avarage value 
#values2 = data_frame["ar rank"].median()#### value in the middle after sorting 
values3 = data_frame["er score"].mode()[0]#### most frequently value 
values4 = data_frame["ger rank"].mode()[0]##### 
values5 = data_frame["ifr score"].mode()[0]#most frequent

##---------------median works for sorted integers--------

data_frame["ar score"].fillna(values1 , inplace = True)
#data_frame["ar rank"].fillna(values2 , inplace = True)
data_frame["er score"].fillna(values3 , inplace = True)
data_frame["ger rank"].fillna(values4 , inplace = True)
data_frame["ifr score"].fillna(values5 , inplace= True)
#print(data_frame["ar score"])
#print(data_frame["ar rank"])
#print(data_frame["er score"])

print(data_frame.info())