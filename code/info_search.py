# Author: Celso Alejandro Maldonado
# Date: 05/06/2023
# Linkedin: https://www.linkedin.com/in/alejandro-maldonado-a9a908148/
from abc import ABC
from youtubesearchpython import VideosSearch

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
        result = data["result"][0].get("link")
        return result