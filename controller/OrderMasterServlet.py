from repository.OrderMasterRepo import OrderMasterRepo
from repository.UserMasterRepo import UserMasterRepo
from util.Util import Util
from util.ResponseConst import ResponseConst
from flask import Blueprint,request
order_master_blueprint = Blueprint('order_master', __name__)
orderMasterRepo=OrderMasterRepo()
userMasterRepo=UserMasterRepo()
util=Util()
@order_master_blueprint.route("/create/orderMaster/fOr/uSerId", methods=["POST"])
def create_order_master():
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        return orderMasterRepo.create_new_user_order((request.json)['order_master'])
    else:
        return ResponseConst.noDataFound
    
@order_master_blueprint.route("/fetch/orderMaster/lIst/bY/uSerId", methods=["POST"])
def fetch_user_order_master():
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        print('test123')
        return orderMasterRepo.fetch_user_order_master((request.json)['user_master'])
    else:
        return ResponseConst.noDataFound    
@order_master_blueprint.route("/update/orderMaster/pAYmENt/fOr/uSerId", methods=["POST"])
def update_user_order_master_payment():
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        print('test123')
        return orderMasterRepo.update_user_order_master_payment((request.json)['order_master'])
    else:
        return ResponseConst.noDataFound
    
    