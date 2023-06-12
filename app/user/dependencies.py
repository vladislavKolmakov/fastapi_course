from datetime import datetime
from fastapi import Request, status, HTTPException, Depends
from jose import JWTError, jwt
from app.user.dao import UserDAO

from app.config import settings

def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='111')
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='222')
    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id: str = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await UserDAO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user