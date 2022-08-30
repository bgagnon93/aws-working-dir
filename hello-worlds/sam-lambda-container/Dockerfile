FROM public.ecr.aws/lambda/python:3.8
COPY function/ ./
RUN pip3 install -r requirements.txt && \
    chmod -R 755 .

CMD [ "app.lambda_handler" ]