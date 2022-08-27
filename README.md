# aws-working-dir

### Working notes

I'd like to create a workable AWS environment for future development environments, with some serverless examples I can cite going into the future. I have my Account and User setup. Now, I'd like to configure aws sam and ECR. I'd like to have working examples using serverless resources like Lambda, API Gateway, SNS, and SQS. I'd also like to configure a simple Single Page Application (deployed in S3), and a simple container application (which could be deployed in ECS Fargate, but Lambda may be easier and more cost effective). 

Before starting, I will need to decide on my tools and overall strategy. I will use CloudFormation for now. Learning the CDK can come after some foundations have been laid. I'll use AWS CLI and SAM for deployment. Locally, I will develop with a WSL2 Ubuntu configuration. I'll use Python for serverless Lambda resources, Java for Web Apps, and React for Front End. I need to be able to build and test everything locally, so I will use Docker to build and test containers and serverless functions. 

Since I will be using SAM, my first step will be to create an S3 bucket for holding my SAM build resources. I will create the sam-bucket directory, and define my first CF Template for creating the bucket. Simple is good. 

