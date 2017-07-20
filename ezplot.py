import matplotlib as mpl
import matplotlib.pyplot as plt

class SubPlot:
    ''' subplot class '''


    def __init__(self, rows, cols):

        if not isinstance(rows, int):
            print('ezplot error: Number of subplot rows must be an integer.')
            return

        if not isinstance(cols, int):
            print('ezplot error: Number of subplot columns must be an integer.')
            return

        self.rows = rows
        self.cols = cols
        self.max_ax = rows * cols

        self.fig, self.ax = plt.subplots(rows, cols)

        return


    def subplot(self, subplot_number):

        if not isinstance(subplot_number, int):
            print('ezplot error: subplot index must be an integer.')
            return

        if subplot_number > self.max_ax:
            print('ezplot error: subplot index must be less than rows x columns')
            return

        if subplot_number < 0:
            print('ezplot error: subplot index must be a positive integer.')
            return

        self.n_ax = subplot_number

        return


    def suptitle(self, title):
        self.fig.suptitle(title, fontsize=12)

        return

    def plot(self, params):
        return
