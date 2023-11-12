import requests

class EmotionClassifier:
    def __init__(self):
        self.API_URL = "https://api-inference.huggingface.co/models/daveni/twitter-xlm-roberta-emotion-es"
        self.headers = {"Authorization": "Bearer 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"}

    def query(self, payload):
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        return response.json()
