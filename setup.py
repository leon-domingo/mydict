# coding=utf8

from setuptools import setup
import markdown

# get HTML description from "README.md", transformed into HTML
with open('./README.md', 'r') as readme_f:
    html_desc = markdown.markdown(readme_f.read())

setup(
    name='mydict',
    version='1.0.3',
    author=u'León Domingo',
    author_email='leon@codevince.dev',
    description='A Python dict subclass which tries to act like JavaScript objects, so you can use the dot-notation (d.foo) to access members of the object.',
    long_description=html_desc,
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
