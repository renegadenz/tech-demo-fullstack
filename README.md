# Tech Demo - Work in progress

## Intro
This is a full stack cloudformation deployment that covers both backend and frontend infrastructure required to host Microservices and Static Content. On top of the infrasructure deployments I have put together a CI/CD workflow using AWS Tooling such as AWS code pipeline, Code Build, and Code Commit. 

At some point, I may add Observability and logging to theis builtent but for now, this deployment is kept simple as there is quite a lot of infrastructure as code that has been created for this simple website and backend.

The front end is build on html with basic css. This is purely to test the workflow of the infrsatructure. Again for the backend we have a very simple flask based python application I've also setup swagger for the api gateway integration.

## Cloudformation Deployments
The cloud formation deployments have been broken up into core, backend, and frontend deployments and API gateway

* The core represents the core components which will be the Elastic Container Service Cluster and the Application Load balancer. This will need to be deployed first.
* Frontend hosts the Frontend cloudformation templates that are used to deploy cloudfront and S3 bucket that will host the website. The deploymment also as a CI/CD aspect to it. THe idea is developer will use code commit to store their code which will trigger code pipeline to deploy onto S3. 
* Backend this deploys the ecs service and alb context routing along with the pipeline that builds and deploys the container to ECS
* Fially we have the api gateway configuration which we take swagger file and deploy the api gateway configuration that will integrate the frontend and backend together.

Conceptually we are covering both backend and front end infrastructure deployments, CI/CD workflow to manage our code and code deployments and api gateway.

Below is a diagram illustrating the outcome.
### Diagram

![Diagram](doc/Fullstack-demo-Diagram.png)


Please note this is purely a demo I wouldn't expect anyone to have a such complex infrastructure for a simple hello world app. I may expand this deployment at a future date.