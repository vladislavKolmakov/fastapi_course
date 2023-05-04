from fastapi import APIRouter

from app.booking.dao import BookingDAO

router = APIRouter(
    prefix='/booking',
    tags=['Booking'],
)

@router.get('')
async def get_booking():
        return await BookingDAO.find_all()