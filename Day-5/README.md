# Day 5 Log

### PROBLEM STATEMENT
> Learn about running a subprocess in Python.
> Add error handling

**METHODOLOGY**  
1. Studied Python’s `subprocess` module and official documentation.  
2. Practiced running commands, capturing output, and interacting with child processes.  
3. Explored advanced features like streaming output and sending data via `stdin`.
4. Added error handling for five different cases
    - Ping command not found
    - Simulated error in working code
    - Connection timeout
    - Internet connection failed
    - Incorrect DNS

**WHAT I LEARNED**  
1. `subprocess.run()` executes a command and can capture `stdout`/`stderr` for later use.  
2. `subprocess.Popen()` enables real-time communication with a running process via `stdin` and `stdout`.

**REFERENCE MATERIAL**  
1. https://docs.python.org/3/library/subprocess.html
