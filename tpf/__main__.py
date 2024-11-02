import argparse
from tpf.mandelbrot import plot_mandelbrot, plot_julia

def mandelbrot_plot_cli():
    """CLI for generating Mandelbrot set images."""
    parser = argparse.ArgumentParser(description="Plot the Mandelbrot set with customizable parameters.")
    
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        default="Mandelbrot.png", 
        help="Output file name (default: Mandelbrot.png)"
    )
    parser.add_argument(
        "--zmin", 
        type=complex, 
        default=-2.0 - 1.5j, 
        help="Minimum complex value for the plot (default: -2.0-1.5j)"
    )
    parser.add_argument(
        "--zmax", 
        type=complex, 
        default=1.0 + 1.5j, 
        help="Maximum complex value for the plot (default: 1.0+1.5j)"
    )
    parser.add_argument(
        "--pixel_size", 
        type=float, 
        default=1e-3, 
        help="Pixel size for plot resolution (default: 1e-3)"
    )
    parser.add_argument(
        "--max-iter", 
        type=int, 
        default=50, 
        help="Maximum number of iterations for the sequence (default: 100)"
    )
    
    args = parser.parse_args()
    plot_mandelbrot(
        zmin=args.zmin,
        zmax=args.zmax,
        pixel_size=args.pixel_size,
        max_iter=args.max_iter,
        figname=args.output
    )
    
    print("Plot saved as", args.output)

def julia_plot_cli():
    """CLI for generating Julia set images."""
    parser = argparse.ArgumentParser(description="Plot a Julia set with customizable parameters.")
    
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        default="Julia.png", 
        help="Output file name (default: Julia.png)"
    )
    parser.add_argument(
        "-c", "--c", 
        type=complex, 
        default=-0.8 + 0.156j, 
        help="Complex constant for the Julia set (default: -0.8+0.156j)"
    )
    parser.add_argument(
        "--zmin", 
        type=complex, 
        default=-2.0 - 1j, 
        help="Minimum complex value for the plot (default: -2.0-1.5j)"
    )
    parser.add_argument(
        "--zmax", 
        type=complex, 
        default=2.0 + 1j, 
        help="Maximum complex value for the plot (default: 1.0+1.5j)"
    )
    parser.add_argument(
        "--pixel_size", 
        type=float, 
        default=1e-3, 
        help="Pixel size for plot resolution (default: 1e-3)"
    )
    parser.add_argument(
        "--max-iter", 
        type=int, 
        default=10, 
        help="Maximum number of iterations for the sequence (default: 100)"
    )
    
    args = parser.parse_args()
    plot_julia(
        c=args.c,
        zmin=args.zmin,
        zmax=args.zmax,
        pixel_size=args.pixel_size,
        max_iter=args.max_iter,
        figname=args.output
    )
    
    print("Plot saved as", args.output)
