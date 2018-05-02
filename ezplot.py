from __future__ import print_function

import itertools
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pdb


def plot(*args, **kwargs):

    x, y, num_subplots = select_mode(*args)
    # y.append(np.arange(0, 10))

    # if mode=='single':
    #     plt.figure()
    #     plt.plot(x[0], **kwargs)
    # elif mode=='xy':
    #     if not num_subplots:
    #         plt.figure()
    #         for i in range(len(x)):
    #             plt.plot(x[i], y[i], **kwargs)
    #     else:
    m, n = num_subplots
    print('m: {}, n: {}'.format(m, n))
    fig, axes = plt.subplots(m, n)
    for i, j in list(itertools.product(range(len(y)), range(m*n))):
        print('{}, {}'.format(i, j))
        try:
            ax = axes[j]
        except TypeError:
            ax = axes
            if len(y)==1 and m==1:
                print(1)
                y = [y]
        # pdb.set_trace()
        ax.plot(x[i], y[i][j], **kwargs)

    return


def select_mode(*args):

    all_x = []
    all_y = []
    len_x = 0
    flag_first_run = True
    for i, arg in enumerate(args):
        if i % 2:
            m, n, transpose = get_size(arg)
            if flag_first_run:
                flag_first_run = False
                num_data_series = m
            num_data_points = n
            if not num_data_points==n:
                raise ValueError('each (x, y) must have same lengths\n'
                'for pair {}, the length of x is {}, but the length of y is '
                '{}'.format(i % 2, len_x, len_y))

            if transpose:
                all_y.append(arg.T)
            else:
                all_y.append(arg)
        else:
            m, n, transpose = get_size(arg)
            if flag_first_run:
                num_data_series = m
            num_data_points = n

            if transpose:
                all_x.append(arg.T)
            else:
                all_x.append(arg)

    if i==0:
        return [np.arange(0, num_data_points)], all_x, (m, 1)


    elif not i % 2:
        raise ValueError('data must be in the format (x1, y1, x2, y2, ...)')
    else:
        mode = 'xy'
        m, n = np.shape(all_y[0])
        num_subplots = min([m, n])

    return all_x, all_y, (num_subplots, 1)


def get_size(arr):
    try:
        m, n = np.shape(arr)
        if m > n:
            m, n = n, m
            transpose_flag = True
        else:
            transpose_flag = False

    except ValueError:
        m = 1
        n = len(arr)
        transpose_flag = False

    return m, n, transpose_flag


if __name__ == "__main__":

    x = np.arange(0, 10)

    # plot(x, 2*x, 3*x, x, linestyle='dashed')
    plot(x, color='green')
    # plot(x, np.array([x, 2*x]), color='green')
    # plot(np.array([x, 2*x]), color='green')
    plot(np.random.rand(2, 10), color='green')
    # pdb.set_trace()
    plt.show()
