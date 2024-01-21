import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    squared_diff = [(tar - pred) ** 2 for tar, pred in zip(tar, pred)]
    mse = sum(squared_diff) / len(tar)
    rmse = mse ** 0.5 # TODO: Implement RMSE Calculation here...
    return rmse