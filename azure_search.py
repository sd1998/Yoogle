import requests

azure_search_endpoint = 'https://htn-bitplease.search.windows.net/'
headers = {
'Content-Type': 'application/json',
'api-key': '<api_key>'
}
api_version = '?api-version=2019-05-06'

def create_index(index_schema):
    if not index_exists(index_schema['name']):
        url = azure_search_endpoint + 'indexes' + api_version
        response = requests.post(url, headers=headers, json=index_schema)
        index = response.json()
        print(index)
    else:
        print('Index already exists')
        delete_index(index_schema['name'])
        create_index(index_schema)

def index_exists(index_name):
    url = azure_search_endpoint + 'indexes' + api_version + '&$select=name'
    response  = requests.get(url, headers=headers)
    index_list = response.json()
    for index in index_list.get('value'):
        if index.get('name') == index_name:
            return True
    return False

def insert(index_name, data):
    url = azure_search_endpoint + 'indexes/' + index_name + '/docs/index' + api_version
    payload = {
    'value': data
    }

def delete_index(index_name):
    url = azure_search_endpoint + 'indexes/' + index_name + api_version
    response = requests.delete(url, headers=headers)
    print(response)

def search(index_name, search_query):
    url = azure_search_endpoint + 'indexes/' + index_name + '/docs' + api_version + search_query
    response = requests.get(url, headers=headers, json=search_query)
    query_result = response.json()
    print(query_result)
    return query_result
