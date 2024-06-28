from util.DbUtil import DbUtil
from util.DbConstants import DbConstants
from util.ResponseConst import ResponseConst
import json

dbUtilObj=DbUtil()

class ImageMasterRepo:
    def getImageMaster(self,productMaster):
        cursor=dbUtilObj.getPostgresqlConnection()
        print("productMaster:")
        print(productMaster['pd_id'])
        cursor.execute(DbConstants.getImageMaster+f" im_pd_id='{productMaster['pd_id']}'")
        results = cursor.fetchall()
        print('getImageMaster')
        print(results)
        cursor.close()
        return json.dumps({"status":"success","success":True,"data":results})
    
    def createImageMaster(self,imageMaster):
        cursor=dbUtilObj.getPostgresqlConnection()
        print(imageMaster)
        print("ImageMaster")
        cursor.execute(DbConstants.createImageMaster,(imageMaster['im_id'],imageMaster['im_url'],imageMaster['im_pd_id'],imageMaster['im_active']))
        print('created imageMaster')
        cursor.close()
        return json.dumps({"status":"success","success":True})