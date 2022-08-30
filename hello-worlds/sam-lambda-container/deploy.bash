# Login
aws ecr --profile admin get-login-password | docker login --username AWS --password-stdin 983510677257.dkr.ecr.us-east-1.amazonaws.com

# Build Image
docker build -t 983510677257.dkr.ecr.us-east-1.amazonaws.com/hello-lambda-container:dev .

# Push Image to ECR
docker push 983510677257.dkr.ecr.us-east-1.amazonaws.com/hello-lambda-container:dev

# sam build
sam build

# sam package
sam package --image-repository "983510677257.dkr.ecr.us-east-1.amazonaws.com/hello-lambda-container" --output-template-file packaged.yml

# Update packaged.yml with unique image uri
imageId=`docker inspect --format='{{index .RepoDigests 0}}' 983510677257.dkr.ecr.us-east-1.amazonaws.com/hello-lambda-container:dev`
sed -i "s|Ref: ImageURI.*|\"$imageId\"|" packaged.yml

# Deploy with CloudFormation
sam deploy --template packaged.yml --s3-bucket sam-resources-bucket --profile admin