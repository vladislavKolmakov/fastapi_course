from sqlalchemy import select

from app.database import async_session_maker


class BaseDAO:
    model = None

    # @classmethod
    # async def find_one_or_none(cls, **filter):
    #     async with async_session_maker() as session:
    #         query = select(cls.model.__table__.columns).filter_by(**filter)
    #         result = await session.execute(query)
    #         return result.mappings().one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter)
            result = await session.execute(query)
            return result.mappings().one_or_none()


    @classmethod
    async def find_all(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter)
            result = await session.execute(query)
            return result.mappings().all()