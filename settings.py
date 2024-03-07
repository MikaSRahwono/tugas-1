import os
import secrets

# Database url configuration
DATABASE_URL = "postgresql://{username}:{password}@{host}:{port}/{db_name}".format(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    db_name=os.getenv("POSTGRES_DB"),
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)
SECRET_KEY = secrets.token_urlsafe(32)