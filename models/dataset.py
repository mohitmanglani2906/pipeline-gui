from mongoengine import Document, StringField, DictField, DateTimeField
import datetime

class KaggleDataSet(Document):
    #Document represents this is a collection/table name in mongodb
    #these fields represents column names in kaggle_data_set collection/table
    dataset_name = StringField(required=True)
    dataset_json = DictField(required=True)
    createdAt = DateTimeField(default=datetime.datetime.now())

    @staticmethod
    def fetchDatasetJsonByName(dataset_name):
        datasetJsonObj =  KaggleDataSet.objects(dataset_name = dataset_name)
        datasetJson = dict()
        if datasetJsonObj and len(datasetJsonObj) == 1:
            for obj in datasetJsonObj:
                datasetJson = obj.dataset_json
        return datasetJson

    @staticmethod
    def fetchAllDatasetName():
        datasetObj = KaggleDataSet.objects().only('dataset_name')
        datasetNames = list(('Choose Dataset',))
        for obj in datasetObj:
            datasetNames.append(obj.dataset_name)
        return datasetNames

    def saveDataset(self):
        self.save()
