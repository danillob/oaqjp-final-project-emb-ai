import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = input_json, headers = header)
    
    if response.status_code == 200:
        response_json = json.loads(response.text)

        highest_score = 0
        dominant_emotion = ''
    
        for k, v in response_json['emotionPredictions'][0]['emotion'].items():
            if v > highest_score:
                highest_score = v
            dominant_emotion = k

        emotions = {
            'anger': response_json['emotionPredictions'][0]['emotion']['anger'],
            'disgust': response_json['emotionPredictions'][0]['emotion']['disgust'],
            'fear': response_json['emotionPredictions'][0]['emotion']['fear'],
            'joy': response_json['emotionPredictions'][0]['emotion']['joy'],
            'sadness': response_json['emotionPredictions'][0]['emotion']['sadness'],
            'dominant_emotion': dominant_emotion
        }
    
    elif response.status_code == 400:
        emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    return emotions
