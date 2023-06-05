import unittest
from src.music_downloader.info_search import info_search

class test_infosearch(unittest.TestCase):
    def test_search(self):
        desc1 = "la chispa adecuada"
        desc2 = "pxndx los malaventurados"
        data1 = info_search.song_info(desc1)
        data2 = info_search.song_info(desc2)
        result1 = info_search.get_link(data1)
        result2 = info_search.get_link(data2)
        self.assertEqual(result1,"https://www.youtube.com/watch?v=jnDjEHyhFpU")
        self.assertEqual(result2,"https://www.youtube.com/watch?v=CF72RkHcKqs")
        
if __name__ == "__main__":
    unittest.main()