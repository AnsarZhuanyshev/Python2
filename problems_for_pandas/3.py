#------------convert into correct data-------------
import pandas as pd 

data_frame = pd.read_csv('2023 QS World University Rankings.csv')

data_frame['ar score'] = pd.to_numeric(data_frame['ar score'])
#######use function to_something 
####it could be string , datatime , timadelta , numeric 
#### but it can not convert empty strings to correct format 
print(data_frame['ar score'])