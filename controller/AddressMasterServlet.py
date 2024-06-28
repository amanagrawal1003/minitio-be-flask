from repository.AddressMasterRepo import AddressMasterRepo
from repository.UserMasterRepo import UserMasterRepo
from util.Util import Util
from util.ResponseConst import ResponseConst
from flask import Blueprint,request
address_master_blueprint = Blueprint('address_master', __name__)
addressMasterRepo=AddressMasterRepo()
userMasterRepo=UserMasterRepo()
util=Util()
@address_master_blueprint.route("/create/addressMaster/fOr/uSerId", methods=["POST"])
def createUserAddressMaster():
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        print('createUserAddressMaster')
        print(request.json)
        print()
        return addressMasterRepo.createUserAddressMaster((request.json)['address_master'])
    else:
        return ResponseConst.noDataFound
@address_master_blueprint.route("/get/addressMaster/lIst/bY/uSerId", methods=["POST"])
def getAddressMaster():
    print('getAddressMaster')
    print((request.json))
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        print('getAddressMaster')
        print((request.json))
        return addressMasterRepo.getAddressMaster((request.json)['user_master'])
    else:
        return ResponseConst.noDataFound
@address_master_blueprint.route("/update/addressMaster/primaryAddress/fOr/uSerId", methods=["POST"])
def updateUserPrimaryAddressMaster():
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        return addressMasterRepo.updateUserPrimaryAddressMaster((request.json)['address_master'])
    else:
        return ResponseConst.noDataFound