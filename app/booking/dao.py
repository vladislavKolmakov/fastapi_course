from sqlalchemy import select

from app.database import async_session_maker
from app.booking.models import Booking
from app.dao.dase import BaseDAO


class BookingDAO(BaseDAO):
    model = Booking