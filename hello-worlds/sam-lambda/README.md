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