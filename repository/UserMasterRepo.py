from util.DbUtil import DbUtil
from util.DbConstants import DbConstants
from util.ResponseConst import ResponseConst
from flask import jsonify
import json
dbUtilObj=DbUtil()
class UserMasterRepo:    
    def create_normal_user(self,data):
        print(data)
        cursor=dbUtilObj.getPostgresqlConnection()
        cursor.execute(DbConstants.createNUserId)
        userId= dict((cursor.fetchall())[0]) 
        cursor.execute(DbConstants.createNormalUser+f"('{userId['user_id']}','{data['user_first_name']}','{data['user_last_name']}','{data['user_email']}','{data['user_mobile_no']}','{data['user_password']}','{DbConstants.nUserType}','{DbConstants.statusActive}','{data['user_gender']}','{data['user_dob']}','{DbConstants.verifIed}')")
        cursor.close()
        print(json.dumps({"status":"success","success":True,"data":str(userId['user_id'])}))
        return json.dumps({"status":"success","success":True,"data":str(userId['user_id'])})
    
    def update_normal_user(self,data):
        print('data')
        print(data)
        cursor=dbUtilObj.getPostgresqlConnection()
        cursor.execute(DbConstants.updateNormalUser,(data['user_first_name'],data['user_last_name'],data['user_email'],data['user_mobile_no'],data['user_status'],data['user_gender'],data['user_dob'],DbConstants.notVerified,data['user_id']))
        cursor.close()
        print('am update')
        return json.dumps({"status":"success","success":True,"data":"SUCCESS"})


    def get_normal_user(self,data):
        print('test1')
        print(data['user_mobile_no'])
        cursor=dbUtilObj.getPostgresqlConnection()
        cursor.execute(DbConstants.getNormalUser+f"(user_email='{data['user_mobile_no']}' or user_mobile_no='{data['user_mobile_no']}' )")
        results = cursor.fetchone()
        print('test2')
        print(results)
        cursor.close()
        if results!=None:
            responseData={"results":results,"status":ResponseConst.validUser}
            return json.dumps(responseData) 
        else:   
            return json.dumps({"status":ResponseConst.noDataFound})

    def get_normal_user_validation(self,data):
        cursor=dbUtilObj.getPostgresqlConnection()
        cursor.execute(DbConstants.getNormalUserValidation+f" user_id='{data['user_id']}'")
        results = cursor.fetchall()
        cursor.close()
        if len(results)>0:
            return json.dumps(results)
        else:
            return ResponseConst.noDataFound       
        
      