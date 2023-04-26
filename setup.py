from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pidgin-eng-dictionary',
  version='0.0.1',
  description='A simple pidgin-english dictionary for various applications',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/Zeecoworld/pidgin-english-dictionary',  
  author='Isaac Yakubu',
  author_email='engrisaac1234@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='dictionary,pidgin/english,pidgin dictionary', 
  packages=find_packages(),
  install_requires=['difflib'] 
)