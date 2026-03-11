import numpy as np

def sharpe_ratio(returns):

    returns = np.array(returns)

    if len(returns) < 2:
        return 0

    mean = np.mean(returns)
    std = np.std(returns)

    return (mean/std) * np.sqrt(252)