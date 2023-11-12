import AnalicerIA.domain.EmotionClassifierModel as EmotionClassifier

class EmotionClassifierService:
    def __init__(self):
        self.emotionClassifier = EmotionClassifier.EmotionClassifier()

    def classify(self, text):
        payload = {"inputs": text}
        return self.emotionClassifier.query(payload)