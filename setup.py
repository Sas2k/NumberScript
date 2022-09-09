import setuptools

with open('README.md') as f:
    longest_description = f.read()

setuptools.setup(
    name="NumberScript",
    version="1.13.0",
    description="possibly the world's most simplest and restricted language.",
    author="Sasen Perera",
    long_description=longest_description,
    long_description_content_type="text/markdown",
    packages=["NumberScript"],
    github_url="https://github.com/Sas2k/NumberScript",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #adding executable
    entry_points={
        'console_scripts': [
            'NumberScript = NumberScript.main:main',
            'nspm = NumberScript.nspm:main'
        ]
    },
    python_requires='>=3.6'
)