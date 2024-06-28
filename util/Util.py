import ast

class Util:
    def listToString(self,list1):
        listToStr = ' '.join(map(str, list1))
        return listToStr
    def stringToList(self,data):
        l1= ast.literal_eval(data)
        return l1
    def listToCommaSepString(self,my_list):
        comma_separated_string = ', '.join(my_list)
        return comma_separated_string