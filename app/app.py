from flask import Flask, request, jsonify
from AnalicerIA.application.EmotionClassiferService import EmotionClassifierService
from QuestionAnswerIA.application.SummaryService import SummaryService

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/EmotionClassifer', methods=['POST'])
def EmotionClassifer():
    data = request.get_json();
    texto_analizar= data['text'];
    return jsonify(EmotionClassifierService().classify(str(texto_analizar)))

@app.route('/Summary', methods=['POST'])
def Summary():
    data = request.get_json();
    question = data['question'];
    context = data['context'];
    return jsonify(SummaryService().summarize(str(question), str(context)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)