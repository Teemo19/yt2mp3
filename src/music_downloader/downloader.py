import yt_dlp.YoutubeDL as ydl

class Youtube:
    def __init__(self):
        pass

    def download_mp3(self,link,title):
        ydl_opts = {
            'format': 'bestaudio/best[filesize<4M]',
            'outtmpl': f'music/{title}',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        ydl(ydl_opts).download([link])