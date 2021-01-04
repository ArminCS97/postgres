# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, MetaData, String, Table
from sqlalchemy.schema import FetchedValue
from database.database import Base

metadata = Base.metadata


class Vendor(Base):
    __tablename__ = 'vendors'
    # __table_args__ = {'extend_existing': True}

    vendor_id = Column(Integer, primary_key=True, server_default=FetchedValue())
    vendor_name = Column(String(255), nullable=False)
    vendor_score = Column(String(5), nullable=True)


print('Models 2')