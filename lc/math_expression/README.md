### Evaluate a mathematical expression passed as a String

This challenge may be broken down into two steps. First, I should convert the expression into a 'postfix' expression. Second, I evaluate the postfix expression, and return an answer. 

To solve this problem, I brought in both the stack and queue data structure classes from the data structures course I took recently. I then created two independent python scripts for generating the postfix expression and evaluating it. These could be joined in one class, but I figure this is a small module. It makes sense to me to split them out so I may work on them independently. Below is the file structure:

```bash
├── function
│   ├── app.py
│   ├── algorithms
│   │   ├── postfix.py
│   │   ├── evaluate.py
│   ├── data_structures
│   │   ├── queue.py
│   │   ├── stack.py
├── test
│   ├── evaluate_test.py
│   ├── postfix_test.py
├── template.yml
├── samconfig.toml
├── README.md
```

I was excited to empower end users to pass a query parameter to be evaluated, but that's not going to play nicely when put in a url. Instead, I'll set up a simple POST service. 

### Test, Build, and Deploy

With pytest installed, run the following command in this directory:
```
pytest test
```

To build the Lambda Function, run the command:

```
sudo sam build
```

To test the function locally, the docker daemon must be running in the background. Then run the below command (customize the sample-request as desired):
```
sam local invoke --event function/sample-request.json
```

To deploy the Lambda Function, run:

```
sam deploy --s3-bucket sam-resources-bucket --profile admin
```

This Function is coupled with a Serverless API. The API uses a Custom Domain, and can be invoked with a POST request to https://mathexpression.gagnonagon.com.

A curl command in the terminal may also be used to invoke the function. 

```bash
curl -X POST https://mathexpression.gagnonagon.com -H 'Content-Type: application/json' -d '"14+3*10^2/5-61"'
```

## Architecture
<img src="https://user-images.githubusercontent.com/38666646/187108756-7a875759-41e2-4dd6-a71d-83d721de5a38.png" alt="training-app-architecture" width="500">
