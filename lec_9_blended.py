import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.transforms as transforms

def vanilla_plot():
    fig, ax = plt.subplots()
    x = np.random.randn(1000)

    ax.hist(x, 30)
    ax.set_title(r'$sigma=1  dots  sigma=2$', fontsize=16)

    # the x coords of this transformation are data, and the y coord are axes
    # highlight the 1..2 stddev region with a span.
    # We want x to be in data coordinates and y to span from 0..1 in axes coords.
    rect = mpatches.Rectangle((1, 0), width=1, height=1,
                              color='yellow', alpha=0.5)
    ax.add_patch(rect)

    plt.show()

def blended_plot():
    fig, ax = plt.subplots()
    x = np.random.randn(1000)

    ax.hist(x, 30)
    ax.set_title(r'$sigma=1  dots  sigma=2$', fontsize=16)

    # the x coords of this transformation are data, and the y coord are axes
    trans = transforms.blended_transform_factory(
        ax.transData, ax.transAxes)
    # highlight the 1..2 stddev region with a span.
    # We want x to be in data coordinates and y to span from 0..1 in axes coords.
    rect = mpatches.Rectangle((1, 0), width=1, height=1, transform=trans,
                              color='yellow', alpha=0.5)
    ax.add_patch(rect)

    plt.show()
    
    
if __name__ == "__main__":
    vanilla_plot()
    # blended_plot()