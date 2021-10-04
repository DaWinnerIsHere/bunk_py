from setuptools import setup

setup(
   name='bunk_py',
   version='1.0',
   description='An API wrapper for BunkServices API.',
   author='DaWinnerIsHere',
   author_email='dawinnerishere@gmail.com',
   packages=['bunk_py'],
   package_dir={'bunk_py': './bunk_py.py'},
   install_requires=['wheel', 'bar', 'greek'],
)
