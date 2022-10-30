import pandas as pd
import numpy as np 

a1 = pd.read_csv("Predicted Testing Data Analyst 1.csv").to_numpy()
a2 = pd.read_csv("Predicted Testing Data Analyst 2.csv").to_numpy()
a3 = pd.read_csv("Predicted Testing Data Analyst 3.csv").to_numpy()



final = (a1 + a2 + a3) / 3
final = np.hstack((np.expand_dims(np.arange(start = 0, stop = final.shape[0]), axis=1) ,final))
np.savetxt( "averaged.csv", final)



