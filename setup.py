from setuptools import setup, find_packages


setup(
    name='pyAudioAnalysis',
    version='2017.11.17',
    author='Giannakopoulos, Theodoros',
    url='https://github.com/tyiannak/pyAudioAnalysis',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'sklearn',
        'hmmlearn',
        'simplejson',
        'eyed3',
        'pydub',
    ],
)
