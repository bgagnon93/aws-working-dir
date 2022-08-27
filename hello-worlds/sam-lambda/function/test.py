from app import lambda_handler

msg = lambda_handler("event!", None)
print(msg)