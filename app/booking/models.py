from sqlalchemy import JSON, Column, Computed, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey('rooms.id'))
    user_id = Column(ForeignKey('users.id'))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_coast = Column(Integer, Computed('(date_to - date_from) * price'))
    total_coast = Column(Integer, Computed('date_from - date_from'))

    # user = relationship('Users', back_populates='booking')
    # room = relationship('Room', back_populates='booking')

    # def __str__(self):
    #     return f'Booking #{self.id}'