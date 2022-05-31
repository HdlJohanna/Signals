from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Signals',
  version='0.2',
  description=' Fast, simple object-to-object and broadcast signaling',
  long_description=open('README.MD').read(),
  long_description_content_type='text/markdown',
  url='',  
  author='HdlJohanna',
  author_email='hdljohanna@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='signal emit blink broadcast', 
  packages=find_packages(),
  install_requires=[] 
)
