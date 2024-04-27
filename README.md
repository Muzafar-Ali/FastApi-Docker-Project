# Project Name

## Instructions

### Building the Docker Image for Development

To build the image for development, execute the command :
docker build -f Dockerfile.dev -t fisrtDockerImage 


To build the image for development, with environment variables command :
docker build --build-arg DATABASE_URL=your_database_url_here -t fisrtDockerImage.

### Checking Images

To view all Docker images, use the command :
docker images

### Verify the config:

To Verify the config, use the command  :
docker inspect my-dev-image

### Running the Container for Dev:

To Running the Container for Dev, use the command : 
docker run -d --name dev-cont1 -p 8000:8000 my-dev-image

