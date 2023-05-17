from fastapi import FastAPI

from app.booking.router import router as router_booking
from app.user.router import router as router_user


app = FastAPI()

app.include_router(router_user)
app.include_router(router_booking)

@app.get('/')
def test():
    return {'msg': 'hellow there'}
