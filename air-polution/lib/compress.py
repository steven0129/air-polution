import zipfile


class zip:
    def extract(self, input, outDir):
        fZip = zipfile.ZipFile(input)
        fZip.extractall(outDir)
