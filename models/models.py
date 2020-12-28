# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, MetaData, String, Table
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from database.database import Base


metadata = Base.metadata



class Part(Base):
    __tablename__ = 'parts'

    part_id = Column(Integer, primary_key=True, server_default=FetchedValue())
    part_name = Column(String(255), nullable=False)
    part_desc = Column(String(255), nullable=False, default='Hi')
    part_score = Column(Integer, nullable=True)

    vendors = relationship('Vendor', secondary='vendor_parts', backref='parts')


class PartDrawing(Part):
    __tablename__ = 'part_drawings'

    part_id = Column(ForeignKey('parts.part_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    file_extension = Column(String(5), nullable=False)
    drawing_data = Column(LargeBinary, nullable=False)



t_vendor_parts = Table(
    'vendor_parts', metadata,
    Column('vendor_id', ForeignKey('vendors.vendor_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    Column('part_id', ForeignKey('parts.part_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
)



class Vendor(Base):
    __tablename__ = 'vendors'

    vendor_id = Column(Integer, primary_key=True, server_default=FetchedValue())
    vendor_name = Column(String(255), nullable=False)
