# This module plots user-specified trig functions

# Import all the definitions from the numpy and plotting libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the plotting function
def makeplot(funcname):

    # Define the x array
    x = np.arange(0, 2*np.pi, 0.01)

    # Check if the user entered the sin, cos, or tan function
    if funcname=='sin':
        plt.plot(x, np.sin(x))
    elif funcname=='cos':
        plt.plot(x, np.cos(x))
    elif funcname=='tan':
        plt.plot(x, np.tan(x))
    else:
        print("Unrecognized function "+str(funcname))

# Define a new plotting function
def makeplot_2(funcname, wavelength=[2*np.pi]):

    # Define the x array
    x=np.arange(0, 2*np.pi, 0.01)

    # Loop over wavelengths
    for w in wavelength:

        # Check if the user entered the sin, cos, or tan function
        if funcname=='sin':
            plt.plot(x, np.sin(x*2*np.pi/w))
        elif funcname=='cos':
            plt.plot(x, np.cos(x*2*np.pi/w))
        elif funcname=='tan':
            plt.plot(x, np.tan(x*2*np.pi/w))
        else:
            print("Unrecognized function "+str(f))
            return

# Define the plotting function that handles exceptions
def makeplot_3(funcname, wavelength=[2*np.pi]):

    # Define the x array
    x=np.arange(0, 2*np.pi, 0.01)

    # Try to loop over wavelengths to make sure it's possible. If not,
    # turn wavelengths into a list.
    try:
        for w in wavelength:
            pass
    except TypeError:
        wavelength=[wavelength]

    # Loop over wavelengths
    for w in wavelength:

        # Check if the user entered the sin, cos, or tan function
        if funcname=='sin':
            plt.plot(x, np.sin(x*2*np.pi/w))
        elif funcname=='cos':
            plt.plot(x, np.cos(x*2*np.pi/w))
        elif funcname=='tan':
            plt.plot(x, np.tan(x*2*np.pi/w))
        else:
            print("Unrecognized function "+str(f))
            return
