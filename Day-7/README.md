# Day 7 Log

### PROBLEM STATEMENT
> Convert the previously created email-reading Python script into a reusable Python module that can be imported into other scripts or used as a package.

**METHODOLOGY**
1. Modularized the script into different files:
    - `__init__.py`: Exports all public functions for easy import
    - `config.py`: Loads the environment variables from `.env`
    - `connection.py`: Handles IMAP connection and authentication
    - `utils.py`: Stores the utility functions of the package
2. Added an example usage in `examples/examples_usage.py`. Run it from the root directory of the package as `python -m examples.example_usage.py`.
3. You can now import it from the python shell.

**WHAT I LEARNED**
1. To create a reusable package in Python
