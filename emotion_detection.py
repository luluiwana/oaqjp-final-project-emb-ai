import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=input_json)
    
    data = json.loads(response.text)

    emotion_dict = {'anger': data['emotionPredictions'][0]['emotion']['anger'],
    'disgust': data['emotionPredictions'][0]['emotion']['disgust'],
    'fear': data['emotionPredictions'][0]['emotion']['fear'],
    'joy': data['emotionPredictions'][0]['emotion']['joy'],
    'sadness': data['emotionPredictions'][0]['emotion']['sadness']}
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    emotion_dict['dominant_emotion'] = dominant_emotion
    return emotion_dict
   
    



