.. TPF Mandelbrot-Julia documentation master file, created by
   sphinx-quickstart on Fri Nov  1 20:47:23 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PAPY TP Final : Mandelbrot-Julia
=================================

Welcome to the Mandelbrot-Julia project documentation. 
This project provides a comprehensive toolset for visualizing fractal patterns, specifically the Mandelbrot and Julia sets. 
Even if I am french, this documentation is written in english to train for my internship.

Project Overview
----------------

The TPF Mandelbrot-Julia project includes the following main functionalities:

- **Mandelbrot Set Visualization**: Generates and plots the Mandelbrot set. The Mandelbrot set is defined by iterating the function \( f(z) = z^2 + c \), where `z` starts at zero, and `c` represents each point in the complex plane.

- **Julia Set Visualization**: Generates and plots the Julia set for a given complex parameter \( c \). The Julia set is a generalization of the Mandelbrot set.

Command Line toolset
--------------------

Main functions:

- **MandelbrotPlot** for the Mandelbrot set

- **JuliaPlot** for the Julia set (needs a complex number as argument)

Parameters:

- **-o, --output**: Output file name (optional)
- **--zmin**: Minimum complex value for the plot (optional)
- **--zmax**: Maximum complex value for the plot (optional)
- **--pixel_size**: Pixel size (optional)
- **--max-iter**: Maximum number of iterations (optional, default: 100)
- **-c, --c**: Complex value for the Julia plot. (optional). Do not forget to put the complex number between quotes! 

In depth code documentation
---------------------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   module