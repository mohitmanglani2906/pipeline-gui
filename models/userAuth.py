from mongoengine import Document, StringField

class userAuth(Document):
    userName = StringField(required=True, unique=True)
    userEmail = StringField(required=True, unique=True)
    fullName = StringField(required=True)
    password = StringField(required=True)

    @staticmethod
    def getUserObjByUserName(userName):
        userAuthObj = userAuth.objects(userName= userName)
        return userAuthObj
        # print(userAuthObj)
        # for obj in userAuthObj:
        #     print(obj.userName)
        #     print(obj.userEmail)
        #     print(obj.fullName)
        #     print(obj.password)