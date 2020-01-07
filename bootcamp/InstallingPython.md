# Installing Python

## Python Version

Python has and continues to be developed by the
community.  10 years ago, the majority of the world
used Python 2 while Python 3 was under development.
Today, Python 3 is the standard and will be the 
requirement for LAMAT.

And within Python 3, there are a number of sub-versions:
Python 3.6, 3.7, and coming soon 3.8.  Most software
developers are using Python 3.7 now and we strongly
recommend that you do so too.

## Python Distribution

There are many python distributions online but we 
require that you install with 
[Anaconda](https://www.anaconda.com/distribution/).
They offer support for nearly every platform.
We hope that your computing is either Linux or
MacOS.  If you are using Windows, it is possible
you will struggle with some aspects of the computing.
At the least, we recommend you install 
[Cygwin](https://www.cygwin.com/) which provides
some functionality similar to Unix.

From the webpage above, you should be able to 
download and install Python 3.7.  Be sure to follow 
closely the Installation notes
on the website.  If you already
have an installation of Python, we recommend you
remove it and start from scratch.

## Test yourself

If you feel you have successfully installed Python,
try the following:

### Launch a Jupyter Notebook 

There are multiple ways to do this.
From a Terminal on a Linux or MacOS system,
you can type:

```jupyter notebook```

and the software will then start in your
brower (e.g. Safari, Chrome).
You then start a New Notebook by choosing
*Python 3* under the *New* button.

There are many tutorials on Jupyter Notebooks
online.  Here are a few that we recommend
(ignore notes on Installation):

* [Towards Data Science](https://towardsdatascience.com/a-beginners-tutorial-to-jupyter-notebooks-1b2f8705888a)
* [Jupyter Notebook Docs](https://jupyter-notebook.readthedocs.io/en/stable/)

Note that [Jupyter Lab](https://jupyterlab.readthedocs.io/en/latest/)
is a more sophisticated version.  We won't use that
during Bootcamp.

### Confirm your version of Python

In a cell in your Notebook, input:

```
import sys
sys.version
```

And execute the cell (either by clicking on Run
or typing Shift+Enter).

You should see something like:

```
Out[1]:  '3.7.3 (default, Mar 27 2019, 22:11:17) \n[GCC 7.3.0]'
```

### Confirm other key packages are installed

Now try to import a number of other packages that
we will use during Bootcamp.  Input this into
a new cell in your Notebook:

``` 
import matplotlib
import astropy
import scipy
import numpy
```

and then execute the cell.  It should run
without any warnings or errors.  
If so, you are all set!