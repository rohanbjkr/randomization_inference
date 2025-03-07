from setuptools import setup, find_packages

setup(
    name='randomization_inference',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'statsmodels',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for performing randomization inference.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/randomization_inference', # Replace with your repo url.
)