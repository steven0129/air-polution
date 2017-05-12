import os
import xlrd
import csv
from pathlib import Path


class IO:
    def listFromDir(self, dirName):
        dir = []
        for root, dirs, fileNames in os.walk(dirName):
            for fileName in fileNames:
                dir.append(os.path.join(root, fileName))

        return dir


class filter:
    def byType(self, files, type):
        filteredFile = [file for file in files if file.endswith(type)]
        return filteredFile
