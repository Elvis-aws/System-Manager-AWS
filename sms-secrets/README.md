# Secrets Manager Lambda Extension
The AWS SAM template deploys a Lambda function in Python with the Secrets Manager Lambda extension.

## Testing

Run the following Lambda CLI invoke command to invoke the function. Edit the {GetSecretFunction} placeholder with the 
ARN of the deployed Lambda function. This is provided in the stack outputs.
View the secret in the function logs, edit the {stack-name} which you entered when deploying the stack.

```bash
aws lambda invoke --function-name {GetSecretFunction ARN} --cli-binary-format raw-in-base64-out response.json
sam logs --stack-name {stack-name}
```

## Cleanup

1. Delete the stack, Enter `Y` to confirm deleting the stack and folder.

```bash
sam delete
```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
