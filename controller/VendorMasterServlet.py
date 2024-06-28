from repository.VendorMasterRepo import VendorMasterRepo
from repository.UserMasterRepo import UserMasterRepo
from util.Util import Util
from util.ResponseConst import ResponseConst
from flask import Blueprint,request
vendor_master_blueprint = Blueprint('vendor_master', __name__)
vendorMasterRepo=VendorMasterRepo()
userMasterRepo=UserMasterRepo()
util=Util()
@vendor_master_blueprint.route("/create/vendorMaster", methods=["POST"])
def createVendorMaster():
    print("createVendorMaster")
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_type']=="ADMIN"):
        print((request.json))
        return vendorMasterRepo.createVendorMaster((request.json)['vendor_master'])
    else:
        return ResponseConst.noDataFound
    
@vendor_master_blueprint.route("/fetch/vendorMaster", methods=["POST"])
def fetchVendorMaster():
    print("fetchVendorMaster")
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_type']=="ADMIN"):
        return vendorMasterRepo.fetchVendorMaster()
    else:
        return ResponseConst.noDataFound
    
    