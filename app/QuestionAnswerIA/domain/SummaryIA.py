import requests

class EmotionClassifier:
    def __init__(self):
        self.API_URL = "https://api-inference.huggingface.co/models/mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"
        self.headers = {"Authorization": "Bearer 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"}

    def query(self, payload):
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        return response.json()