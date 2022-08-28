# aws-working-dir

### Working notes

I'd like to create a workable AWS environment for future development environments, with some serverless examples I can cite going into the future. I have my Account and User setup. Now, I'd like to configure aws sam and ECR. I'd like to have working examples using serverless resources like Lambda, API Gateway, SNS, and SQS. I'd also like to configure a simple Single Page Application (deployed in S3), and a simple container application (which could be deployed in ECS Fargate, but Lambda may be easier and more cost effective). 

Before starting, I will need to decide on my tools and overall strategy. I will use CloudFormation for now. Learning the CDK can come after some foundations have been laid. I'll use AWS CLI and SAM for deployment. Locally, I will develop with a WSL2 Ubuntu configuration. I'll use Python for serverless Lambda resources, Java for Web Apps, and React for Front End. I need to be able to build and test everything locally, so I will use Docker to build and test containers and serverless functions. 

Since I will be using SAM, my first step will be to create an S3 bucket for holding my SAM build resources. I will create the sam-bucket directory, and define my first CF Template for creating the bucket. Simple is good. 

### August 27
Today, I configured my local WSL environment with docker, aws cli 2, sam, and git. Then I deployed a basic Lambda function, and configured a basic API Gateway. Finally, I purchased a domain, and set up that API to use the Custom Domain. 

Tomorrow, I'd like to move my testing training app to S3. I will handle those updates in that repository, instead of this one. I'll set up a simple sam deployment solution. I'd also like to remove the "required" fields from the first page. This will make that application easier to demo. I may also look into buying another domain. I'm still trying to come up with something more professional, but all my first picks are taken. 