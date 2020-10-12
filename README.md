# EngineeringAssessment
A containerized Nameko service that provides three simple functions.

## The Development Summarized

**Development Environment Setup:**

 I haven't programmed in Python for quite a few months; I'd have to check my commits on `pymathfi` to be sure. On my Windows desktop, the following steps outline how I set up my Python development environment.

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

I have never used Docker before, so I worked through the first half of [this tutorial](https://www.youtube.com/watch?v=fqMOX6JJhGo). Another tutorial that was an excellent resource was [Introduction to Nameko with Docker](https://max6log.wordpress.com/2017/04/23/introduction-to-nameko-with-docker/). My plan for the implementation was to roughly complete it in three phases.


1. First create three, simple working functions. This was `threefunctions.py`.
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

To complete the assignment, I remove the files created by `pipenv` as well as the initial draft, `threefunctions.py`, as they're no longer necessary. Final test was to clone the repository fresh in a different location and ensure that the above steps all work.

## Review
Overall, I had a blast! The microservices approach is new to me, as my background in programming is mostly related to implementing numerical methods for my own use. I can, however, immediately see the value. The entire assessment took about 5 hours with most of that time spent learning the basics of Docker and `docker-compose`.