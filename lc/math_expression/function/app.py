import logging
import json

from algorithms.postfix import postfix
from algorithms.evaluate import evaluate_postfix_expression

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    body = event['body']
    LOGGER.info(body)

    # Load the expression. A string is technically valid json, so the expression will be understood as type String. 
    expression = json.loads(body)

    # Transform the infix expression to postfix. 
    postfix_expression = postfix(expression)

    # Evaluate the postfix expression and return a number. This number will then be type cast as an integer. 
    solution = int(evaluate_postfix_expression(postfix_expression))

    # The response body will contain the original expression, the postfix expression, and the solution. 
    body = {
        "expression": expression,
        "postfix": postfix_expression,
        "solution": solution
    }

    LOGGER.info(json.dumps(body))

    # API Gateway requires additional fields. The json body MUST be passed as a String. 
    response = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

    return response
