# Project Name

## Instructions

### Building the Docker Image for Development

To build the image for development, execute the command :

<div class="copy-button-container">
  <code class="command">docker build --build-arg DATABASE_URL=your_database_url_here -t fisrt-docker-Image .
</code>
</div>

### Checking Images

To view all Docker images, use the command :

<div class="copy-button-container">
  <code class="command">docker images</code>
</div>

### Verify the config:

To Verify the config, use the command :

<div class="copy-button-container">
  <code class="command">docker inspect fisrt-docker-Image</code>
</div>

### Running the Container for Dev:

To run the container for Dev, use the following command:

<div class="copy-button-container">
  <code class="command">docker run -d --name dev-cont1 -p 8000:8000 fisrt-docker-Image</code>
</div>

**Explanation of command:**

- `d` is for detach after running the container in the background.
- `--name dev-cont1` assigns the name `dev-cont1` to the container.
- `-p 8000:8000` maps port 8000 of the host to port 8000 of the container.
- `fisrt-docker-Image` is the name of the Docker image to run.
