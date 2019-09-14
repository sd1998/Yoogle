import youtube_dl

class YoutubeMetadata :
    
    @staticmethod
    def extract_youtube_metadata(url):
        ydl = youtube_dl.YoutubeDL({'outtmpl': url[url.rfind('/'): len(url)] + ".mkv"})        
        with ydl:
            result = ydl.extract_info(url, download=False)
        return result
        
    @staticmethod
    def download_youtube_video(url, video_file_path):
        with youtube_dl.YoutubeDL({'outtmpl': video_file_path,'noplaylist': True, 'format': 'worst'}) as ydl:
            ydl.download([url])