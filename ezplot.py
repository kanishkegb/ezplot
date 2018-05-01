from __future__ import print_function

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pdb


def plot(*args, **kwargs):

    plt.figure()
    mode, x, y = select_mode(*args)
    print(mode)
    if mode=='single':
        plt.plot(x[0], **kwargs)
    elif mode=='xy':
        for i in range(len(x)):
            plt.plot(x[i], y[i], **kwargs)
    return


def select_mode(*args):

    all_x = []
    all_y = []
    len_x = 0
    for i, arg in enumerate(args):
        if i % 2:
            len_y = len(arg)
            if not len_x==len_y:
                raise ValueError('each (x, y) must have same lengths\n'
                'for pair {}, the length of x is {}, but the length of y is '
                '{}'.format(i % 2, len_x, len_y))
            all_y.append(arg)
        else:
            len_x = len(arg)
            all_x.append(arg)

        mode = 'unknown'

    if i==0:
        return 'single', all_x, all_y
    elif not i % 2:
        raise ValueError('data must be in the format (x1, y1, x2, y2, ...)')
    else:
        mode = 'xy'

    return mode, all_x, all_y


if __name__ == "__main__":

    x = np.arange(0, 10)
    pdb.set_trace()

    # plot(x, 2*x, 3*x, x, linestyle='dashed')
    plot(x, color='green')
    # plot(np.array([[x], [2*x]]), color='green')
    plt.show()
