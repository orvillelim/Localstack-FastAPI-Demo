from aws_cdk import Stack, CfnOutput, App

from aws_cdk import aws_dynamodb as dynamodb
from constructs import Construct


class OrderTableStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the DynamoDB table for order details
        order_table = dynamodb.Table(
            self, "OrderTable",
            table_name="OrderTable",
            partition_key=dynamodb.Attribute(name="order_id", type=dynamodb.AttributeType.STRING),
            read_capacity=5,
            write_capacity=5
        )

        # Output the table name for reference
        output_table_name = CfnOutput(
            self, "OrderTableName",
            value=order_table.table_name,
            description="Name of the Order DynamoDB table"
        )


app = App()
OrderTableStack(app, "OrderTableStack")
