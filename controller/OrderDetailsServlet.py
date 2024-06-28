from repository.OrderDetailsRepo import OrderDetailsRepo
from repository.UserMasterRepo import UserMasterRepo
from util.Util import Util
from util.ResponseConst import ResponseConst
from flask import Blueprint,request
order_details_blueprint = Blueprint('order_details', __name__)
orderDetailsRepo=OrderDetailsRepo()
userMasterRepo=UserMasterRepo()
util=Util()
@order_details_blueprint.route("/create/orderDetails/fOr/uSerId", methods=["POST"])
def create_order_details():
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        return orderDetailsRepo.create_new_user_order_details((request.json)['order_details'])
    else:
        return ResponseConst.noDataFound
    
@order_details_blueprint.route("/fetch/orderDetails/lIst/bY/uSerId", methods=["POST"])
def fetch_user_order_details():
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        return orderDetailsRepo.fetch_user_order_details((request.json)['order_master'].get('om_id'),(request.json)['user_master'].get('user_id'))
    else:
        return ResponseConst.noDataFound
    
@order_details_blueprint.route("/customize/orderDetails/bY/oDId", methods=["POST"])
def add_order_customization_details():
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        print((request.json)['order_details'].get('od_product_customization'))
        print('test11')
        return orderDetailsRepo.add_order_customization_details((request.json)['order_details'].get('od_product_customization'),(request.json)['order_details'].get('od_id'))
    else:
        return ResponseConst.noDataFound
    
@order_details_blueprint.route("/admin/supplier/orderDetails", methods=["POST"])
def fetch_admin_supplier_order_deails():

    print('order_details admin')
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_type']=="ADMIN"):
        return orderDetailsRepo.fetch_admin_supplier_order_deails((request.json)['user_master'])
    else:
        return ResponseConst.noDataFound    
@order_details_blueprint.route("/admin/change/orderDetails/status", methods=["POST"])
def admin_change_order_details_status():

    print('admin_change_order_details_status admin')
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_type']=="ADMIN"):
        return orderDetailsRepo.admin_change_order_details_status((request.json)['order_details'])
    else:
        return ResponseConst.noDataFound   
    
    