from mongoengine import Document, StringField

class userAuth(Document):
    #This class will work as a collection of our authentication database.
    userName = StringField(required=True, unique=True)
    userEmail = StringField(required=True, unique=True)
    fullName = StringField(required=True)
    password = StringField(required=True)

    @staticmethod
    def getUserObjByUserName(userName):
        userAuthObj = userAuth.objects(userName= userName)
        return userAuthObj