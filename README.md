# pyScraper
This is a simple Python API implemented using Flask, Beautiful Soup and MongoDB. It receives a url and return information about the product displayed. 

## Installation
### Approach 1
Inside the project file, there is a Dockerfile that can be used to build a docker image containing the project and all its dependencies using the command `docker build -t pyScraper`. Once the build is finished, you can then run the container using the port parameters you want. 
You will also need a container with a MongoDB image 4.6.8. To do so, just run the following command: ``


### Approach 2
I tried to implement a docker compose approach in order to avoid dealing with various containers, but could not debug the eventual errors that popped up. I'll leave the file here anyways as I'll be coming back to this soon to correct it.

## REST API
### Request
  `GET /scrape?<url>`
##Expected Return:
  
## Development

The project folder structure was based on previous experiences, separating responsibilities and business rules.
The project was tested using Amazon desktop urls, here are some examples:

