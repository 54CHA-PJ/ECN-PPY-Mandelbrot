from typing import Generator
import matplotlib.pyplot as plt
import numpy as np

def suite(c: complex, z: complex) -> Generator:
    """ 
    Computes the sequence of the Mandelbrot or Julia set.
    The sequence is defined by the function: f(z) = z^2 + c.

    Args:
        c (complex): Parameter
        z (complex): Initial value

    Yields:
        Generator: Suite of the Mandelbrot or Julia set
    """
    while True:
        yield z
        z = z * z + c

def suite_mandelbrot(c: complex) -> Generator:
    """ 
    Generates the Mandelbrot sequence for a given complex number c.
    Please refer to the "suite" function for more details.
    """
    return suite(c, z=0)

def suite_julia(c: complex, z: complex) -> Generator:
    """ 
    Generates the Julia sequence for a given complex number c and initial value z.
    Please refer to the "suite" function for more details.
    """
    return suite(c, z)

def is_in_mandelbrot(c: complex, max_iter=100) -> bool:
    """ 
    Checks if a complex number c belongs to the Mandelbrot set. 
    A point is in the set if the sequence is bounded.
    The sequence is aproximated by stopping the sequence when the norm is greater than 2.

    Args:
        c (complex)
        max_iter (int, optional): Maximum number of iterations. Defaults to 100.

    Returns:
        bool: True if c belongs to the Mandelbrot set, False otherwise.
    """
    z_iter = suite_mandelbrot(c)
    for _ in range(max_iter):
        z_next = next(z_iter)
        if np.abs(z_next) > 2:
            return False
    return True

def is_in_julia(c: complex, z: complex, max_iter=100, div_norm =2) -> bool:
    """ 
    Checks if a complex number z belongs to the Julia set for a given c.
    In other words, checks if the Julia sequence starting from z remains bounded.
    The sequence is aproximated by looking at the norm of the last computed value.

    Args:
        c (complex): Parameter of the Julia set.
        z (complex): Initial value in the complex plane.
        max_iter (int, optional): Maximum number of iterations. Defaults to 100.
        div_norm (int, optional): Divergence threshold. In other words, the sequence diverges if the norm of the last computed value is greater than div_norm. Defaults to 2.

    Returns:
        bool: True if z belongs to the Julia set for parameter c, False otherwise.
    """
    z_iter = suite_julia(c, z)
    for _ in range(max_iter):
        z_next = next(z_iter)
    return np.abs(z_next) <= div_norm

def plot_mandelbrot(
    zmin: complex = -2.0-1.5j,
    zmax: complex = 1.0+1.5j,
    pixel_size: float = 1e-3,
    max_iter: int = 100,
    figname: str = "Mandelbrot.png"
) -> None:
    """
    Displays the Mandelbrot set in the complex plane.

    Args:
        zmin (complex, optional): Lower bound of the display. Defaults to -2.0-1.5j.
        zmax (complex, optional): Upper bound of the display. Defaults to 1.0+1.5j.
        pixel_size (float, optional): Size of each pixel inside the display. Defaults to 1e-3.
        max_iter (int, optional): Maximum number of iterations. Defaults to 100.
        figname (str, optional): Name of the output file. Defaults to "Mandelbrot.png".
    """
    real_min, real_max = zmin.real, zmax.real
    imag_min, imag_max = zmin.imag, zmax.imag

    # Separate the real and imaginary parts
    real_values = np.arange(real_min, real_max, pixel_size)
    imag_values = np.arange(imag_min, imag_max, pixel_size)

    # Initialize the plot
    mandelbrot_set = np.zeros((len(imag_values), len(real_values)), dtype=bool)
    print(f"Plot density: {len(imag_values)} x {len(real_values)} px.")

    for i, imag in enumerate(imag_values):
        for j, real in enumerate(real_values):

            # Display progress
            if (i * len(real_values) + j) % (len(imag_values) * len(real_values) // 20) == 0:
                print(f"{100 * (i * len(real_values) + j) //
                      (len(imag_values) * len(real_values))}%")

            c = real + 1j * imag
            mandelbrot_set[i, j] = is_in_mandelbrot(c, max_iter=max_iter)
    print("100%")

    plt.imshow(
        mandelbrot_set,
        extent=[real_min, real_max, imag_min, imag_max],
        cmap='binary',
        origin='upper'  # Vertical flip
    )
    plt.axis('off')
    plt.savefig(figname, bbox_inches='tight', pad_inches=0)
    plt.show()


def plot_julia(
    c: complex = -0.8 + 0.156j,
    zmin: complex = -2.0-1.5j,
    zmax: complex = 1.0+1.5j,
    pixel_size: float = 1e-7,
    max_iter: int = 100,
    figname: str = "Julia.png"
) -> None:
    """Displays the Julia set in the complex plane.

    Args:
        c (complex): Parameter of the Julia set.
        zmin (complex, optional): Lower bound of the display. Defaults to -2.0-1.5j.
        zmax (complex, optional): Upper bound of the display. Defaults to 1.0+1.5j.
        pixel_size (float, optional): Size of each pixel inside the display. Defaults to 1e-3.
        max_iter (int, optional): Maximum number of iterations. Defaults to 100.
        figname (str, optional): Name of the output file. Defaults to "Mandelbrot.png".
    """
    real_min, real_max = zmin.real, zmax.real
    imag_min, imag_max = zmin.imag, zmax.imag

    # Separate the real and imaginary parts
    real_values = np.arange(real_min, real_max, pixel_size)
    imag_values = np.arange(imag_min, imag_max, pixel_size)

    # Initialize the plot
    julia_set = np.zeros((len(imag_values), len(real_values)), dtype=bool)
    print(f"Plot density: {len(imag_values)} x {len(real_values)} px.")

    for i, imag in enumerate(imag_values):
        for j, real in enumerate(real_values):

            # Display progress (only for development)
            if (i * len(real_values) + j) % (len(imag_values) * len(real_values) // 20) == 0:
                print(f"{100 * (i * len(real_values) + j) //
                      (len(imag_values) * len(real_values))}%")

            z = real + 1j * imag
            julia_set[i, j] = is_in_julia(c, z, max_iter=max_iter)
    print("100%")

    plt.imshow(
        julia_set,
        extent=[real_min, real_max, imag_min, imag_max],
        cmap='binary',
        origin='upper'  # Vertical flip
    )
    plt.axis('off')
    plt.savefig(figname, bbox_inches='tight', pad_inches=0)
    plt.show()


""" 
if __name__ == "__main__":

    # plot_mandelbrot()

    # plot_mandelbrot(
    #     zmin=-0.7440+0.1305j,
    #     zmax=-0.7425+0.1320j,
    #     pixel_size=5e-7,
    #     max_iter=200,
    #     figname="Mandelbrot_tentacle.png"
    # )

    plot_julia(
        c=-0.8 + 0.156j,
        zmin=-2-1j,
        zmax=2+1j,
        pixel_size=5e-4,
        max_iter=100,
        figname="Julia_-0.8+0.156j.png"
    )
"""