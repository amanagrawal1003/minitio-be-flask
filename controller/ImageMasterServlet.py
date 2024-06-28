from flask import Blueprint,request
from util.Util import Util
from repository.UserMasterRepo import UserMasterRepo
from repository.ImageMasterRepo import ImageMasterRepo
from util.ResponseConst import ResponseConst
image_master_blueprint = Blueprint('image_master', __name__)
util=Util()
userMasterRepo=UserMasterRepo()
imageMasterRepo=ImageMasterRepo()
@image_master_blueprint.route("/get/imageMaster", methods=["POST"])
def get_image_master():
    return imageMasterRepo.getImageMaster(request.json)    