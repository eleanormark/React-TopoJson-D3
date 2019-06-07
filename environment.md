# Setting up your environment

To get started on this challenge:

- Download and install Docker via their website:
    - Mac: https://store.docker.com/editions/community/docker-ce-desktop-mac
    - Windows 10 Pro: https://store.docker.com/editions/community/docker-ce-desktop-windows
    - Windows 7 or later: https://docs.docker.com/toolbox/toolbox_install_windows/

- See [troubleshooting](./help.md) documentation for more info

## Building the container

To build the application container, run `make build` in the base directory. The console output should look something like:

```bash
$ make build
docker-compose -f docker-compose.yml -p amino-challenge stop
docker-compose -f docker-compose.yml -p amino-challenge rm -f
No stopped containers
find . -name '*.pyc' -delete
find . -name '__pycache__' -delete
docker-compose -f docker-compose.yml -p amino-challenge build
Building app
Step 1 : FROM python:3.7-alpine
 ---> d1128d077f32
Step 2 : RUN apk add --update make sqlite
 ---> Using cache
 ---> da96ad32775f
Step 3 : ENV APP /data/app
 ---> Using cache
 ---> 0ddc51a48595
... and so on
```

This will take a bit to run the first time as it downloads the base image and initially populates the database, then should be fast after subsequent builds.

## Running tests
To run the tests, run `make test` in the base directory. The console output should look something like:

```bash
$ make test
docker-compose -f docker-compose.yml -p amino-challenge run --rm app test
pytest tests
========================================================================== test session starts ===========================================================================
platform linux -- Python 3.5.2, pytest-3.0.4, py-1.4.31, pluggy-0.4.0
rootdir: /data/app, inifile:
collected 4 items

tests/test_server.py ....

======================================================================== 4 passed in 0.40 seconds ========================================================================
```

## Running the server
To run the server, run `make run` in the base directory, and navigate to your local server at [http://localhost:5000](http://localhost:5000). 
When you start up server, you should see console output like below. When you navivate there, you should see a fun surprise.

```bash
$ make run
docker-compose -f docker-compose.yml -p amino-challenge up
Creating aminochallenge_app_1
Attaching to aminochallenge_app_1
app_1  | python runserver.py
app_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

## Developing your application

Volume mappings between your local machine and the container's `app/www` and `app/test` folders have been created in the docker-compose file used by the Makefile, which should allow you to run tests and make changes to the backend server without rebuilding your container. Docker's volume mapping technology isn't perfect though, so if you have trouble or encounter weird behavior, if all else fails kill your server, rebuild the container using `make build`, and try again.


# Halp!

If you have difficulty getting things up and running, please email us at [coding.challenge@amino.com](mailto:coding.challenge@amino.com).