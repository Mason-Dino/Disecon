from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
readme = (here / 'README.md').read_text(encoding='utf-8')

classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Disecon',
  version='0.6.7',
  description='Disecon',
  long_description=readme,
  long_description_content_type="text/markdown",
  url='',  
  author='LegosAndStuff',
  license='MIT', 
  classifiers=classifiers,
  keywords='economy', 
  packages=find_packages(),
  install_requires=[''] 
)