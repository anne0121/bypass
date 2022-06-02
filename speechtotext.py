from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = "<your_apikey"
url = "<your_link>"

# Setup Service
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

# Perform conversion
with open({your_file},'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/mp3').get_result()
print(res)
text = res['results'][0]['alternatives'][0]['transcript']

print(text)
