from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '2.8.0'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='google_images_download',
    version=__version__,
    keywords='google images download save filter color image-search image-dataset image-scrapper image-gallery terminal command-line',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=install_requires,
    dependency_links=dependency_links,
    entry_points={
        'console_scripts': [
            'googleimagesdownload = google_images_download.google_images_download:main'
        ]},

)
