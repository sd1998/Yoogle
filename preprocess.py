import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from youtube_metadata import YoutubeMetadata
from azure import extract_video_features
import time
import os

firebase_credentials = credentials.Certificate('serviceAccountKey.json')

firebase = firebase_admin.initialize_app(firebase_credentials, {
'databaseURL': 'https://htn2019-e1074.firebaseio.com'
})

def preprocess(video):
    youtube_metadata = YoutubeMetadata.extract_youtube_metadata(video)
    video_file_path = youtube_metadata['id'] + '.mkv'
    YoutubeMetadata.download_youtube_video(video, video_file_path)
    if os.path.exists(video_file_path):
        video_features = extract_video_features(video_file_path)
        video_data = {
        'youtube_link': video,
        'title': youtube_metadata['title'],
        'description': youtube_metadata['description'],
        'duration': youtube_metadata['duration'],
        'features': video_features,
        'youtube_thumbnail_link': youtube_metadata['thumbnails'][0]['url'] if youtube_metadata['thumbnails'] is not None else None
        }
        os.remove(video_file_path)
        db.reference(youtube_metadata['id']).set(video_data)