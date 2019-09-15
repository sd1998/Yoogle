from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def create_index(es_object, index_name='recipes'):
    created = False
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "members": {
                "dynamic": "strict",
                "properties": {
                    "youtube_link": {
                        "type": "text"
                    },
                    "description": {
                        "type": "text"
                    },
                    "youtube_thumbnail_link": {
                        "type": "text"
                    },
                    "title": {
                        "type": "text"
                    },
                    "duration": {
                        "type": "integer"
                    },
                    "frame_features": {
                        "type": "nested",
                        "properties":{
                            "frame_no": {"type": "integer"},
                            "adult": {"type": "nested",
                            "properties":{
                            "adultScore":{"type" : "float"},
                            "isAdultContent":{"type" : "boolean"},
                            "isRacyContent":{"type" : "boolean"},
                            "racyScore":{"type" : "float"},
                            }},
                            "categories": {"type": "nested",
                            "properties":{
                            "name":{"type":"text"},
                            "score":{"type":"float"}
                            }},
                            "description": {"type": "nested",
                            "properties":{
                            "captions":{"type":"nested",
                            "properties":{
                                "confidence":{"type":"float"},
                                "text":{"type":"text"}
                            }},
                            "tags": {"type": "nested",
                            "properties":{
                            "tags":{"type":"text"}
                            }},
                            }},
                            "tags": {'type': 'nested', 'properties' {
                            'confidence': {'type': 'float'},
                            'name': {'type': 'text'}
                            }}
                        }
                    }
                }
            }
        }
    }
try:
        if not es_object.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            es_object.indices.create(index=index_name, ignore=400, body=settings)
            print('Created Index')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created