import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64

def extract_frame_features(frame_file_name):
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '592f656df9a242e69bb91c3a8406338d',
    }

    params = urllib.parse.urlencode({
        'visualFeatures': 'Categories,Tags,Description,Faces,ImageType,Color,Adult',
        'details': 'Celebrities,Landmarks',
        'language': 'en',
    })

    try:
        conn = http.client.HTTPSConnection('htn-bitplease.cognitiveservices.azure.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, open(frame_file_name, 'rb'), headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
        return data
    except Exception as e:
        raise RuntimeError(e)
