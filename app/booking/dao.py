from app.database import async_session_maker

from app.booking.models import Booking
from sqlalchemy import select


class BookingDAO:
    
    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(Booking)
            bookings = await session.execute(query)
            return bookings.scalars().all()