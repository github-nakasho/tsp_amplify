#!/usr/bin/env python3

import numpy as np

def make_instance():
    # set the number of cities
    N = 5
    # set random matrix
    d = np.random.rand(N, N)
    # make symmetric matrix
    d = (d+d.T) / 2 - np.diag(np.diag(d))
    # input feed_dict for hyperparameters
    feed_dict = {'h1': 1.0, 'h2': 1.0}
    return d, feed_dict