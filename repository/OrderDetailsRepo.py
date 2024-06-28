from util.DbUtil import DbUtil
from util.DbConstants import DbConstants
from util.ResponseConst import ResponseConst
import json
dbUtilObj=DbUtil()
class OrderDetailsRepo:
    def create_new_user_order_details(self,data):
        print(data)
        cursor=dbUtilObj.getPostgresqlConnection()
        cursor.execute(DbConstants.createNewUserOrderDetails,(data['od_id'],data['od_om_id'],data['od_created_time'],
                       data['od_pd_color'],data['od_pd_size'],data['od_price'],
                       data['od_user_id'],data['od_pd_id'],data['od_pd_name'],
                       data['od_pd_quantity'],data['od_pd_image'],data['od_tracking_id'],
                       data['od_refund_flag'],data['od_refund_status'],data['od_refund_amount'],data['od_product_customization']))
        cursor.close()
        resbObj={"status":ResponseConst.userCreatedSuccessfully,"success":True}
        return json.dumps(resbObj)
    
    def fetch_user_order_details(self,od_om_id,user_id):
        cursor=dbUtilObj.getPostgresqlConnection()
        query=DbConstants.fetchUserOrderDetailsByUserIdAndOrderMasterId %(od_om_id ,user_id)
        print("query")
        print(query)
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        print("results order")
        resbObj=json.dumps({"status":ResponseConst.success,"success":True,"data":results})
        print(resbObj)
        return resbObj
    def add_order_customization_details(self,od_product_customization,od_id):
        cursor=dbUtilObj.getPostgresqlConnection()
        query=DbConstants.addCustomizationDetailsOnOrderDetails % (od_product_customization, od_id)
        cursor.execute(query)
        cursor.close()
        resbObj=json.dumps({"status":ResponseConst.success,"success":True,"data":True})
        return resbObj
    
    def fetch_admin_supplier_order_deails(self,user_master):
        cursor=dbUtilObj.getPostgresqlConnection()
        query=DbConstants.fetchAdminSupplierOrderDeails % (user_master['user_id'])
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        resbObj=json.dumps({"status":ResponseConst.success,"success":True,"data":results})
        print(resbObj)
        return resbObj
    
    def admin_change_order_details_status(self,order_details):
        cursor=dbUtilObj.getPostgresqlConnection()
        query=DbConstants.changeOrderDetailStatus % (order_details['od_tracking_id'],order_details['od_refund_status'], order_details['od_id'])
        cursor.execute(query)
        cursor.close()
        resbObj=json.dumps({"status":ResponseConst.success,"success":True,"data":True})
        return resbObj