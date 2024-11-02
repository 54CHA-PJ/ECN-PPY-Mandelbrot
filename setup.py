from setuptools import setup, find_packages

setup(
    name="tpf_mandelbrot_julia",
    version="0.1",
    packages=find_packages(),
    description="A Python tool for plotting Mandelbrot and Julia sets with customizable options",
    author="Sacha Cruz",
    author_email="your_email@example.com",
    install_requires=[
        "matplotlib>=3.0.0",
        "numpy>=1.17.0",
    ],
    entry_points={
        "console_scripts": [
            "MandelbrotPlot=tpf.__main__:mandelbrot_plot_cli",
            "JuliaPlot=tpf.__main__:julia_plot_cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
