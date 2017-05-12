import os
import sys
import pandas as pd
import pymongo
import json
import codecs
import csv
from bson.code import Code


class mongo:
    def __init__(self, dbName, collectionName, hostName='localhost', port=27017):
        self.conn = pymongo.MongoClient(hostName, port)
        self.dbName = dbName
        self.collectionName = collectionName

    def insertFile(self, filePath, headerNames):
        with codecs.open(filePath, "r", errors='ignore') as fdata:
            data = None
            print('解析 ' + filePath + ' 中......')

            if filePath.endswith('csv'):
                data = pd.read_csv(fdata, skiprows=1, names=headerNames)

            elif filePath.endswith('xls'):
                excel = pd.ExcelFile(filePath)
                data = excel.parse(excel.sheet_names[0], skiprows=0)

            dataJSON = json.loads(data.to_json(orient='records'))
            try:
                db = self.conn[self.dbName]
                db[self.collectionName].insert(dataJSON)
            except Exception as error:
                print(error)

    def mapReduce(self, outputCollection, mapper, reducer):
        db = self.conn[self.dbName]
        db[self.collectionName].map_reduce(
            Code(mapper), Code(reducer), outputCollection)

    def aggregate(self, pipeline):
        db = self.conn[self.dbName]
        result = db[self.collectionName].aggregate(
            pipeline, allowDiskUse=True)
        return result

    def dropCollection(self, collectionName):
        db = self.conn[self.dbName]
        db.drop_collection(collectionName)

    def find(self, query):
        db = self.conn[self.dbName]
        return db[self.collectionName].find(query)

    def distinct(self, field):
        db = self.conn[self.dbName]
        return db[self.collectionName].distinct(field)
