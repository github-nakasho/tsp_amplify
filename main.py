#!/usr/bin/env python3

import make_hamiltonian as mh
import make_instance as mi
import solve_problem as sp
import visualize_solution as vs


if __name__ == '__main__':
    # get instance information
    d, feed_dict = mi.make_instance()
    # set hamiltonian for model
    x, model = mh.make_hamiltonian(d=d, feed_dict=feed_dict)
    # solve with amplify
    obj, values, broken = sp.solve_problem(model=model)
    print(broken)
    # visualize solution
    vs.visualize_solution(x=x, values=values)    
    