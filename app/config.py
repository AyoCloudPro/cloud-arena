from datetime import datetime, timezone
from dotenv import load_dotenv

import os

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Cloud Arena")
    CLOUD_PROVIDER: str = os.getenv("CLOUD_PROVIDER", "LOCAL")
    REGION: str = os.getenv("REGION", "DEV")
    VERSION: str = os.getenv("VERSION", "0.1.0")
    BUILD_NUMBER: str = os.getenv("BUILD_NUMBER", "DEV")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "DEV")
    DOCKER_IMAGE: str = os.getenv("DOCKER_IMAGE", "cloud-arena:local")

    START_TIME = datetime.now(timezone.utc)

settings = Settings()
