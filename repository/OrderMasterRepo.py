from util.DbUtil import DbUtil
from util.DbConstants import DbConstants
from util.ResponseConst import ResponseConst
from repository.OrderDetailsRepo import OrderDetailsRepo
import json
dbUtilObj=DbUtil()
class OrderMasterRepo:
    def create_new_user_order(self,data):
        addressMaster=data['address_master']
        cursor=dbUtilObj.getPostgresqlConnection()
        cursor.execute(DbConstants.createNewUserOrderMaster,(data['om_id'],data['om_user_id'],data['om_status'],
                       data['om_total_amount'],data['om_payment_method'],data['om_payment_id'],
                       data['om_order_date_time'],data['om_tracking_id'],data['om_delivery_date_time'],
                       data['om_return_date_time'],data['om_refund_flag'],addressMaster['am_id']))
       
        cursor.close()
        order_details_list = data.get('list_order_details', [])
        for oDetails in order_details_list:
            oDetailsRepo = OrderDetailsRepo
            oDetailsRepo.create_new_user_order_details(self,oDetails)
        
        resbObj={"status":ResponseConst.orderCreatedSuccessfully,"success":True}
        return json.dumps(resbObj)
    
    def fetch_user_order_master(self,data):
        print("orfer user id")
        print(data['user_id'])
        cursor=dbUtilObj.getPostgresqlConnection()
        query=(DbConstants.fetchUserOrderMasterByUserId %(data['user_id']))
        print("query")
        print(query)
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        print("results order")
        resbObj=json.dumps({"status":ResponseConst.success,"success":True,"data":results})
        print(resbObj)
        return resbObj
    def update_user_order_master_payment(self,data):
        cursor=dbUtilObj.getPostgresqlConnection()
        query=DbConstants.updateOrderMasterUserPayment  % (data['om_status'],data['om_payment_id'], data['om_id'])
        print("query")
        print(query)
        cursor.execute(query)
        cursor.close()
        print("results order")
        resbObj=json.dumps({"status":ResponseConst.success,"success":True})
        print(resbObj)
        return resbObj