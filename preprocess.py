import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from youtube_metadata import YoutubeMetadata
from azure import extract_frame_features
import time
import os
import json
import shutil

firebase_credentials = credentials.Certificate('serviceAccountKey.json')

firebase = firebase_admin.initialize_app(firebase_credentials, {
'databaseURL': 'https://htn2019-e1074.firebaseio.com'
})

def preprocess(video):
    youtube_metadata = YoutubeMetadata.extract_youtube_metadata(video)
    video_file_path = youtube_metadata['id'] + '.mkv'
    YoutubeMetadata.download_youtube_video(video, video_file_path)
    if os.path.exists(video_file_path):
        if not os.path.exists(youtube_metadata['id']):
            if youtube_metadata['id'][0] == '-':
                dir_name = youtube_metadata['id'][1:]
            else:    
                dir_name = youtube_metadata['id']
            os.mkdir(dir_name)
        os.system("ffmpeg -i " + video_file_path + " -vf fps=1/3 " + dir_name + "/out%d.png")
        video_data = {
        'youtube_link': video,
        'title': youtube_metadata['title'],
        'description': youtube_metadata['description'],
        'duration': youtube_metadata['duration'],
        'youtube_thumbnail_link': youtube_metadata['thumbnails'][0]['url'] if youtube_metadata['thumbnails'] is not None else None,
        'frame_features': []
        }
        files = os.listdir(dir_name)
        for i in range(0,len(files)):
            frame_features = extract_frame_features(dir_name + "/" + files[i])
            frame_features = json.loads(frame_features.decode('utf-8'))
            print(frame_features)
            if frame_features.get('error') is not None and frame_features['error']['code'] == '429':
                i -= 1
                time.sleep(60)
            else:
                video_data['frame_features'].append(frame_features)
        os.remove(video_file_path)
        shutil.rmtree(dir_name)
        db.reference(dir_name).set(video_data)