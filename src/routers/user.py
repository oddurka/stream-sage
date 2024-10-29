import logging

from fastapi import APIRouter, HTTPException, status

from src.models.user import UserIn
from src.security import authenticate_user, create_access_token, get_password_hash, get_user
from src.database import database, user_table

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/register", status_code=201)
async def register(user: UserIn):
    if await get_user(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    hashed_password = get_password_hash(user.password)
    query = user_table.insert().values(email=user.email, password=hashed_password)

    logger.debug(query)

    await database.execute(query)
    return {"detail": "User registered"}

@router.get("/token")
async def login(user: UserIn):
    user = await authenticate_user(user.email, user.password)
    access_token = create_access_token(user.email)
    return {"access_token": access_token, "token_type": "bearer"}