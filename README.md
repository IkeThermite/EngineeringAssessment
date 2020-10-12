# EngineeringAssessment
A containerized Nameko service that provides three simple functions.


## The Development Summarized

**Development Environment Setup:**
 
 1. Installed Virtual Box.
 2. Created a Virtual Machine with Ubuntu 20.20.
 3. Installed `python3.6` globally by adding `deadsnakes` repository to system sources.
 4. Installed `pip` and `pipenv`.
 5. Installed `git` and Visual Studio Code.
    - Added the Python extension to VS Code.
 6. Created this repository on GitHub and cloned it to a local drive of the Virtual Machine.
 7. Created a `pipenv` virtual environment to use `python3.6`.
 8. Added the Pipfile, committed and pushed.
    - This needed a personal access token, since I have 2FA on my GitHub account.

**Development Procedure:**

1. First create three, simple working functions. 
2. Refactor those functions as a Nameko service and test.
    - This requires RabbitMQ installed.

Okay, this all went fine *except* the Huffman compression generates a `byte` literal, which can't be JSON serialized (obviously).
This means that it can't be used as a request or response payload with the RPC extension for Nameko. 
Since the spec requires that we return a dictionary, my solution is to create an additional hashtable to sit between the user of the service and the actual encoded (compressed) string.