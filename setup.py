from setuptools import setup

setup(
    name="smartrm",
    version="0.2.0",
    packages=['smartrm'],
    author="Victoria Stanko",
    author_email="vstanko1998@gmail.com",
    description="Utility for removing files and directories.",
    url="https://bitbucket.org/Vereline/lab2-clever-rm",

    entry_points={
        'console_scripts': [
            'smartrm = smartrm.Main:main'
        ]
    }
)
