from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "TradePilot AI"
    VERSION: str = "1.0.0"

    UPSTOX_CLIENT_ID: str = ""
    UPSTOX_CLIENT_SECRET: str = ""
    UPSTOX_REDIRECT_URI: str = ""
    UPSTOX_ACCESS_TOKEN: str = ""

    class Config:
        env_file = ".env"


settings = Settings()