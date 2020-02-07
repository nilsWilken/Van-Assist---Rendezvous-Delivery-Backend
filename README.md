
## Installation

To start and use this webservice as a Docker container, it is required to have a Docker Engine installed and running.
If this is not the case, you can find instructions on how to install Docker Engine here: https://docs.docker.com/install/

Once you have Docker installed and running you can either build the provided docker files yourself from the command line, or you can use the "prepare_vanassistwebservice_docker.py" script.

In case you want to build the docker images yourself from the command line, the Dockerfile in the "VanAssistUbuntu" directory has to be built
before the Dockerfile in the "vanassist---webservice" directory.

A more convenient way to build all required images and start the webservice as a container is to used the provided python script.
Obviously, to execute it you have to first install python on your machine.

When you have python and a version of pip installed. You can use pip to install the required docker module for python with the following command:
    'pip install docker'

Now you are ready to execute the "prepare_vanassistwebservice_docker.py" script, which will automatically build all required images and start a docker container with the
webservice.
