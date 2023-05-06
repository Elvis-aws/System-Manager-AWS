import json
import boto3
from botocore.exceptions import ClientError
import os
import \
    requests

secret_name = os.environ.get('SECRET_NAME')
secrets_extension_http_port = os.environ.get(
    'PARAMETERS_SECRETS_EXTENSION_HTTP_PORT')
aws_session_token = os.environ.get('AWS_SESSION_TOKEN')

secrets_extension_endpoint = "http://localhost:" + \
                             secrets_extension_http_port + "/secretsmanager/get?secretId=" + secret_name
headers = {'X-Aws-Parameters-Secrets-Token': f'{aws_session_token}'}


def lambda_handler(event, context):
    r = requests.get(secrets_extension_endpoint, headers=headers)

    secret = json.loads(r.text)["SecretString"]

    print(secret)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "secret": secret,
            }
        ),
    }


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

        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    # Your code goes here.
