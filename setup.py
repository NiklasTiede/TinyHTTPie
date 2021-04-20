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
    project_urls={
        'GitHub': 'https://github.com/NiklasTiede/tinyHTTPie',
        'Documentation': 'https://tinyhttpie.readthedocs.io',
    },
    license="MIT",
    py_modules = ["tihttp"],
    install_requires=[      
        "requests",
    ],
    extras_require={    
        'dev': [
            'pytest',
        ],
    },
    platforms=["any"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["tihttp = tihttp:run_main"]},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
