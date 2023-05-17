from app.dao.dase import BaseDAO
from app.user.models import Users

class UserDAO(BaseDAO):
    model = Users