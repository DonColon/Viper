from setuptools import setup
from os import path


def loadDescription():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.md'), encoding='utf-8') as file:
        return file.read()


setup(
    name='viper',
    version='0.0.1',
    license='MIT',

    description='A web server build from scratch with Python.',
    long_description=loadDescription(),
    long_description_content_type='text/markdown',

    url='https://github.com/DonColon/Viper',
    author='Dardan Rrafshi',
    author_email='drrafshi@hotmail.de',

    keywords='http server request response',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: System Administrators',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'License :: OSI Approved :: MIT License',
    ],
    packages=['viper'],

    # TODO Dependency Listing
)
