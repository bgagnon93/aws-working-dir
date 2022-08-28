The certificate for orange-lightning.com:

```
aws cloudformation create-stack --template-body file://template.yml --stack-name orange-lightning-certificate --profile admin
```

After initializing the creation of this certificate, I had to navigate to the [AWS Certificate Manager](https://us-east-1.console.aws.amazon.com/acm/home?region=us-east-1#/certificates/list) and create a new record with the provided DNS details. This was straightforward, because the "Create records in Route 53" button in the Certificate resource in the Certificate Manager Console mapped those details for me. 