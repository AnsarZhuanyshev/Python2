import pandas as pd 
import matplotlib.pyplot as plt 

data_frame = pd.read_csv('2023 QS World University Rankings.csv')

data_frame.plot()

plt.show()