from fastapi import HTTPException, status

UserAlredyExistExeption = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='User alredy exist'
)

IncorrectEmailOrPasswordExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Invalid email or password'
)

ExpiredTokenExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Expired token'
)

IncorrectTokenFormatExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Incorrect token format'
)

AbsentTokenExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='No token'
)

UserIsNotPresentExeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)