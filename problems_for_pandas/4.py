##-------------wrong data---------------
import pandas as pd 

data_frame = pd.read_csv('2023 QS World University Rankings.csv')

for i in data_frame.index:#### i is number of row in ar score column
    if data_frame.loc[i,'ar score'] % 10 != 0 :###number should be devided by 10 without any aditions 
        data_frame.loc[i,'ar score'] = round(data_frame.loc[i,'ar score'])######we have rounded all numbers which not devisible by 10 

print(data_frame['ar score'])