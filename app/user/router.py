from fastapi import APIRouter, HTTPException, Response, status
from app.user.schemas import SUserAuth
from app.user.dao import UserDAO
from app.user.auth import get_password_hash, authentificate_user, create_access_token

router = APIRouter(
    prefix='/auth',
    tags=['Auth & Users']
)


@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    user = await authentificate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('booking_access_token', access_token, httponly=True)
    return access_token
    