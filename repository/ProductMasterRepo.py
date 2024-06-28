from util.DbUtil import DbUtil
from util.DbConstants import DbConstants
from util.ResponseConst import ResponseConst
import json

dbUtilObj=DbUtil()

class ProductMasterRepo:
    def getProductMaster(self):
        cursor=dbUtilObj.getPostgresqlConnection()
        cursor.execute(DbConstants.getProductMaster)
        results = cursor.fetchall()
        cursor.close()
        return json.dumps({"status":"success","success":True,"data":results})