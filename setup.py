# coding=utf8

from setuptools import setup
import os

description = 'A Python dict subclass which tries to act like JavaScript objects, so you can use the dot-notation (d.foo) to access members of the object.'

try:
    import pypandoc
    readme_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
    long_description = pypandoc.convert_file(readme_path, 'rst')

except ImportError:
    long_description = description

setup(
    name='mydict',
    version='1.0.8',
    author=u'León Domingo',
    author_email='leon@codevince.dev',
    description=description,
    long_description=long_description,
    license='MIT',
    keywords='dict javascript dot-notation codevince',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
    ],
    url='https://github.com/codevincedev/mydict',
    packages=[
        'mydict',
    ],
    install_requires=[
        'pytest',
    ]
)
