# aws-working-dir

### Working notes

I'd like to create a workable AWS environment for future development environments, with some serverless examples I can cite going into the future. I have my Account and User setup. Now, I'd like to configure aws sam and ECR. I'd like to have working examples using serverless resources like Lambda, API Gateway, SNS, and SQS. I'd also like to configure a simple Single Page Application (deployed in S3), and a simple container application (which could be deployed in ECS Fargate, but Lambda may be easier and more cost effective). 

Before starting, I will need to decide on my tools and overall strategy. I will use CloudFormation for now. Learning the CDK can come after some foundations have been laid. I'll use AWS CLI and SAM for deployment. Locally, I will develop with a WSL2 Ubuntu configuration. I'll use Python for serverless Lambda resources, Java for Web Apps, and React for Front End. I need to be able to build and test everything locally, so I will use Docker to build and test containers and serverless functions. 

Since I will be using SAM, my first step will be to create an S3 bucket for holding my SAM build resources. I will create the sam-bucket directory, and define my first CF Template for creating the bucket. Simple is good. 

### August 27
Today, I configured my local WSL environment with docker, aws cli 2, sam, and git. Then I deployed a basic Lambda function, and configured a basic API Gateway. Finally, I purchased a domain, and set up that API to use the Custom Domain. 

Tomorrow, I'd like to move my testing training app to S3. I will handle those updates in that repository, instead of this one. I'll set up a simple sam deployment solution. I'd also like to remove the "required" fields from the first page. This will make that application easier to demo. I may also look into buying another domain. I'm still trying to come up with something more professional, but all my first picks are taken. 

### August 28
Today, I moved the test training app to S3. I renamed it "policytrainer", since I felt this would be clearer to any readers. I made all of those changes in the [testing-training-app](https://github.com/bgagnon93/testing-training-app) repo. I was able to achieve all of my objectives for today, including a decision on a domain. With every variation of bgagnon taken, I opted for gagnonagon.com. Brings me back. 

I set up a simple sam deployment solution which orchestrates the creation of an S3 bucket, a CloudFront distribution, and a Route 53 record set which invokes the CloudFront endpoint. CloudFront also includes the certificate I created, and re-routes to https when users attempt to launch the policytrainer with http. I also removed the check for required fields on the first page, so the app will be easier to demo. Lastly, I threw together a quick architecture diagram for that solution:

<img src="https://user-images.githubusercontent.com/38666646/187100897-783ebf0d-13b6-480f-b750-ea4fb04945b8.png" alt="training-app-architecture" width="500">

Tomorrow's the start of the work week, so I'm skeptical I'll be able to keep this momentum up. That said, I'd like to try building a video or music playback service. A 'login' service could also be cool - how would I go about setting up a simple DB for authenticating preferences. Maybe I really could build that Planit Poker site. Or even a retro board. 
