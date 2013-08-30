__author__ = 'vshanmugam'

from setuptools import setup

setup(name='dilibs',
      version='1.0',
      description='di libraries',
      url='https://github.com/vaidy-ror/dirobot.git',
      author='vaidyanathan shanmugam',
      author_email='vaidyanathan_shanmugam@intuit.com',
      license='',
      packages=['dilibs',],
      install_requires = [
                          'robotframework-selenium2library==1.3.0',
                          'robotframework-rammbock==0.3.0',
                          'robotframework-androidlibrary==0.1.19',
                          'robotframework-httplibrary==0.4.2',
                          'robotframework-requests==0.3.3',
                          'robotframework==2.8.1',
                          'requests==1.2.3',
                          'dipipinstall==1.0'
                          ],
      zip_safe=False)