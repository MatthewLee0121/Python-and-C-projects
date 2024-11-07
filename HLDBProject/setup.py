from setuptools import setup, Extension
import pybind11

setup(
    ext_modules=[
        Extension(
            "backend",  # This will be the name you use in Python to import
            ["backend.cpp"],  # C++ source file
            include_dirs=[pybind11.get_include()],
            language="c++",
        )
    ]
)
