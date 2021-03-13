from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Numeth_Yon_package',
  version='0.0.1',
  description='Modules for finding Roots',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='YON_Fajardo,Timbungco,Rodriguez,Vitales',
  author_email='donna.mae.fajardo.@adamson.edu.ph',
  license='MIT', 
  classifiers=classifiers,
  keywords='roots', 
  packages=find_packages(),
  install_requires=[''] 
)