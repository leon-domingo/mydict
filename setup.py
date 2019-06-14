from setuptools import setup
import os

description = 'A Python dict subclass which tries to act like JavaScript objects, so you can use the dot-notation (d.foo) to access members of the object.'

try:
    readme_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
    with open(readme_path) as ld_f:
        long_description = ld_f.read()

except ImportError:
    long_description = description

setup(
    name='mydict',
    version='1.0.20',
    author=u'León Domingo',
    author_email='leon.domingo@gmail.com',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='dict javascript dot-notation',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
    ],
    url='https://github.com/leon-domingo/mydict',
    packages=[
        'mydict',
    ],
    install_requires=[
        'pytest',
    ]
)
