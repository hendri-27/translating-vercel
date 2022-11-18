from flask import Flask, jsonify, request
import os
from googletrans import Translator

def translate(text,src="id",tgt="en"):
    translator = Translator()
    result = translator.translate(text, tgt, src)
    return result.text

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def index():
    data = request.get_json()
    text = data['text']
    model = (data['model']).split("_")
    for i in range(9):
        text = translate(text,model[i],model[i+1])
        
    return jsonify({"output": text})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
