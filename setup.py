from setuptools import setup, find_packages

setup(
    name='mojproject',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'numpy',
        'opencv-python',
        'Pillow',
        'chess',
        'keras',
    ],
    python_requires='>=3.8.2',
)