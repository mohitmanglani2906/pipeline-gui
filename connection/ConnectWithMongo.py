from mongoengine import connect

class Connection:
    def __init__(self, dbName:str):
        self._dbName = dbName
        self._connectionString = 'mongodb+srv://<Your Username>:<Your Password>@cluster0.z8wlz.mongodb.net/{}?retryWrites=true&w=majority'.format(self._dbName)
        #self._connectionString = self._connectionString.format(self._dbName)
        connectObj = self.connectWithMongo()
        print("connectObj with pipeline-gui", connectObj)

    def connectWithMongo(self):
        print("connection string ",self._connectionString)
        obj = connect(host = self._connectionString)
        return obj