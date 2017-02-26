# coding=utf8

from setuptools import setup
import os

readme_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
try:
    import pypandoc
    long_description = pypandoc.convert_file(readme_path, 'rst')

except ImportError:
    # when you're installing the package, "pypandoc" is not required
    with open(readme_path) as f:
        long_description = f.read()

setup(
    name='mydict',
    version='1.0.7',
    author=u'León Domingo',
    author_email='leon@codevince.dev',
    description='A Python dict subclass which tries to act like JavaScript objects, so you can use the dot-notation (d.foo) to access members of the object.',
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
