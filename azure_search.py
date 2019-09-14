import requests

azure_search_endpoint = 'https://htn-bitplease.search.windows.net/'
headers = {
'Content-Type': 'application/json',
'api-key': '68C76C8D11203B3952A579820A398AD3'
}
api_version = '?api-version=2019-05-06'

index_schema = {
'name': 'htn-bitplease',
'fields': [
{'name': 'youtube_link', 'type': 'Edm.String', 'key': 'true', 'retrievable': 'true'},
{'name': 'description', 'type': 'Edm.String', 'retrievable': 'true', 'searchable': 'true'},
{'name': 'youtube_thumbnail_link', 'type': 'Edm.String', 'retrievable': 'true'},
{'name': 'title', 'type': 'Edm.String', 'searchable': 'true', 'retrievable': true},
{'name': 'duration', 'type': 'Edm.Int64', 'retrievable': 'true'},
{'name': 'frame_features', 'type': 'Edm.ComplexType', 'fields': [
{'name': 'adult', 'type': 'Edm.ComplexType', 'fields': [
{'name': 'adultScore', 'type': 'Edm.Double', 'retrievable': 'true', 'searchable': 'true', 'filterable': 'true'},
{'name': 'isAdultContent', 'type': 'Edm.Boolean', 'facetable': 'true', 'filterable': 'true'},
{'name': 'isRacyContent', 'type': 'Edm.Boolean', 'facetable': 'true', 'filterable': 'true'},
{'name': 'racyScore', 'type': 'Edm.Double', 'retrievable': 'true', 'searchable': 'true', 'filterable': 'true'}
]},
{'name': 'categories', 'type': 'Collection(Edm.ComplexType)', 'fields': [
{'name': 'name', 'type': 'Edm.String', 'searchable': 'true', 'retrievable': 'true'},
{'name': 'score', 'type': 'Edm.Double', 'retrievable': 'true', 'searchable': 'true', 'filterable': 'true'}
]},
{'name': 'description', 'type': 'Edm.ComplexType', 'fields': [
{'name': 'captions', 'type': 'Collecton(Edm.ComplexType)', 'fields': [
{'name': 'coonfidence', 'type': 'Edm.Double', 'retrievable': 'true', 'searchable': 'true', 'filterable': 'true'},
{'name': 'text', 'type': 'Edm.String', 'searchable': 'true', 'retrievable': 'true'}
]},
{'name': 'tags', 'type': 'Collection(Edm.String)', 'searchable': 'true', 'retrievable': 'true', 'sortable': 'true'}
]},
{'name': 'tags', 'type': 'Collection(Edm.ComplexType)', 'fields': [
{'name': 'confidence', 'type': 'Edm.Double', 'retrievable': 'true', 'searchable': 'true', 'filterable': 'true'},
{'name': 'name', 'type': 'Edm.String', 'searchable': 'true'}
]}
]}
]
}

def create_index(index_schema):
    url = azure_search_endpoint + 'indexes' + api_version
    response = requests.post(url, headers=headers, json=index_schema)
    index = response.json()
    print(index)
    
def insert(index_name, data):
    url = endpoint + 'indexes/' + index_name + '/docs/index' + api_version
    payload = {
    'value': data
    }
    response = requests.post(url, eaders=header, json=payload)
    index_content = response.json()
    print(index_content)
    
def search(index_name, search_query):
    url = endpoint + 'indexes/' + index_name + '/docs' + api_version + search_query
    response = requests.get(url, headers=headers, json=search_query)
    query_result = response.json()
    print(query_result)
    return query_result