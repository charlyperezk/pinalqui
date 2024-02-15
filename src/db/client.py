# External
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

# Internal
from src.utils.exceptions import DataBaseError

# Code
class DataBaseClient:

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, object) -> None:
        try:
            self._session.add(object)
            self._session.commit()
        except Exception as e:
            raise DataBaseError(e)

    def last(self, object):
        try:
            data = self._session.query(object).order_by(object.id.desc()).first()
            self.session_commit()
            return data
        except Exception as e:
            raise DataBaseError(e)

    def get_all(self, object):
        try:
            data = self._session.query(object).all()
            return data
        except Exception as e:
            raise DataBaseError(e)

    def get_all_by_id(self, object, id):
        try:
            data = self._session.query(object).filter_by(user_id=id).all()
            return data
        except NoResultFound:
            return None
        except Exception as e:
            raise DataBaseError(e)

    def get_by_id(self, object, id):
        try:
            data = self._session.query(object).filter_by(id=id).one()
            return data
        except NoResultFound:
            return None
        except Exception as e:
            raise DataBaseError(e)
        
    def session_commit(self) -> None:
        self._session.commit()
