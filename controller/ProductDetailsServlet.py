from repository.ProductDetailsRepo import ProductDetailsRepo
from repository.UserMasterRepo import UserMasterRepo
from repository.ImageMasterRepo import ImageMasterRepo
from util.Util import Util
from util.ResponseConst import ResponseConst
from flask import Blueprint,request
product_details_blueprint = Blueprint('product_details', __name__)
productDetailsRepo=ProductDetailsRepo()
userMasterRepo=UserMasterRepo()
imageMasterRepo=ImageMasterRepo()
util=Util()
@product_details_blueprint.route("/get/productDetails", methods=["POST"])
def get_product_details():
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        return productDetailsRepo.getProductDetails((request.json)['product_master'])
    else:
        return ResponseConst.noDataFound
@product_details_blueprint.route("/get/productDetails/lIst/bY/iD", methods=["POST"])
def get_product_details_list_by_id():
    if((util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master'])))[0]['user_status']=="ACTIVE"):
        pd_ids = [item['pd_id'] for item in (request.json['list_product_details'])]
        return productDetailsRepo.get_product_details_list_by_id(pd_ids)
    else:
        return ResponseConst.noDataFound
    
@product_details_blueprint.route("/create/productDetails/", methods=["POST"])
def create_product_details():
    valid_Admin=util.stringToList(userMasterRepo.get_normal_user_validation((request.json)['user_master']))
    print('user_type')
    print(valid_Admin[0]['user_type'])
    if(valid_Admin[0]['user_status']=="ACTIVE" and valid_Admin[0]['user_type']=="ADMIN"):
        if(productDetailsRepo.create_product_details((request.json)['product_details'])):
            print((request.json)['list_image_master'])
            for image_master in ((request.json)['list_image_master']):
                return imageMasterRepo.createImageMaster(image_master)
        else:
            return ResponseConst.somethingWentWromg+':Not able to upload images'
    else:
        return ResponseConst.noDataFound 