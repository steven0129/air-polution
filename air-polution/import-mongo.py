import os
import lib.shell as shell
import lib.compress as compress
import lib.file as file
import lib.db as db
import zipfile
import platform

myDB = db.mongo(dbName='air', collectionName='element')

if platform.system() == 'Windows':
    shell.command().run('type .\data\polution-data.zip.parta* > .\data\polution-data.zip')
elif platform.system() == 'Linux':
    shell.command().run('cat ./data/polution-data.zip.parta* > ./data/polution-data.zip')

compress.zip().extract(input='./data/polution-data.zip', outDir='data')

files = file.IO().listFromDir('./data/')
filteredCSVFile = file.filter().byType(files, 'csv')
filteredXLSFile = file.filter().byType(files, 'xls')
filteredFile = filteredCSVFile + filteredXLSFile

for myFile in filteredFile:
    myDB.insertFile(myFile, ['日期', '測站', '測項', '01', '02', '03', '04', '05', '06', '07',
                             '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])
