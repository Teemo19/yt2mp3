# Author: Celso Alejandro Maldonado
# Date: 05/06/2023
# Linkedin: https://www.linkedin.com/in/alejandro-maldonado-a9a908148/
from abc import ABC
from youtubesearchpython import VideosSearch

ZERO = 0

class info_search(ABC):
    @staticmethod
    def search_link():
        search = VideosSearch(["result"][ZERO].get("title"))
        
    