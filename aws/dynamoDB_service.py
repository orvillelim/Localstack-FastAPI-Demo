import json

import boto3

from core.settings import Settings

settings = Settings()

ddb = boto3.resource('dynamodb',
                     endpoint_url=settings.AWS_ENDPOINT_URL,
                     region_name=settings.AWS_REGION_NAME,
                     aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                     aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

from endpoints.order.model import OrderDetail

# DynamoDB table name
table_name = "OrderTable"


def create_order_details(order_detail: OrderDetail):
    # Get the DynamoDB table
    table = ddb.Table(table_name)

    # Put the item into the table
    response = table.put_item(Item=order_detail.model_dump())
    return response
