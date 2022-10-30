from backtest import backtest
import numpy as np
from scipy import stats
from scipy.optimize import minimize
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import statsmodels.api as sm

'''
strat_function(preds, prices) - user specified mapping from past n days of price and analyst data to weights.
Returns: An array of asset weightings. The maximum weighting is 1, and the minimum is -1. The weights must sum to between -1 and 1. 

Refer to test datasets for the shape of input data. Both preds and prices will be 2 dimensional arrays, with number of columns equal to number of assets + 1.
Number of days equal to number of rows. The first column will be date data.

Your strategy function needs to work with this data to geenrate portfolio weights.


'''
dir = "../test_datasets/PriceData.csv"
raw_data = pd.read_csv(dir, header=0, index_col=0)
# build stock tickers/symbols list
assets = list(raw_data)
# create dataframe to store close price of stocks

for i in range(253):
    df = raw_data.drop(labels=["Basic shares outstanding"])
    df['Market'] = df.sum(axis=1)
    returns = df.pct_change()
    # Iterate over column names
    betas = []
    exp_ret = []
    excess_returns = returns.drop(labels=["Market"], axis=1)
    for column in excess_returns:
        LR = stats.linregress(returns['Market'].iloc[1:], excess_returns[column].iloc[1:])
        beta, alpha, r_val, p_val, std_err = LR
        betas.append(beta)
        exp_ret.append(beta * returns['Market'].mean())
    raw_data = raw_data.append(raw_data.iloc[-1,:] * (np.asarray(exp_ret)+1))
raw_data.to_csv('original+predictions.csv')
plt.interactive(False)
raw_data.drop(labels=["Basic shares outstanding"]).plot(y=["AOX", "YPA", "KWE"])
plt.show()
