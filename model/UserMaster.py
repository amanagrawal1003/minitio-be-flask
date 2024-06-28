
class UserMaster(): 
     user_id = ""
     user_first_name = ""
     user_last_name = ""
     user_email = ""
     user_mobile_no = 0 
     user_password = ""
     user_type = ""
     def __init__(self, id, first_name, last_name,email,mobileNo,type,password):
          self.id = id
          self.first_name = first_name
          self.last_name = last_name
          self.email = email
          self.mobileNo = mobileNo
          self.type = type
          self.password = password

     def __repr__(self):
          return '<id {}>'.format(self.id)