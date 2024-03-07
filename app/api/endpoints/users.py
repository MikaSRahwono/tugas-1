from fastapi import Body, Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Dict

from db_initializer import get_db
from app.models import users as user_model
from app.services import users as user_db_services
from app.schemas.users import CreateUserSchema, UserSchema, UserLoginSchema
from app.utils import decode_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/login")
router = APIRouter()

@router.post('/signup', response_model=UserSchema)
def signup(
    payload: CreateUserSchema = Body(), 
    session:Session=Depends(get_db)
):
    payload.hashed_password = user_model.User.hash_password(payload.hashed_password)
    return user_db_services.create_user(session, user=payload)

@router.post('/login', response_model=Dict)
def login(
        payload: OAuth2PasswordRequestForm = Depends(),
        session: Session = Depends(get_db)
    ):
    try:
        user:user_model.User = user_db_services.get_user(
            session=session, email=payload.username
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    is_validated:bool = user.validate_password(payload.password)
    if not is_validated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    return user.generate_token()

@router.get("/profile")
def profile(account=Depends(decode_jwt)) -> UserSchema:
    """Get authenticated account"""
    return account