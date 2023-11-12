from flask import Flask, request, jsonify
from AnalicerIA.application.EmotionClassiferService import EmotionClassifierService

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/EmotionClassifer', methods=['POST'])
def EmotionClassifer():
    data = request.get_json();
    texto_analizar= data['text'];
    return jsonify(EmotionClassifierService().classify(str(texto_analizar)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)