from setuptools import setup

setup(
    name='breast_cancer_ml_project',
    version='0.1',
    packages=['components', 'pipelines'],
    install_requires=[
        'scikit-learn',
        'flask',
    ],
)
