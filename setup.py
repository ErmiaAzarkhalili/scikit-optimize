try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='skopt',
      version='0.0',
      description='Sequential model-based optimization toolbox.')
