from datetime import date
from fastapi import APIRouter, Depends

from app.booking.schemas import SBooking
from app.booking.dao import BookingDAO
from app.user.dependencies import get_current_user
from app.user.models import Users
from app.exeptions import RoomCanNotBeBooked

router = APIRouter(
    prefix='/booking',
    tags=['Booking'],
)


@router.get('/')
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
        # print(user, type(user), user.email)
        return await BookingDAO.find_all(user_id=1)


@router.post('')
async def add_booking(
        room_id: int, date_from: date, date_to: date,
        user: Users = Depends(get_current_user),
    ): 
        booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
        if not booking:
            raise RoomCanNotBeBooked
