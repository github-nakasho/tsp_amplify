#!/usr/bin/env python3

from amplify import decode_solution


def visualize_solution(x, values):
    # execute decoding
    x_sol = decode_solution(x, values, 1)
    print(x_sol)