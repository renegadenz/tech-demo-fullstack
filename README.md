# Tech Demo - WIP

Flask app: A basic Flask app with Swagger and Prometheus metrics that runs in a Docker container. It includes a simple frontend that consumes the Flask app via AJAX. The app is deployed to an EC2 instance or an ECS service, depending on the deployment model you choose.

Static content: The static content for the frontend, which includes HTML, CSS, and JavaScript files. The static content is stored in an S3 bucket and served via CloudFront.

CloudFormation templates: The CloudFormation templates that create and manage the infrastructure for the Flask app and the static content. The templates include the following:

Root stack: A top-level CloudFormation stack that orchestrates the deployment of all the resources required for the Flask app and the static content. This stack includes references to the nested stacks that create the individual resources.
ALB stack: A nested CloudFormation stack that creates an Application Load Balancer to route traffic to the Flask app or the static content.
ECS stack: A nested CloudFormation stack that creates an ECS cluster, an ECS service, and an Auto Scaling Group to run the Flask app in Docker containers. If you choose the EC2 deployment model, this stack also includes a Launch Configuration to define the EC2 instance configuration. If you choose the ECS deployment model, this stack includes an ECS task definition to define the Docker container configuration.
Launch Template stack: A nested CloudFormation stack that creates a Launch Template to define the EC2 instance configuration for the ECS stack.
CodePipeline: A pipeline that deploys the Flask app to an EC2 instance or an ECS service. The pipeline includes the following stages:

Source: Connects to the CodeCommit repository that contains the Flask app code as the source.
Build: Uses CodeBuild to build the Docker image and push it to ECR.
Deploy: Uses the ECS deploy action to deploy the new Docker image to the ECS service or an EC2 instance.
This setup allows for a fully automated deployment pipeline, from code commit to running the Flask app in production.