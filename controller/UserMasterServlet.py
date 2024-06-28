from repository.UserMasterRepo import UserMasterRepo
from util.ResponseConst import ResponseConst
from util.Util import Util
from flask import Blueprint,request
user_master_blueprint = Blueprint('user_master', __name__)
userMasterRepo=UserMasterRepo()
util=Util()
@user_master_blueprint.route("/create/normal/user", methods=["POST"])
def create_normal_user():
    return userMasterRepo.create_normal_user((request.json)['user_master'])
@user_master_blueprint.route("/get/normal/user", methods=["POST"])
def get_normal_user():
    return userMasterRepo.get_normal_user((request.json)['user_master'])
@user_master_blueprint.route("/update/normal/user", methods=["POST"])
def update_normal_user():
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        return userMasterRepo.update_normal_user((request.json)['user_master']), 200, {'Content-Type': 'application/json'}
    else:
        return ResponseConst.noDataFound
@user_master_blueprint.route("/check")
def checkController():
    return"working"

