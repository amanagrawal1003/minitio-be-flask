from util.DbUtil import DbUtil
from util.DbConstants import DbConstants
from util.ResponseConst import ResponseConst
import json

dbUtilObj=DbUtil()

class AddressMasterRepo:
    def createUserAddressMaster(self,data):
        print(data)
        cursor=dbUtilObj.getPostgresqlConnection()
        cursor.execute(DbConstants.createNAddressId)
        addressId= dict((cursor.fetchall())[0]) 
        cursor.execute(DbConstants.createAddressMaster+f"('{addressId['am_id']}','{data['am_um_id']}','{data['am_name']}','{data['am_mobile_no']}','{data['am_street']}','{data['am_postal_code']}','{data['am_city']}','{data['am_state']}','{data['am_country']}','{data['am_created_date']}','{data['am_primary_flag']}')")
        cursor.close()
        resbObj={"status":ResponseConst.userCreatedSuccessfully,"success":True,"data":addressId['am_id']}
        return json.dumps(resbObj)

    def getAddressMaster(self,data):
        cursor=dbUtilObj.getPostgresqlConnection()
        cursor.execute(DbConstants.getAddressMaster+f" am_um_id='{data['user_id']}'")
        results = cursor.fetchall()
        print('getAddressMaster')
        print(results)
        cursor.close()
        return json.dumps({"status":"success","success":True,"data":results})
    def updateUserPrimaryAddressMaster(self,data):
        cursor=dbUtilObj.getPostgresqlConnection()
        print(data)
        cursor.execute(DbConstants.updatePrimaryAddressMaster,(data['am_id'],data['am_um_id']))
        cursor.close()
        return json.dumps({"status":"success","success":True,"data":"SUCCESS"})
    
    