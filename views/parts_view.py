from flask import jsonify, Blueprint

from database.database import DatabaseSession
from models.models import Part, PartDrawing, Vendor

parts_blueprint = Blueprint('Parts', __name__)

@parts_blueprint.route('/part/add')
def add():
    # First add a new part
    part = Part(part_name='Part')
    DatabaseSession.add(part)
    DatabaseSession.commit()

    # Then get all of them
    parts = Part.query.all()
    parts_list = []
    for part in parts:
        parts_list.append({'part_id': part.part_id, 'part_name': part.part_name})
    return jsonify(parts_list=parts_list)

@parts_blueprint.route('/part/delete')
def delete():
    # filter_by(part_id = num).delete() can be used too
    Part.query.filter(Part.part_id == 3).delete()
    DatabaseSession.commit()

    parts = Part.query.all()
    parts_list = []
    for part in parts:
        parts_list.append({'part_id': part.part_id, 'part_name': part.part_name})
    return jsonify(parts_list=parts_list)

@parts_blueprint.route('/part/join')
def results():
    # Now we want to get the part_drawings for parts of part_id = 45 and part_id 67
    parts = Part.query.join(PartDrawing, PartDrawing.part_id == Part.part_id)
    parts_list = []
    for part in parts:
        parts_list.append({'part_id': part.part_id, 'part_name': part.part_name})
    return jsonify(parts_list=parts_list)

@parts_blueprint.route('/part/vendor')
def results2():
    # Adding the first 3 vendors that already exist in the db to part of part_id=1

    part1 = Part.query.filter(Part.part_id == 1).first()

    vendors_for_part1 = []
    vendors_for_part1.append(Vendor.query.filter_by(vendor_id = 1).first())
    vendors_for_part1.append(Vendor.query.filter_by(vendor_id = 2).first())
    vendors_for_part1.append(Vendor.query.filter_by(vendor_id = 3).first())

    # Add them to vendors of part1
    part1.vendors.extend(vendors_for_part1)

    DatabaseSession.commit()

    # Now get all the parts and their corresponding vendors
    parts = Part.query.all()
    answer_dict = {}
    parts_list = []
    for part in parts:
        vendors_list_for_this_part = []
        for vendor in part.vendors:
            vendors_list_for_this_part.append({'vendor_id': vendor.vendor_id,
                                               'vendor_name': vendor.vendor_name})

        parts_list.append({'vendorS for this part': vendors_list_for_this_part,
                           'part_id': part.part_id})
    answer_dict['all the vendorS for all the partS'] = parts_list

    # Now we going to do the same but on vendors and show all the vendors with their corresponding parts
    vendors = Vendor.query.all()
    vendors_list = []
    for vendor in vendors:
        parts_for_this_vendor = []
        for part in vendor.parts:
            parts_for_this_vendor.append({'part_id': part.part_id, 'part_name': part.part_name})
        vendors_list.append({'vendor_id': vendor.vendor_id,
                             'parts for this vendor': parts_for_this_vendor})

    answer_dict['all the partsS for all the vendorS'] = vendors_list

    return jsonify(answer_dict)

"""
When you take a look at the Vendor model, you never see a variable called parts. However,
in model Part we have an attribute called vendors. In either cases we can use them and for the
former we get NO error saying that class Vendor does not have an attribute called parts
"""