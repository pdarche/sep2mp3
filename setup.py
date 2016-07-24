from setuptools import setup

setup(
    name='sep2mp3',
    description='A tool for converting Stanford Encyclopedia of Philosophy articles into mp3s',
    url='https://github.com/pdarche/sep2mp3',
    author='Peter Darche',
    license='MIT',
    install_requires=[
        'bs4',
        'requests'
    ],
    scripts=['bin/sep2mp3']
)
