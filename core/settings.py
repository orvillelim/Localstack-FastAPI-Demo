from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_ENDPOINT_URL: str
    AWS_REGION_NAME: str

    class Config:
        env_file = './.env'