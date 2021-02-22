
import pathlib
import setuptools


setuptools.setup(
    name="tihttp",
    version="0.1.0",
    author='Niklas Tiede',
    author_email='niklastiede2@gmail.com',
    description="tiny HTTP client for making GET requests.",
    long_description=pathlib.Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    license="MIT",

    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"), 

    py_modules = ["tihttp"],
    
    install_requires=[
        "requests>=2.21",
    ],
    extras_require={
        'dev': [
            'pytest', # pip install tihttp[dev]
        ],
    },
    platforms="linux",
    python_requires=">=3.5",
    entry_points={
        "console_scripts": 
        ["tihttp=tihttp:run_main"]
        },
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Education',
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
