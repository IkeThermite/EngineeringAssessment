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

Okay, this all went fine *except* the Huffman compression generates a `byte` literal, which can't be JSON serialized.
This means that it can't be used as a request or response payload with the RPC extension for Nameko. 
Since the spec requires that we return a dictionary, my solution is to create an additional hashtable to sit between the user of the service and the actual encoded (compressed) string. I've added to `peek` functions to make working with both hashtables easy.

3. Now to containerize the application.

After some trial and error, it appears that it's more difficult to run `rabbitmq` inside the same container than what it is to use `docker-compose` and the official `rabbitmq` image. So that's what I've done.

**Using the Service:**

- Start by building the image from the Dockerfile: `docker-compose build`
- Then start the services in background (detached): `docker-compose up -d`
- Head over to the container's bash: `docker exec -it engineeringassessment_app_1 bash`
- Fire up the `nameko shell` with the proper config: `nameko shell --config conf.yml`

Now you can test the services. Example tests:

```python
n.rpc.engineering_assessment.square_odd([-4, -3, 1, 2, 3, 5, 10])
n.rpc.engineering_assessment.encode_strings(['this', 'is', 'a', 'test'])
n.rpc.engineering_assessment.peekAtStringHashes()
n.rpc.engineering_assessment.decode_string('lZoc1vIy') #this hash will be different
```

**Wrapping Up:**
To complete the assignment, I remove the files created by `pipenv` as well as the initial draft, `threefunctions.py`, as they're no longer necessary.