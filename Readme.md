### Overview

This application was created for the purpose of experimenting with LocalStack, The inspiration was to
create a simple REST API ordering system with FastAPI

### AWS service used with Localstack

| Environment      | AWS                       |
|------------------|---------------------------|
| **Services**     | DynamoDB, SES             |
| **Integrations** | AWS SDK, AWS CLI, AWS CDK |
| **Categories**   | Fast API                  |
| **Works on**     | LocalStack v3             |

### Prerequisites

- Docker
- [Localstack](https://github.com/localstack/localstack)
- Python 3.10+
- npm
- pip

### Setup

```bash
# Install dependencies
pip install -r requirements.txt

# setup aws configuration see
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export AWS_ENDPOINT_URL=http://0.0.0.0:4566
export AWS_REGION=us-east-1
```

### Create a dynamoDB table

```bash
# Install CDK dependencies
npm install -g aws-cdk-local aws-cdk

# CDK Boostrap and deploy
cd ./aws/cdk-devops
pip install -r requirements.txt
cdklocal bootstrap
cdklocal deploy
```

```bash
# start the app
uvicorn main:app --reload --port 8000
```

### cURL test

```cUrl
curl -X POST --location "http://127.0.0.1:8000/api/orders/" \
  -H "Content-Type: application/json" \
  -d '{
    "order_id": "123456789",
    "product_name": "Sample Product",
    "quantity": 2,
    "price": 25.341,
    "order_date": "2024-01-11T08:30:00",
    "recipient": {
      "first_name": "John",
      "last_name": "Doe",
      "address": "123 Main St",
      "phone_number": "+1234567890",
      "email": "john.doe@example.com"
    },
    "billing_information": {
      "first_name": "John",
      "last_name": "Doe",
      "address": "123 Main St",
      "phone_number": "+1234567890",
      "email": "john.doe@example.com"
    }
  }'
```

### View Items:
`$ aws dynamodb scan  --table-name OrderTable`

```json
{
    "Items": [
      {
        "billing_information": {
          "M": {
            "last_name": {
              "S": "Doe"
            },
            "phone_number": {
              "S": "+1234567890"
            },
            "address": {
              "S": "123 Main St"
            },
            "first_name": {
              "S": "John"
            },
            "email": {
              "S": "john.doe@example.com"
            }
          }
        },
        "order_date": {
          "S": "01/11/2024, 08:30:00"
        },
        "quantity": {
          "N": "2"
        },
        ...
```

### Localstack logs
