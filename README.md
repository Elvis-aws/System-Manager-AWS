
# How it works


# Activate Virtual env
    # virtualenv env
    # source env/bin/activate
    # pip3 install -r requirements.txt
    # pip3 freeze > requirements.txt
    # deactive


# Run api locally
- sam build
- sam local start-api
- If you get docker error, simply run "docker logout public.ecr.aws"

# Deployment Instructions
1. activate virtual env
2. sam build
3. sam deploy --guided

During the prompts:
  * Enter a stack name
  * Enter the desired AWS Region
  * Enter a bucket name
  * Allow SAM CLI to create IAM roles with the required permissions.


# Making Changes
1. sam build
2. sam deploy

# Pay Load
 

==============================================
Commands
==============================================
sam build
sam delete
sam deploy
sam init
sam list
sam local generate-event
sam local invoke
sam local start-api
sam local start-lambda
sam logs
sam package
sam pipeline bootstrap
sam pipeline init
sam publish
sam sync
sam traces
sam validate