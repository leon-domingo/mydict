# coding=utf8

from setuptools import setup
import pypandoc

setup(
    name='mydict',
    version='1.0.4',
    author=u'León Domingo',
    author_email='leon@codevince.dev',
    description='A Python dict subclass which tries to act like JavaScript objects, so you can use the dot-notation (d.foo) to access members of the object.',
    long_description=pypandoc.convert_file('./README.md', 'rst'),
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
