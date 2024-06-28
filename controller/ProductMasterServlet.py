from repository.ProductMasterRepo import ProductMasterRepo
from repository.UserMasterRepo import UserMasterRepo
from util.Util import Util
from util.ResponseConst import ResponseConst
from flask import Blueprint,request
product_master_blueprint = Blueprint('product_master', __name__)
productMasterRepo=ProductMasterRepo()
userMasterRepo=UserMasterRepo()
util=Util()
@product_master_blueprint.route("/get/productMaster", methods=["POST"])
def get_product_master():
    print('test m here')
    print(request.json)
    if((util.stringToList(userMasterRepo.get_normal_user_validation(request.json)))[0]['user_status']=="ACTIVE"):
        return productMasterRepo.getProductMaster()
    else:
        return ResponseConst.noDataFound