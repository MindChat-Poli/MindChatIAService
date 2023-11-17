import QuestionAnswerIA.domain.SummaryIA as SummaryIA

class SummaryService:
    def __init__(self):
        self.summaryIA = SummaryIA.EmotionClassifier()

    def summarize(self, question, context):
        payload = {"question": question, "context": context}
        return self.summaryIA.query(payload)