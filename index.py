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
{'name': 'description', 'type': 'Edm.String', 'retrievable': 'true', 'searchable': 'true'},
{'name': 'youtube_thumbnail_link', 'type': 'Edm.String', 'retrievable': 'true'},
{'name': 'title', 'type': 'Edm.String', 'retrievable': 'true'},
{'name': 'duration', 'type': 'Edm.Int64', 'retrievable': 'true'},
{'name': 'frame_features', 'type': 'Collection(Edm.ComplexType)', 'fields': [
{'name': 'frame_no', 'type': 'Edm.Int64'},
{'name': 'adult', 'type': 'Edm.ComplexType', 'fields': [
{'name': 'adultScore', 'type': 'Edm.Double', 'retrievable': 'true', 'filterable': 'true'},
{'name': 'isAdultContent', 'type': 'Edm.Boolean', 'facetable': 'true', 'filterable': 'true'},
{'name': 'isRacyContent', 'type': 'Edm.Boolean', 'facetable': 'true', 'filterable': 'true'},
{'name': 'racyScore', 'type': 'Edm.Double', 'retrievable': 'true', 'filterable': 'true'}
]},
{'name': 'categories', 'type': 'Collection(Edm.ComplexType)', 'fields': [
{'name': 'name', 'type': 'Edm.String', 'retrievable': 'true'},
{'name': 'score', 'type': 'Edm.Double', 'retrievable': 'true', 'filterable': 'true'}
]},
{'name': 'description', 'type': 'Edm.ComplexType', 'fields': [
{'name': 'captions', 'type': 'Collection(Edm.ComplexType)', 'fields': [
{'name': 'confidence', 'type': 'Edm.Double', 'retrievable': 'true', 'filterable': 'true'},
{'name': 'text', 'type': 'Edm.String', 'retrievable': 'true'}
]},
{'name': 'tags', 'type': 'Collection(Edm.String)', 'retrievable': 'true'}
]},
{'name': 'tags', 'type': 'Collection(Edm.ComplexType)', 'fields': [
{'name': 'confidence', 'type': 'Edm.Double', 'retrievable': 'true', 'filterable': 'true'},
{'name': 'name', 'type': 'Edm.String'}
]}
]}
]
}

create_index(index_schema)

def listener(event):
    value = event.data
    for key in list(value.keys()):
        for i in range(0, len(value[key]['frame_features'])):
            value[key]['frame_features'][i].pop('color', None)
            value[key]['frame_features'][i].pop('faces', None)
            value[key]['frame_features'][i].pop('image_type', None)
            value[key]['frame_features'][i].pop('metadata', None)
            value[key]['frame_features'][i].pop('request_id', None)
            value[key]['frame_features'][i]['frame_no'] = i
        insert(index_schema['name'], [value[key]])

db.reference('/').listen(listener)