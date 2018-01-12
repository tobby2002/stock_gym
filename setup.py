from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1c'

dependency_links = [
    'https://github.com/openai/gym'
]


setup(
    name='stock_gym',
    packages=['stock_gym'],
    version=version,
    description="An OpenAI Gym environment for stock market data",
    long_description=README + '\n\n' + NEWS,
    classifiers=[],
    keywords='openai-gym-environments openai-gym openai',
    author='Bobby',
    author_email='karma0@gmail.com',
    url='https://github.com/karma0/stock_gym',
    license='MIT',
)