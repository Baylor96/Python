from setuptools import setup

setup(
    name='Helloworld',
    version='1.0',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
    [console_scripts]
    hello=hello:cli
    ''',
)