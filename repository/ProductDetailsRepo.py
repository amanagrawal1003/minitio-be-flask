from util.DbUtil import DbUtil
from util.DbConstants import DbConstants
from util.ResponseConst import ResponseConst
from util.Util import Util
import json
util=Util()
dbUtilObj=DbUtil()

class ProductDetailsRepo:
    def getProductDetails(self,data):
        cursor=dbUtilObj.getPostgresqlConnection()
        query=''
        if(data['pm_id']=='3'):
            query=DbConstants.getProductDetails+f" pd_popular_flag='{DbConstants.statusActive}'"
        else:
            query=DbConstants.getProductDetails+f" pd_pm_id='{data['pm_id']}'"    
        cursor.execute(query)
        print('query')
        print(query)
        results = cursor.fetchall()
        print('getProductDetails')
        print(results)
        cursor.close()
        return json.dumps({"status":"success","success":True,"data":results})
    
    def get_product_details_list_by_id(self,data):
        cursor=dbUtilObj.getPostgresqlConnection()
        print("product id")
        print(data)
        placeholders = ', '.join(['%s' for _ in data])
        print("placeholders")
        print(placeholders)
        cursor.execute(DbConstants.getProductDetails+f" pd_id in ({placeholders})",data )
        results = cursor.fetchall()
        print('get_product_details_list_by_id')
        print(results)
        cursor.close()
        return json.dumps({"status":"success","success":True,"data":results})
    
    def create_product_details(self,data):
        cursor=dbUtilObj.getPostgresqlConnection()
        print("product id")
        print(data)
        pd_colours=util.listToCommaSepString(data['pd_colours'])
        pd_sizes=util.listToCommaSepString(data['pd_sizes'])
        cursor.execute(DbConstants.createProductDetails,(data['pd_id'], data['pd_pm_id'], data['pd_name'], data['pd_description'], data['pd_price'], data['pd_supplier_id'], data['pd_avg_cust_ratings'], data['pd_sale_active_flag'], data['pd_profile_image_link'], data['pd_active_status'], pd_colours, pd_sizes, data['pd_purchase_price'], data['pd_sale_price'], data['pd_listed_date'], data['pd_popular_flag'], data['pd_specification']))
        print('create_product_details')
        
        cursor.close()
        return True