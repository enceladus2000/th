import numpy as np
import matplotlib.pyplot as plt

def plot_surface(x, y, z):
    """This function is very different from matplotlib's. The x's and y's are 
    1D arrays indicating x and y coordinates at which to plot the function. z 
    is a 2D array of shape (len(y), len(x)) - columns of a matrix are considered 
    along the x axis.

    Args:
        x (_type_): _description_
        y (_type_): _description_
        z (_type_): _description_
    """
    x, y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if callable(z):
        z = z(x, y)
    else:
        assert z.shape == (len(y), len(x)), "z must have shape (len(y), len(x)) if an array. "

    ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

    return ax

if __name__ == "__main__":
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    z = lambda x, y: x**2 + y**2
    z = np.random.normal(1., 0.0005, size=(len(y), len(x)))
    ax = plot_surface(x, y, z)

    plt.show()