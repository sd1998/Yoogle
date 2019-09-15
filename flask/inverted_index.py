import csv
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
import re
import json
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class InvertedIndex:

    def __init__(self):
        self.inverted_index = {}
        self.firebase_credentials = credentials.Certificate('../serviceAccountKey.json')
        self.firebase = firebase_admin.initialize_app(self.firebase_credentials, {
        'databaseURL': 'https://htn2019-e1074.firebaseio.com'
        })
        self.stopwords = set(stopwords.words('english'))
        if os.path.exists('inverted_index.json'):
            self.inverted_index = self.read_index_file('inverted_index.json')
        else:
            db.reference('/').listen(self.listener)

    def remove_stopwords(self, tokens):
        tokens_wo_stopwords = []
        for i in range(0,len(tokens)):
            if tokens[i].lower() not in self.stopwords:
                tokens_wo_stopwords.append(tokens[i].lower())
        return tokens_wo_stopwords

    def get_pos_tag(self, token):
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

    def lemmatize(self, tokens):
        lemmatizer = WordNetLemmatizer()
        for i in range(0,len(tokens)):
            tokens[i] = lemmatizer.lemmatize(tokens[i],pos=str(get_pos_tag(tokens[i])))
        return tokens

    def add_to_inverted_index(self, tokens,data):
        for i in range(0,len(tokens)):
            if tokens[i] not in self.inverted_index:
                self.inverted_index[tokens[i]] = [data]
            else:
                self.inverted_index[tokens[i]].append(data)

    def listener(self, event):
        print(event)
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
                        self.add_to_inverted_index([tag['name']], {
                        'confidence': tag['confidence'],
                        'video': key,
                        'frame_no': i + 1
                        })
        self.save(self.inverted_index, 'inverted_index.json')
        print(self.inverted_index)

    def search(self, word):
        if word in self.inverted_index:
            result = {}
            for doc in self.inverted_index[word]:
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

    def save(self, inverted_index, filename):
        with open(filename, 'w') as file:
            json.dump(self.inverted_index, file)

    def read_index_file(self, index_file_name):
        with open(index_file_name,'r') as file:
            return json.load(file)
