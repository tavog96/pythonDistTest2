import os

class TextFileController:

    filesFolderPath = ''

    def __init__(self, filesFolderPath):
        super().__init__()
        self.filesFolderPath = filesFolderPath

    def filesNamesScan (self):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.filesFolderPath):
            for file in f:
                if (r==self.filesFolderPath):
                    files.append(file)
        return files

    def fileInfoScan (self, filepath):
        fileInfoResult = {}
        fileMetaStats = os.stat(self.filesFolderPath+'/'+filepath)
        fileInfoResult['name'] = filepath
        fileInfoResult['size'] = fileMetaStats.st_size
        fileInfoResult['lastmodificate'] = fileMetaStats.st_mtime
        return fileInfoResult
    
    def filesInfoScan (self):
        filesInfo2Return=[]
        filespaths = self.filesNamesScan()
        for eachFilepath in filespaths:
            if '.py' not in eachFilepath and eachFilepath != "__pycache__":
                filesInfo2Return.append(self.fileInfoScan(eachFilepath))
        return filesInfo2Return

    def readFileContent (self, fileName):
        try:
            f = open(self.filesFolderPath + '/'+fileName, "r")
            return (f.read())
        except:
            return False
