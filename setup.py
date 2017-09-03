from setuptools import setup

setup(
    name='bitbelt',
    packages=['bitbelt'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pymongo',
        'mongoengine',
        'six'
    ]
)
