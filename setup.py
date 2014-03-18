from distutils.core import setup


setup(
	name='DelightedPython',
    version='0.0.1.5',
    author='Testive, Inc',
    author_email='lee@testive.com',
    packages=['delighted', 'delighted.test'],
    url='http://pypi.python.org/pypi/DelightedPython/',
    license='LICENSE.txt',
    description='Python wrapper for the Delighted API',
    long_description=open('README.rst').read(),
    install_requires=[
       'requests >= 2.2.1'
    ],
)