# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, MetaData, String, Table
from database.database import Base


metadata = Base.metadata


t_vendor_parts = Table(
    'vendor_parts', metadata,
    Column('vendor_id', ForeignKey('vendors.vendor_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    Column('part_id', ForeignKey('parts.part_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
)

print('Models 3')
