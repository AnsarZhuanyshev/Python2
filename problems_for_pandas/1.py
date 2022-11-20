#----------------------deleting all empty rows----------------
import pandas as pd 

data_frame = pd.read_csv('2023 QS World University Rankings.csv') 

data_frame.dropna(inplace = True )

print("Hello")
