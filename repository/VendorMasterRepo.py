from util.DbUtil import DbUtil
from util.DbConstants import DbConstants
from util.ResponseConst import ResponseConst
import json

dbUtilObj=DbUtil()
class VendorMasterRepo:
    def createVendorMaster(self,data):
        cursor=dbUtilObj.getPostgresqlConnection()
        cursor.execute(DbConstants.createVendorMasterId)
        vendorMasterId= dict((cursor.fetchall())[0]) 
        cursor.execute(DbConstants.createVendorMaster+f"('{vendorMasterId['vm_id']}','{data['vm_business_name']}','{data['vm_name']}','{data['vm_mobile_no']}','{data['vm_landmark']}','{data['vm_street']}','{data['vm_postal_code']}','{data['vm_city']}','{data['vm_state']}','{data['vm_country']}','{data['vm_created_date']}','{data['vm_created_by']}','{data['vm_gst_number']}','{data['vm_active_status']}')")
        cursor.close()
        respObj={"status":ResponseConst.userCreatedSuccessfully,"success":True,"data":vendorMasterId['vm_id']}
        return json.dumps(respObj)
    def fetchVendorMaster(self):
        cursor=dbUtilObj.getPostgresqlConnection()
        cursor.execute(DbConstants.getVendorMaster)
        results = cursor.fetchall()
        cursor.close()
        if results!=None:
            responseData={"status":ResponseConst.success,"success":True,"data":results}
            return json.dumps(responseData) 
        else:   
            return json.dumps({"status":ResponseConst.noDataFound})
        