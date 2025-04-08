from setuptools import find_packages, setup

setup(
    name="Churn-Prediction",
    version="0.1",
    packages=find_packages(),
    install_requires=[
    "pandas",
    'numpy',
    'seaborn',
    'pickle',
    'scikit-learn',
    'logging',
    "pytest",
    ]
)