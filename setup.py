from setuptools import setup

setup(
    name='tipbot',
    version='1',
    py_modules=['tipbot'],
        install_requires=[
            'Click',
    ],
    entry_points='''
        [console_scripts]
        tip=tipbot:cli
        tip-lasts=tipbot:last
    ''',
)
