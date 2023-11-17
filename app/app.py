from flask import Flask, request, jsonify
from google.cloud import language_v2
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

@app.route('/test')
def sample_analyze_sentiment(text_content: str = "I am so happy and joyful.") -> None:
    """
    Analyzes Sentiment in a string.

    Args:
      text_content: The text content to analyze.
    """

    client = language_v2.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    document_type_in_plain_text = language_v2.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language_code = "en"
    document = {
        "content": text_content,
        "type_": document_type_in_plain_text,
        "language_code": language_code,
    }

    # Available values: NONE, UTF8, UTF16, UTF32
    # See https://cloud.google.com/natural-language/docs/reference/rest/v2/EncodingType.
    encoding_type = language_v2.EncodingType.UTF8

    response = client.analyze_sentiment(
        request={"document": document, "encoding_type": encoding_type}
    )
    # Get overall sentiment of the input document
    print(f"Document sentiment score: {response.document_sentiment.score}")
    print(f"Document sentiment magnitude: {response.document_sentiment.magnitude}")
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(f"Sentence text: {sentence.text.content}")
        print(f"Sentence sentiment score: {sentence.sentiment.score}")
        print(f"Sentence sentiment magnitude: {sentence.sentiment.magnitude}")

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(f"Language of the text: {response.language_code}")
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)