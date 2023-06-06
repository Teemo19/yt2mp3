# Author: Celso Alejandro Maldonado
# Date: 05/06/2023
# Linkedin: https://www.linkedin.com/in/alejandro-maldonado-a9a908148/
from abc import ABC
from youtubesearchpython import VideosSearch
import re

ZERO = 0

class info_search(ABC):
    @staticmethod
    def song_info(description):
        """
        Input: Name of the song

        Process: Check the name of the song

        Result: Return all the information about the song
        """
        search = VideosSearch(description,limit=1).result()
        return search
    
    @staticmethod
    def get_link(data):
        result = data["result"][ZERO].get("link")
        return result
    
    @staticmethod
    def get_title(data):
        title = data["result"][ZERO].get("title")
        result = re.sub('[/,#,|,*,],:,",(,),],',"",title)
        return result
    
    @staticmethod
    def get_artist(data):
        result = data["result"][ZERO].get("artist")
        return result
    