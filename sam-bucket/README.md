The S3 bucket in this location may be deployed, updated, and changed with the following:

```
aws cloudformation create-stack --template-body file://template.yml --stack-name sam-resources-bucket --profile admin
```