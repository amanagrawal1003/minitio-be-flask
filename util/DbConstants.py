class DbConstants:
    getNormalUser="SELECT user_id ,user_first_name ,user_last_name ,user_email ,user_mobile_no ,user_password ,user_type ,user_status,user_gender, user_dob, user_mob_verified  FROM user_master where"
    createNormalUser="insert into user_master(user_id ,user_first_name ,user_last_name ,user_email ,user_mobile_no ,user_password ,user_type,user_status , user_gender, user_dob, user_mob_verified) values"
    createNUserId="SELECT COALESCE(cast(max(user_id) as BIGINT)+1, 101) as user_id FROM user_master"
    getNormalUserValidation="select user_type,user_status from user_master where"
    updateNormalUser="""Update user_master
                        set user_first_name = %s ,user_last_name = %s ,user_email= %s ,user_mobile_no= %s  ,user_status= %s , user_gender= %s, user_dob= %s , user_mob_verified= %s
                        where user_id = %s
                     """
    nUserType="NORMAL"
    statusInActive="INACTIVE"
    statusActive="ACTIVE"
    verifIed= "VERIFIED"
    notVerified="NOT_VERIFIED"
    createVendorMasterId="SELECT COALESCE(cast(max(vm_id) as BIGINT)+1, 101) as vm_id FROM Vendor_Master"
    createVendorMaster="insert into vendor_master(vm_id ,vm_business_name ,vm_name ,vm_mobile_no ,vm_landmark ,vm_street ,vm_postal_code ,vm_city,vm_state,vm_country,vm_created_date,vm_created_by,vm_gst_number,vm_active_status) values"
    getVendorMaster="Select vm_id ,vm_business_name ,vm_name ,vm_mobile_no ,vm_landmark ,vm_street ,vm_postal_code ,vm_city,vm_state,vm_country,vm_created_date,vm_created_by,vm_gst_number,vm_active_status,vm_user_id from Vendor_Master"
    getProductMaster="Select pm_id,pm_name,pm_adv_line,pm_home_image,pm_status from product_master where pm_status='ACTIVE'"
    getProductDetails="SELECT pd_id ,pd_pm_id ,pd_name ,pd_description ,pd_price,pd_supplier_id ,pd_avg_cust_ratings ,pd_sale_active_flag ,pd_profile_image_link, pd_active_status,pd_colours,pd_sizes,pd_purchase_price,pd_sale_price,pd_listed_date,pd_popular_flag,pd_specification  from product_details where "
    createProductDetails="""insert into product_details (pd_id ,pd_pm_id ,pd_name ,pd_description ,pd_price,pd_supplier_id ,pd_avg_cust_ratings ,pd_sale_active_flag ,pd_profile_image_link, pd_active_status,pd_colours,pd_sizes,pd_purchase_price,pd_sale_price,pd_listed_date,pd_popular_flag,pd_specification) 
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    getImageMaster="Select im_id,im_url,im_pd_id,im_active from image_master where"
    createImageMaster="insert into image_master(im_id,im_url,im_pd_id,im_active) values(%s,%s,%s,%s)"
    getAddressMaster="Select am_id,am_um_id,am_name,am_mobile_no,am_street,am_postal_code,am_city,am_state,am_country,am_created_date,am_primary_flag from Address_Master where"
    createAddressMaster="insert into Address_Master(am_id,am_um_id,am_name,am_mobile_no,am_street,am_postal_code,am_city,am_state,am_country,am_created_date,am_primary_flag) values"
    createNAddressId="SELECT COALESCE(cast(max(am_id) as BIGINT), 100) + 1 as am_id from address_master"
    updatePrimaryAddressMaster= """
                                    UPDATE Address_Master
                                    SET am_primary_flag = CASE
                                        WHEN am_id = %s THEN 'ACTIVE'
                                        ELSE 'INACTIVE'
                                    END
                                    WHERE am_um_id = %s; """
    createNewUserOrderMaster="""insert into order_master(om_id,om_user_id,om_status,om_total_amount,om_payment_method ,
    om_payment_id,om_order_date_time,om_tracking_id,om_delivery_date_time,om_return_date_time,om_refund_flag,om_am_id)
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ;"""
    createNewUserOrderDetails="""insert into order_details(od_id,od_om_id,od_created_time,od_pd_color,od_pd_size,
    od_price,od_user_id ,od_pd_id,od_pd_name,od_pd_quantity,od_pd_image,od_tracking_id,od_refund_flag,od_refund_status,
    od_refund_amount,od_product_customization)
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ;"""
    fetchUserOrderMasterByUserId="""  select om_id,om_user_id,om_status,om_total_amount,om_payment_method ,
    om_payment_id,om_order_date_time,om_tracking_id,om_delivery_date_time,om_return_date_time,om_refund_flag,om_am_id,
    am_id,am_um_id,am_name,am_mobile_no,am_street,am_postal_code,am_city,am_state,am_country,am_created_date,am_primary_flag 
    from Order_master o,Address_Master a where o.om_user_id = '%s' and o.om_am_id = a.am_id and o.om_user_id = a.am_um_id 
    order by om_order_date_time desc; """

    fetchUserOrderDetailsByUserIdAndOrderMasterId=""" select  od_id,od_om_id,od_created_time,od_pd_color,od_pd_size,
    od_price,od_user_id ,od_pd_id,od_pd_name,od_pd_quantity,od_pd_image,od_tracking_id,od_refund_flag,od_refund_status,
    od_refund_amount,od_product_customization from Order_Details where od_om_id = '%s' and od_user_id = '%s' ; """

    addCustomizationDetailsOnOrderDetails="""
                                    UPDATE order_details
                                    SET od_product_customization = '%s'
                                    WHERE od_id = '%s';  """
    updateOrderMasterUserPayment="""
                                    UPDATE order_master
                                    SET om_status = '%s',
                                    om_payment_id = '%s'
                                    WHERE om_id = '%s';  """
    fetchAdminSupplierOrderDeails="""
                                    select od_id,od_om_id,od_created_time,od_pd_color,od_pd_size,
                                    od_price,od_user_id ,od_pd_id,od_pd_name,od_pd_quantity,od_pd_image,od_tracking_id,od_refund_flag,od_refund_status,
                                    od_refund_amount,od_product_customization 
                                    from order_details o,product_details p 
                                    where o.od_pd_id = p.pd_id and pd_supplier_id = '%s';
                                  """
    changeOrderDetailStatus="""
                                    UPDATE order_details
                                    SET od_tracking_id = '%s', od_refund_status ='%s'
                                    WHERE od_id = '%s';  """