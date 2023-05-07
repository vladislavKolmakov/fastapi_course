from fastapi import APIRouter

from app.booking.schemas import SBooking
from app.booking.dao import BookingDAO

router = APIRouter(
    prefix='/booking',
    tags=['Booking'],
)

@router.get('')
async def get_booking() -> list[SBooking]:
        return await BookingDAO.find_all()

@router.get('')
async def get_booking() -> SBooking:
        return await BookingDAO.find_one_or_none(room_id=7)
