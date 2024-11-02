import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mandelbrot import is_in_mandelbrot, is_in_julia

def test_is_in_mandelbrot():
    assert is_in_mandelbrot(c=-0.5) == True
    assert is_in_mandelbrot(c=-1.38) == True
    assert is_in_mandelbrot(c=1, max_iter=10) == False
    assert is_in_mandelbrot(c=2j, max_iter=10) == False

def test_is_in_julia():
    assert is_in_julia(z=0.25+0.25j,c=0.25)== True
    assert is_in_julia(z=-0.8-0.2j, c=0.2+0.5j)== False