from datetime import datetime
from fastapi import Request, Depends
from jose import JWTError, jwt
from app.exeptions import AbsentTokenExeption, ExpiredTokenExeption, IncorrectTokenFormatExeption, UserIsNotPresentExeption
from app.user.dao import UserDAO

from app.config import settings

def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise AbsentTokenExeption
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except:
        raise IncorrectTokenFormatExeption
    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise ExpiredTokenExeption
    user_id: str = payload.get('sub')
    if not user_id:
        raise UserIsNotPresentExeption
    user = await UserDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentExeption

    return user