
## Instructions

**Building the Docker Image for Development**

To build the image for development, without env variable execute the command :

```bash
docker build -f Dockerfile.dev -t fisrt-docker-image .
```

To build the image for development, with environment variables command :

```bash
 docker build --build-arg DATABASE_URL=your_database_url_here -f Dockerfile.dev -t fisrt-docker-image . 
```

**Checking Images**

To view all Docker images, use the command :

```bash
docker images
```

**Verify the config:**

To Verify the config, use the command :

```bash
docker inspect fisrt-docker-image
```

**Running the Container for Dev:**

To run the container for Dev, use the following command:

```bash
docker run -d --name dev-cont1 -p 8000:8000 fisrt-docker-image
```

**Explanation of Running the Container command:**

- `d` is for detach after running the container in the background.
- `--name dev-cont1` assigns the name `dev-cont1` to the container.
- `-p 8000:8000` maps port 8000 of the host to port 8000 of the container.
- `fisrt-docker-image` is the name of the Docker image to run.


**Running and interacting with the Container for Dev:**

To run the container and interact with it, use the following command:
```bash
docker run -it --name dev-cont1 -p 8000:8000 fisrt-docker-image
```

**to view container logs**

```bash
docker logs container name 0r container id 
ex: docker logs dev-cont1 
```

**command to run to test the test cases Test the Container:**

```bash
docker run -it --rm fisrt-docker-image /bin/bash -c "poetry run pytest"
```

**Explanation of command to run to test the test cases Test the Container:**

- `--rm` This option automatically removes the container when it exits. It's useful for cleaning up after the container's job is done, ensuring that stopped containers do not accumulate on your system.
- `/bin/bash` This part of the command specifies the shell that will be used to execute the subsequent command. In this case, it's the Bash shell, which is a common Unix shell and command language.
- `-c` This part of the command specifies the shell that will be used to execute the * *subsequent command* *. example: running this command "poetry run pytest"


**"Listing Active Docker Containers"**

```bash
docker ps
```

**Viewing All Docker Containers**

```bash
docker ps -a
```

**Entering and  Executing Commands Inside a running Docker Container**

```bash
docker exec -it dev-cont1 /bin/bash
```

**Explanation of command Executing Commands Inside a Docker Container:**

- `docker exec` This part of the command is used to execute a command in a running container.
- `it` These flags combine -i (interactive) and -t (allocate a pseudo-TTY). They allow you to interact with the container via the terminal.
- `dev-cont1` This is the name of the Docker container you want to interact with.
- `/bin/bash` This is the command to be executed inside the container. It starts a Bash shell, which is a command-line interface for interacting with the container's operating system.

**Exiting a Docker Container Shell Session**

this command will stop the running conatiner 

```bash
exit
```

**Exiting a Docker Container Shell Session without stopping the container**

this command will send container to background 

```bash
CTRL + p + Q
```

**creating image from running container**

```bash
docker commit <containerId or name> <new image name>
Ex: docker commit ag8f / devcont1 newimagefromcontainer 
```