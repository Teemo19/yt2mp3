from abc import ABC
import os 

class directory(ABC):
    @staticmethod
    def createDirectory(path):
        os.mkdir(path)

    @staticmethod
    def verifyDirectoryExist(path):
        return os.path.exists(path)