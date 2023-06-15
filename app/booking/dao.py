from datetime import date
from sqlalchemy import func, select, and_, or_

from app.database import async_session_maker
from app.booking.models import Booking
from app.dao.dase import BaseDAO
from app.hotels.rooms.models import Rooms
from app.database import engine


class BookingDAO(BaseDAO):
    model = Booking

    @classmethod
    async def add(
        cls,
        user_id: int,
        room_id: int,
        date_from: date,
        date_to: date
        ):
        async with async_session_maker() as session:
            booked_rooms = select(Booking).where(
                and_(
                    Booking.room_id == 1,
                    or_(
                        and_(
                            Booking.date_from >= date_from,
                            Booking.date_to <= date_to
                        ),
                        and_(
                            Booking.date_from <= date_from,
                            Booking.date_to > date_from
                        ),
                    )
                )
            ).cte('booked_rooms')

            rooms_left = select(
                (Rooms.quantity - func.count(booked_rooms.c.room_id)).label('rooms_left')
                ).select_from(Rooms).join(
                    booked_rooms, booked_rooms.c.room_id == Rooms.id
                ).where(Rooms.id == room_id).group_by(
                    Rooms.quantity, booked_rooms.c.room_id
                )
            
            print(rooms_left.compile(engine, compile_kwargs={'literal_binds': True}))

            rooms_left = await session.execute(rooms_left)
            print(rooms_left.scalar())