import matplotlib.pyplot as plt


def showf(x,
          y,
          xlim=(None, None),
          ylim=(None, None),
          title=None,
          label=None,
          xlabel=None,
          ylabel=None,
          legend=False,
          grid=False,
          linest='-',
          color=None,
          figsize_x=7,
          figsize_y=4):
    plt.plot(x, y, label=label, color=color, linestyle=linest)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(grid)
    if legend:
        plt.legend()
    plt.gcf().set_size_inches(figsize_x, figsize_y)
    plt.show()


def showfs(x,
           y: list,
           xlim=(None, None),
           ylim=(None, None),
           title=None,
           labels: list = None,
           xlabel=None,
           ylabel=None,
           legend=False,
           grid=False,
           linest: list = None,
           colors: list = None,
           figsize_x=7,
           figsize_y=4):
    if (labels is None):
        labels = [None] * len(y)
    if (linest is None):
        linest = ['-'] * len(y)
    if (colors is None):
        colors = [None] * len(y)

    if isinstance(x, list):
        for k in range(len(y)):
            plt.plot(x[k],
                     y[k],
                     label=labels[k],
                     linestyle=linest[k],
                     color=colors[k])
    else:
        for k in range(len(y)):
            plt.plot(x,
                     y[k],
                     label=labels[k],
                     linestyle=linest[k],
                     color=colors[k])
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(grid)
    if legend:
        plt.legend()
    plt.gcf().set_size_inches(figsize_x, figsize_y)
    plt.show()
