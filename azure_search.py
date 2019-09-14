import requests

azure_search_endpoint = 'https://htn-bitplease.search.windows.net/'
headers = {
'Content-Type': 'application/json',
'api-key': '68C76C8D11203B3952A579820A398AD3'
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
    if data[0]['title'] == '5 Minutes on Tech: Everything You Need to Know about USB-C and Thunderbolt 3':
        print(payload)
    response = requests.post(url, headers=headers, json=payload)
    index_content = response.json()
    print(index_content)
    
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