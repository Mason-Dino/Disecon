from setuptools import setup, find_packages

readme = ""
with open("README.md") as f:
  readme = f.read

classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Disecon',
  version='0.1.9',
  description='Disecon',
  long_description=readme,
  long_description_content_type="md",
  url='',  
  author='LegosAndStuff',
  license='MIT', 
  classifiers=classifiers,
  keywords='economy', 
  packages=find_packages(),
  install_requires=[''] 
)