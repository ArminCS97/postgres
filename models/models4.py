# coding: utf-8
from sqlalchemy import Column, ForeignKey, LargeBinary, String

from database.database import Base
from models.models1 import Part

metadata = Base.metadata

# When you add a row to the child class, the parent class also gets this row
class PartDrawing(Part):
    __tablename__ = 'part_drawings'

    part_id = Column(ForeignKey('parts.part_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    file_extension = Column(String(5), nullable=False)
    drawing_data = Column(LargeBinary, nullable=False)
    part_drawing_score = Column(String(5), nullable=True)

print('Models 4')
