import ezplot as ezp
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    x = np.arange(1, 10)
    y = x

    fig1 = ezp.SubPlot(2, 3)
    fig1.suptitle('Test1')

    fig1.subplot(0, 1)
    fig1.ez_plot(x, y)

    plt.show()
