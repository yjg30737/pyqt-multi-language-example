from setuptools import setup, find_packages

setup(
    name='pyqt-multi-language-example',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='Simple example of how to support multi language with JSON and python dictionary in PyQt',
    url='https://github.com/yjg30737/pyqt-multi-language-example.git',
    install_requires=[
        'PyQt5',
    ]
)