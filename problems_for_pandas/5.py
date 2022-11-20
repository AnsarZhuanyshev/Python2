#-------------delete duplicates----------
import pandas as pd 

data_frame = pd.read_csv('2023 QS World University Rankings.csv')
### duplicated print yes if row is duplicated 
data_frame.drop_duplicates(inplace = True)###just delete

print(data_frame.info())