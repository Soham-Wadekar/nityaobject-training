from setuptools import setup, find_packages

setup(
    name="email_checker",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "email-checker=email_checker.cli:main",
        ],
    },
)
