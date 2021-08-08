# docker for begginer 
* **Image** : A Docker image is a file used to execute code in a Docker container
* **Container** : *A container is a runnable instance of an image* . A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. [more](https://www.docker.com/resources/what-container)
* **daemon** : The Docker daemon ( dockerd ) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services. [Docker overview](https://docs.docker.com/get-started/overview/)


### docker run 
The docker run command first creates a writeable container layer over the specified image, and then starts it using the specified command. That is, docker run is equivalent to the API /containers/create then /containers/(id)/start. [more](https://docs.docker.com/engine/reference/commandline/run/)

### docker ps
List containers . e.x : `docker ps -a`
* --all , -a		Show all containers (default shows just running)

### docker image
Manage images



# Dockerfile
[Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

```
FROM ubuntu:18.04
COPY . /app
RUN make /app
CMD python /app/app.py
```
* **FROM** creates a layer from the ubuntu:18.04 Docker image.
* **COPY** adds files from your Docker client’s current directory.
* **RUN** builds your application with make.
* **CMD** specifies what command to run within the container.

### Build context example
Create a directory for the build context and cd into it. Write “hello” into a text file named hello and create a Dockerfile that runs cat on it. Build the image from within the build context (.):

```
 mkdir myproject && cd myproject
 echo "hello" > hello
 echo -e "FROM busybox\nCOPY /hello /\nRUN cat /hello" > Dockerfile
 docker build -t helloapp1:v1 .
```

now if run

```
docker images 
```
now you can see below line : 
```
REPOSITORY    TAG     IMAGE ID     CREATED             SIZE
helloapp1      v1    f5cc1eb21ff8  31 seconds ago      1.24MB

```

### stdin example

```
echo -e 'FROM busybox\nRUN echo "hello world"' | docker build -
# OR 
docker build -<<EOF
FROM busybox
RUN echo "hello world"
EOF
# OR 
docker build -t myimage:latest -<<EOF
FROM busybox
RUN echo "hello world"
EOF
```

The example below uses the current directory (.) as the build context, and builds an image using a Dockerfile that is passed through stdin

```
# create a directory to work in
mkdir example
cd example

# create an example file
touch somefile.txt

# build an image using the current directory as context, and a Dockerfile passed through stdin
docker build -t myimage:latest -f- . <<EOF
FROM busybox
COPY somefile.txt ./
RUN cat /somefile.txt
EOF
```

The example below builds an image using a Dockerfile from stdin, and adds the hello.c file from the “hello-world” Git repository on GitHub.

```
docker build -t myimage:latestgit -f- https://github.com/docker-library/hello-world.git <<EOF
FROM busybox
COPY hello.c ./
EOF
```
# Dockerfile instructions
## FROM
The FROM instruction initializes a new build stage and sets the Base Image for subsequent instructions.

## RUN
The RUN instruction will execute any commands in a new layer on top of the current image and commit the results.

### apt-get
Probably the most common use-case for RUN is an application of apt-get. Because it installs packages, the RUN apt-get command has several gotchas to look out for.

```
# syntax=docker/dockerfile:1
FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y curl
```
After building the image, all layers are in the Docker cache. Suppose you later modify `apt-get install` by adding extra package:

```
# syntax=docker/dockerfile:1
FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y curl nginx   #add nginx
```

Docker sees the initial and modified instructions as identical and reuses the cache from previous steps. As a result the apt-get update is not executed because the build uses the cached version. Because the apt-get update is not run, your build can potentially get an outdated version of the curl and nginx packages.

Using RUN apt-get update && apt-get install -y ensures your Dockerfile installs the latest package versions with no further coding or manual intervention. This technique is known as **cache busting**. You can also achieve cache-busting by specifying a package version. 

## CMD
The CMD instruction should be used to run the software contained in your image. [more](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#cmd)

## ENV 
The ENV instruction sets the environment variable `<key>` to the value `<value>`.

```
ENV MY_NAME="John Doe"
ENV MY_DOG=Rex\ The\ Dog
ENV MY_CAT=fluffy

#real example 
ENV PG_MAJOR=9.3
ENV PG_VERSION=9.3.4
RUN curl -SL https://example.com/postgres-$PG_VERSION.tar.xz | tar -xJC /usr/src/postgres && …
ENV PATH=/usr/local/postgres-$PG_MAJOR/bin:$PATH
```
## ADD or COPY
Although **ADD** and **COPY** are functionally *similar*, generally speaking, *COPY* is preferred. That’s because it’s more transparent than ADD. COPY only supports the basic copying of local files into the container, while *ADD has some features* (like local-only tar extraction and remote URL support) that are not immediately obvious. Consequently, the best use for ADD is local tar file auto-extraction into the image, as `in ADD rootfs.tar.xz /.`

## EXPOSE
The EXPOSE instruction indicates the ports on which a container listens for connections. Consequently, you should use the common, traditional port for your application. For example, an image containing the Apache web server would use EXPOSE 80, while an image containing MongoDB would use EXPOSE 27017 and so on.

---
## VOLUME
The VOLUME instruction should be used to expose any database storage area, configuration storage, or files/folders created by your docker container. You are strongly encouraged to use VOLUME for any mutable and/or user-serviceable parts of your image.

## WORKDIR
The WORKDIR instruction sets the working directory for any RUN, CMD, COPY and ADD instructions that follow it in the Dockerfile . 

note : For clarity and reliability, you should always use absolute paths for your WORKDIR


# Docker Compose
**Compose** is a **tool** for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.
* YAML : It's often used as a format for configuration files . [YAML Tutorial: Everything You Need to Get Started in Minutes](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started)



## Get started with Docker Compose

* Using Compose is basically a three-step process:

* Define your app’s environment with a Dockerfile so it can be reproduced anywhere.

* Define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment.

Run docker compose up and the Docker compose command starts and runs your entire app. You can alternatively run docker-compose up using the docker-compose binary.

in this [page](https://docs.docker.com/compose/gettingstarted/) you build a simple Python web application running on Docker Compose. The application uses the Flask framework and maintains a hit counter in Redis. While the sample uses Python, the concepts demonstrated here should be understandable even if you’re not familiar with it. 








### reference

* [Docker Docs](https://docs.docker.com/)
* [YAML](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)
* [YAML Tutorial](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started)
* [Docker for beginners](https://docker-curriculum.com/)



author : *MH.sharifi* <br>
date : 2021 08 August
