from flask import jsonify, Blueprint
from models.models2 import Vendor
from database.database import DatabaseSession

vendors_blueprint = Blueprint('Vendors', __name__)

@vendors_blueprint.route('/vendor/add')
def add():
    # First add a new vendor
    vendor = Vendor(vendor_name='Armin Vendor')
    DatabaseSession.add(vendor)
    DatabaseSession.commit()

    # Then query all the vendors
    vendors_of_type_query = Vendor.query.all()
    vendors_list = []
    for vendor in vendors_of_type_query:
        vendors_list.append({'vendor_id': vendor.vendor_id, 'vendor_name': vendor.vendor_name})
    return jsonify(vendors=vendors_list)
