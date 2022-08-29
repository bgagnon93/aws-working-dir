To build the Lambda Function, run the command:

```
sudo sam build
```

To test the function locally, run the below command (customize the sample-request as desired):
```
sam local invoke --event function/sample-request.json
```

To deploy the Lambda Function, run:

```
sam deploy --s3-bucket sam-resources-bucket --profile admin
```

This Function is coupled with a Serverless API. The API uses a Custom Domain, and can be invoked with a POST request to https://lambda.orange-lightning.com.

I should replace this with a simple GET request so it can be accessed from the browser...

## Architecture
<img src="https://user-images.githubusercontent.com/38666646/187108756-7a875759-41e2-4dd6-a71d-83d721de5a38.png" alt="training-app-architecture" width="500">
