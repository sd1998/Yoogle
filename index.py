from azure_search import create_index, insert
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

firebase_credentials = credentials.Certificate('serviceAccountKey.json')

firebase = firebase_admin.initialize_app(firebase_credentials, {
'databaseURL': 'https://htn2019-e1074.firebaseio.com'
})

index_schema = {
'name': 'htn-bitplease',
'fields': [
{'name': 'youtube_link', 'type': 'Edm.String', 'key': 'true', 'retrievable': 'true'},
{'name': 'youtube', 'type': 'Edm.String', 'retrievable': 'true'}
]
}

create_index(index_schema)

def listener(event):
    #value = event.data
    '''
     for key in list(value.keys()):
        print(value[key]['title'])
        for i in range(0, len(value[key]['frame_features'])):
            value[key]['frame_features'][i].pop('color', None)
            value[key]['frame_features'][i].pop('faces', None)
            value[key]['frame_features'][i].pop('image_type', None)
            value[key]['frame_features'][i].pop('metadata', None)
            value[key]['frame_features'][i].pop('request_id', None)
     insert(index_schema['name'], [value[key]])
    '''
    x=0
    for x in range(0,2):
        value = [{'youtube_link':str(x)},{'youtube':"ok"}]
        insert(index_schema['name'], value)
        x+=1
db.reference('/').listen(listener)
