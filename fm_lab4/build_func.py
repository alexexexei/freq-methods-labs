import matplotlib.pyplot as plt


def build_f(x, y, fz1=16,
            fz2=5, clr=None, ttl=None,
            grid=True, legend=False, xlab=None,
            ylab=None, xl1=None, xl2=None,
            yl1=None, yl2=None, lbl=None,
            ls='-'):
    plt.plot(x, y, color=clr, label=lbl, linestyle=ls)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xl1, xl2)
    plt.ylim(yl1, yl2)
    plt.title(ttl)
    plt.gcf().set_size_inches(fz1, fz2)
    plt.grid(grid)
    if legend:
        plt.legend()
    plt.show()


def build_fs(x, y: list, colors: list=None,
             labels: list=None, fz1=16, fz2=5,
             ttl=None, grid=True, legend=False, 
             xlab=None, ylab=None, xl1=None,
             xl2=None, yl1=None, yl2=None,
             ls:list=None):
    if (y is None or len(y) <= 0):
        return
    if (colors is None):
        colors = [None] * len(y)
    if (labels is None):
        labels = [None] * len(y)
    if (ls is None):
        ls = ['-'] * len(y)

    for k in range(len(y)):
        plt.plot(x, y[k], color=colors[k], label=labels[k], linestyle=ls[k])
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xl1, xl2)
    plt.ylim(yl1, yl2)
    plt.title(ttl)
    plt.gcf().set_size_inches(fz1, fz2)
    plt.grid(grid)
    if legend:
        plt.legend()
    plt.show()
