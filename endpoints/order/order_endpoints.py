import logging
from typing import List

# FastAPI related imports
from fastapi import APIRouter

# model
from .model import OrderDetail

# Project imports
from aws import ses_service, dynamoDB_service

router = APIRouter()


@router.post("/orders/")
async def create_order_api(payload: dict):
    """
    Create a new order and send email notification
    """

    order_detail = OrderDetail(**payload)
    order_detail.status = 'CREATE_ORDER'
    response = ses_service.send_email(order_detail.billing_information.email,
                                      order_detail.recipient.email,
                                      "test subject",
                                      "test body")

    if response.get('ResponseMetadata').get('HTTPStatusCode') == 200:
        print('Error sending email notification with response: {}'
              .format(response.get('ResponseMetadata')))

    record = dynamoDB_service.create_order_details(order_detail)

    return record


@router.get("/orders/", response_model=List[OrderDetail])
async def get_orders():
    """
    Get all orders for the authenticated user.
    """
    return
