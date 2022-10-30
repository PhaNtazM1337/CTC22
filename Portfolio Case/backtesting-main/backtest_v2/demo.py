from backtest import backtest
import numpy as np
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



def get_ret_vol_sr(weights,log_ret):
    """
    Takes in weights, returns array or return,volatility, sharpe ratio
    """
    weights = np.array(weights)
    ret = np.sum(log_ret.mean() * weights) * 252
    vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))
    sr = ret / vol
    return np.array([ret, vol, sr])


def neg_sharpe(weights,log_ret):
    return get_ret_vol_sr(weights,log_ret)[2] * -1


# Contraints
def check_sum(weights):
    '''
    Returns 0 if sum of weights is 1.0
    '''
    return np.sum(weights) - 1


  # maximum sharpe value is actually 3.35


def strat_function(preds, prices, prev_weights):
    # # raw_data.append(pd.Series(prices))
    # df = raw_data.drop(labels=["Basic shares outstanding"])
    # log_ret = np.log(df/df.shift(1))
    # # By convention of minimize function it should be a function that returns zero for conditions
    # cons = ({'type': 'eq', 'fun': check_sum})
    #
    # # 0-1 bounds for each weight
    # bounds = list((0,1) for i in range(40))
    #
    # # Initial Guess (equal distribution)
    return prev_weights
    #
    # # Sequential Least SQuares Programming (SLSQP).
    # opt_results = minimize(neg_sharpe, init_guess, log_ret, method='SLSQP', bounds=bounds, constraints=cons)
    # print("*")
    # return opt_results.x
    #return [0.28373274033839435, 0.0, 0.006939912339570646, 5.119123065076353e-16, 0.10197130196220884, 1.0241403673914439e-14, 2.503968969539994e-16, 0.04233502451838096, 3.649547145513784e-16, 0.0, 0.0, 1.1535757732887265e-14, 6.6934082639915995e-15, 1.1197939162439517e-15, 0.0, 0.09142295920469004, 8.265441976115077e-15, 3.3592985668912836e-15, 0.0, 0.0, 1.1004534110480361e-14, 0.0, 0.38414781739105547, 2.0894581709814832e-14, 0.01964434685951555, 1.1913438189568382e-14, 6.111491970782257e-17, 6.111406224280564e-15, 0.0, 0.0, 7.951070229039513e-15, 0.0, 2.7223551336834693e-15, 2.3750677859776595e-15, 0.006710747571626175, 1.0115761619579589e-14, 0.0, 0.006681655918455713, 0.0, 0.056413493896024854]

'''
Running the backtest - starting portfolio value of 10000, reading in data from these two locations.
'''
sharpe=-1
num=1
while(sharpe<0):
    init_guess = np.random.rand(40)
    init_guess = init_guess / np.sum(init_guess)
    print(num)
    num+=1
    sharpe = backtest(strat_function, init_guess, 10000, '../test_datasets/PriceData.csv', '../test_datasets/preds.csv', True, "log.csv")
print(sharpe)
