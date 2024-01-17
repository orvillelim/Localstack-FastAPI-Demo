from functools import lru_cache

from fastapi import FastAPI

from aws import ses_service

# Project Framework settings
from core import settings

# Endpoints router
from endpoints.order import order_endpoints

app = FastAPI()

# Include the orders router
app.include_router(order_endpoints.router, prefix="/api")

@lru_cache
def get_settings():
    return settings.Settings()
