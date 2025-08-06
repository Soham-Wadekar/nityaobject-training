# Day 2 Log

### PROBLEM STATEMENT
> Task 1: Create a Dockerfile, build an image, add the Day 1 script in it and run it as a container
> Task 2: Perform a Trivy scan on the Docker image

**METHODOLOGY**<br>
*Task 1*
1. Copy the code to a separate folder
2. Add a Dockerfile and write the code to run
3. Build a Docker image: `docker build -t <image-name> .`
4. Run the container: `docker run -it <image-name>`. `-it` tags ensure that the code runs in an interactive terminal mode

*Task 2*
1. Run the command: `trivy image <image-name>`


**WHAT I LEARNED**
1. How to create a Dockerfile
2. How to build a Docker image and run a container
3. How to perform a Trivy scan

**REFERENCE MATERIAL**
https://www.youtube.com/watch?v=fqMOX6JJhGo&t=1636s
