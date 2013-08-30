__author__ = 'vshanmugam'

from setuptools import setup

setup(name='diutils',
      version='1.0',
      description='di utilities',
      url='https://github.com/vaidy-ror/dirobot.git',
      author='vaidyanathan shanmugam',
      author_email='vaidyanathan_shanmugam@intuit.com',
      license='',
      packages=['diutils', 'diutils.autocomplete_indices'],
      scripts=['diutils/autocomplete_indices/autocomplete_indices.py'],
      install_requires=[
                          'dilibs==1.0',
                          'dipipinstall==1.0'
                          ],
      zip_safe=False)
