from flask import jsonify, Blueprint
from models import PartDrawing
from database.database import DatabaseSession

part_drawings_blueprint = Blueprint('Part Drawings', __name__)

@part_drawings_blueprint.route('/part-drawing')
def add():
    part_drawing1 = PartDrawing(part_id=45, file_extension='.exe1', drawing_data=bytes(1), part_name='Part Cool1')
    part_drawing2 = PartDrawing(part_id=67, file_extension='.exe2', drawing_data=bytes(2), part_name='Part Cool1')

    DatabaseSession.add(part_drawing1)
    DatabaseSession.add(part_drawing2)
    DatabaseSession.commit()

    return True
