import matplotlib.pyplot as plt
import ezplot as ezp

if __name__ == "__main__":

    fig1 = ezp.SubPlot(3, 2)
    print(fig1.rows)
    print(fig1.cols)

    fig1.subplot(1)
    fig1.suptitle('Test1')

    plt.show()
