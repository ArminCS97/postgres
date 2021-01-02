# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, MetaData, String, Table
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from database.database import Base


metadata = Base.metadata



class Part(Base):
    __tablename__ = 'parts'
    __table_args__ = {'extend_existing': True}

    part_id = Column(Integer, primary_key=True, server_default=FetchedValue())
    part_name = Column(String(255), nullable=False)
    part_desc = Column(String(255), nullable=False, default='Hi')
    part_score = Column(Integer, nullable=True)

    vendors = relationship('Vendor', secondary='vendor_parts', backref='parts')

print('Models 1')

