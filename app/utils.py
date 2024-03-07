from fastapi import Depends
from sqlalchemy.orm import Session
from jose import jwt

import settings
from db_initializer import get_db
from app.services import users as user_db_services

def decode_jwt(jwt_token:str, session:Session=Depends(get_db)):
    try:
        decoded_data = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        return user_db_services.get_user(session=session, email=decoded_data['email'])
    except jwt.ExpiredSignatureError:
        print("JWT token has expired.")
    except jwt.InvalidTokenError:
        print("Invalid JWT token.")