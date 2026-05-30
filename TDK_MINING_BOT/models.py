from sqlalchemy import *

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    telegram_id = Column(String)

    username = Column(String)

    balance = Column(Float, default=0)

    mining_balance = Column(Float, default=0)

    wallet = Column(String)

    mining_active = Column(Boolean, default=True)

    last_mine_time = Column(BigInteger)