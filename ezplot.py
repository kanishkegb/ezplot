from __future__ import print_function

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pdb


def plot(*args, **kwargs):

    mode, x, y = select_mode(*args)
    # pdb.set_trace()
    print(mode)
    if mode=='single':
        plt.plot(x[0])

    return

def select_mode(*args):

    all_x = []
    all_y = []
    for i, arg in enumerate(args):
        if i % 2:
            all_y.append(arg)
        else:
            all_x.append(arg)

        mode = 'unknown'

    if i==0:
        return 'single', all_x, all_y
    elif not i % 2:
        raise ValueError('data must be in the format (x1, y1, x2, y2, ...)')


    return mode, all_x, all_y

if __name__ == "__main__":

    x = np.arange(0, 10)
    # plot(x, 2*x, 3*x, x)
    plot(x)
    plt.show()
