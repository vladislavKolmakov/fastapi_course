from fastapi import APIRouter, Depends

from app.booking.schemas import SBooking
from app.booking.dao import BookingDAO
from app.user.dependencies import get_current_user
from app.user.models import Users

router = APIRouter(
    prefix='/booking',
    tags=['Booking'],
)

# @router.get('')
# async def get_booking() -> list[SBooking]:
#         return await BookingDAO.find_all()

# @router.get('')
# async def get_booking() -> SBooking:
#         return await BookingDAO.find_one_or_none(room_id=7)

@router.get('/')
async def get_bookings(user: Users = Depends(get_current_user)):
        # print(user, type(user), user.email)
        return await BookingDAO.find_all(user_id=1)
