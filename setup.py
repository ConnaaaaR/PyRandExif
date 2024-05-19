from setuptools import setup, find_packages

setup(
    name="pyRandExif",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A command-line tool to add random EXIF data to images.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ConnaaaaR/PyRandExif",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "Pillow>=8.0.0",
        "piexif>=1.1.3",
    ],
    entry_points={
        "console_scripts": [
            "pyRandExif=pyRandExif.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
