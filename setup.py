from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
readme = (here / 'README.md').read_text(encoding='utf-8')

classifiers = [
  'Development Status :: 5 - Production/Stable Copy',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.12'
]

setup(
  name='Disecon',
  version='1.0.0',
  description='Disecon',
  long_description=readme,
  long_description_content_type="text/markdown",
  url='https://github.com/Mason-Dino/Disecon',  
  author='LegosAndStuff',
  license='MIT', 
  classifiers=classifiers,
  keywords='economy', 
  packages=find_packages(),
  install_requires=[''] 
)