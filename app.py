from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
nlp = pipeline('conversational')

@app.route('/message', methods=['POST'])
def message():
    data = request.json
    user_message = data['message']
    response = nlp(user_message)
    return jsonify({'reply': response[0]['generated_text']})

if __name__ == '__main__':
    app.run(port=5001)