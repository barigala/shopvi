from setuptools import setup, find_packages

setup(
    name='Shop-mobile-automation-appium',
    version='1.0',
    description='Vi Shop Mobile Automation',
    author='Sunil Barigala',
    packages=find_packages(),
    install_requires=[
        'Appium-Python-Client',
        'allure-pytest',
        'pytest',
        'selenium',
        'Pillow',
        'behave',
    ],
)