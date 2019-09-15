import csv
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
import re
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

firebase_credentials = credentials.Certificate('../serviceAccountKey.json')

firebase = firebase_admin.initialize_app(firebase_credentials, {
'databaseURL': 'https://htn2019-e1074.firebaseio.com'
})

stopwords = set(stopwords.words('english'))

inverted_index = {}

if os.path.exists('inverted_index.pkl'):
    read()
    
bi_word_inverted_index = {}

def remove_stopwords(tokens):
    tokens_wo_stopwords = []
    for i in range(0,len(tokens)):
        if tokens[i].lower() not in stopwords:
            tokens_wo_stopwords.append(tokens[i].lower())
    return tokens_wo_stopwords
    
def get_pos_tag(token):
    pos_tag = nltk.pos_tag([token])[0][1]
    if pos_tag.startswith('N'):
        return wordnet.NOUN
    elif pos_tag.startswith('V'):
        return wordnet.VERB
    elif pos_tag.startswith('J'):
        return wordnet.ADJ
    elif pos_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
        
def lemmatize(tokens):
    lemmatizer = WordNetLemmatizer()
    for i in range(0,len(tokens)):
        tokens[i] = lemmatizer.lemmatize(tokens[i],pos=str(get_pos_tag(tokens[i])))
    return tokens
    
def add_to_inverted_index(tokens,data):
    for i in range(0,len(tokens)):
        if tokens[i] not in inverted_index:
            inverted_index[tokens[i]] = [data] 
        else:
            inverted_index[tokens[i]].append(data)
                
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
            if 'tags' in value[key]['frame_features'][i]:
                for tag in value[key]['frame_features'][i]['tags']:
                    add_to_inverted_index([tag['name']], {
                    'confidence': tag['confidence'],
                    'video': key,
                    'frame_no': i + 1
                    })
    if not os.path.exists('inverted_index.pkl'):
        save(inverted_index, 'inverted_index.pkl')

def search(word):
    if word in inverted_index:
        result = {}
        for doc in inverted_index[word]:
            if doc['video'] in result:
                result[doc['video']].append({
                'confidence': doc['confidence'],
                'frame_no': doc['frame_no']
                })  
            else:
                result[doc['video']] = [{
                'confidence': doc['confidence'],
                'frame_no': doc['frame_no']
                }]    
        return result
    return None
    
def save(inverted_index,filename):
    with open(filename + '.pkl','wb') as index:
        pickle.dump(inverted_index,index,pickle.HIGHEST_PROTOCOL)
        
def read():
    with open("inverted_index.pkl",'rb') as file:
        inverted_index = pickle.load(file)    
                
db.reference('/').listen(listener)
