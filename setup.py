import os
from setuptools import setup, find_packages

try:
    from unittest import mock
except ImportError:
    mock = None


tests_require = ['netCDF4', 'pytest']
if mock is None:
    tests_require += ['mock']


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Scientific/Engineering',
]


setup(name='h5netcdf',
      description='netCDF4 via h5py',
      long_description=(open('README.rst').read()
                        if os.path.exists('README.rst')
                        else ''),
      version='0.5.0',
      license='BSD',
      classifiers=CLASSIFIERS,
      author='Stephan Hoyer',
      author_email='shoyer@gmail.com',
      url='https://github.com/shoyer/h5netcdf',
      install_requires=['h5py'],
      tests_require=tests_require,
      packages=find_packages())
