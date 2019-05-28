'''
the permission will be set in the database
and only the managers will have permission to
cancel an order already completed
'''
class User():
    def __init__(self, userid, username, permission):
        self.userid=userid
        self.username=username
        self.permission=permission

    def getItemNumber(self):
        return self.userid

    def getItemName(self):
        return self.username

    def getPermission(self):
        return self.permission
    
    def __str__(self):
        return self.username