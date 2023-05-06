import json
import boto3
from botocore.exceptions import ClientError
import os
import requests  # We use the requests module to make a HTTP GET request to the Secrets Manager Lambda extension: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_lambda.html

secret_name = os.environ.get('SECRET_NAME')
secrets_extension_http_port = os.environ.get(
    'PARAMETERS_SECRETS_EXTENSION_HTTP_PORT')
aws_session_token = os.environ.get('AWS_SESSION_TOKEN')

secrets_extension_endpoint = "http://localhost:" + \
    secrets_extension_http_port + "/secretsmanager/get?secretId=" + secret_name
headers = {'X-Aws-Parameters-Secrets-Token': f'{aws_session_token}'}


def lambda_handler(event, context):

    r = requests.get(secrets_extension_endpoint, headers=headers)

    # We use json.loads to parse our secret and account for special characters that may be in our secret and decode them.
    secret = json.loads(r.text)["SecretString"]

    # We print our secret for demonstration purposes. Remove this line in your production systems!
    print(secret)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "secret": secret,
            }
        ),
    }



# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/




def get_secret():

    secret_name = "emails"
    region_name = "eu-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    # Your code goes here.
