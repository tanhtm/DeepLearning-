import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.datasets

def load_dataset(fn):
    data = pd.read_csv(fn, header = None)
    x_ = data.iloc[:, 0: -1].values
    y_ = data.iloc[:, -1:].values
    X = x_.T
    Y = y_.T
    return X, Y    
    
def load_extra_datasets():  
    N = 200
    noisy_circles = sklearn.datasets.make_circles(n_samples=N, factor=.5, noise=.3)
    noisy_moons = sklearn.datasets.make_moons(n_samples=N, noise=.2)
    blobs = sklearn.datasets.make_blobs(n_samples=N, random_state=5, n_features=2, centers=6)
    gaussian_quantiles = sklearn.datasets.make_gaussian_quantiles(mean=None, cov=0.5, n_samples=N, 
                                                                  n_features=2, n_classes=2,
                                                                  shuffle=True, random_state=None)
    no_structure = np.random.rand(N, 2), np.random.rand(N, 2)
    return noisy_circles, noisy_moons, blobs, gaussian_quantiles, no_structure