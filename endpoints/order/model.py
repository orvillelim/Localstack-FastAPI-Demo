from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, field_validator
from pydantic import validator


class Recipient(BaseModel):
    first_name: str
    last_name: str
    address: str
    phone_number: str
    email: str


class BillingInformation(BaseModel):
    first_name: str
    last_name: str
    address: str
    phone_number: str
    email: str


class OrderDetail(BaseModel):
    order_id: Optional[str]
    status: str | None = None
    product_name: str
    quantity: int
    price: float
    order_date: datetime
    recipient: Recipient
    billing_information: BillingInformation

    @field_validator("price")
    def convert_price(cls, v, values):
        if type(v) != float:
            raise ValueError("Invalid value price, must be float")

        price = round(Decimal(v), 2)
        return price

    @field_validator("order_date")
    def validate_order_date(cls, v, values):
        date_time = v.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time
