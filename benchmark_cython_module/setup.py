from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Benchmark cython module',
    ext_modules=cythonize("benchmark_cython_module.pyx"),
)