#!/usr/bin/env python3

from amplify import BinaryPoly, gen_symbols, sum_poly
from amplify.constraint import equal_to


def make_hamiltonian(d, feed_dict):
    # set the number of cities
    N = len(d)
    # set hyperparameters
    lambda_1 = feed_dict['h1']
    lambda_2 = feed_dict['h2']
    # make variables
    x = gen_symbols(BinaryPoly, N, N)
    # set One-hot constraint for time
    h1 = [equal_to(sum_poly([x[n][i] for n in range(N)]), 1) for i in range(N)]
    # set One-hot constraint for city
    h2 = [equal_to(sum_poly([x[n][i] for i in range(N)]), 1) for n in range(N)]
    # compute the total of constraints
    const = lambda_1 * sum(h1) + lambda_2 * sum(h2)
    # set objective function
    obj = sum_poly(N, lambda n: sum_poly(N, lambda i: sum_poly(N, lambda j: d[i][j]*x[n][i]*x[(n+1)%N][j]), ), )
    # compute model
    model = obj + const
    return x, model
