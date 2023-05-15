from fastapi import FastAPI

from app.booking.router import router as router_booking


app = FastAPI()

app.include_router(router_booking)

@app.get('/')
def test():
    return {'msg': 'hellow there'}
