from setuptools import setup, find_packages

setup(
    name='Visualization_utils',
    version='0.1',
    packages=find_packages(),
    description='A collection of helper functions for data analysis',
    author='Tushar Mahalya',
    author_email='tusharmahalya.com',
    url='https://github.com/tushar-mahalya/Visualization_Utils',
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)