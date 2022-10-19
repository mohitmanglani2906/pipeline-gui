from mongoengine import connect
#ORM is object relational Mapping
#ODM Object document mapping

class Connection:
    def __init__(self, dbName:str):
        self._dbName = dbName
        self._connectionString = 'mongodb+srv://<your_username>:<your_password>@cluster0.z8wlz.mongodb.net/{}?retryWrites=true&w=majority'.format(self._dbName)
        connectObj = self.__connectWithMongo()

    #This method is used to connect with Mongo db. making this private because there is no use outside the class
    def __connectWithMongo(self):
        obj = connect(host= self._connectionString)
        return obj