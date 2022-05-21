from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin

import speechToText
from utils.utils import decodeSound
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/towav", methods=['GET'])
@cross_origin()
def wav():
    return render_template('to_wav.html')

@app.route("/shopping", methods=['GET'])
@cross_origin()
def shop():
    return render_template('shopping.html')

@app.route("/donate", methods=['GET'])
@cross_origin()
def donate():
    return render_template('donate.html')

@app.route("/payment", methods=['GET'])
@cross_origin()
def payment():
    return render_template('payment.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['sound']
    decodeSound(image, "audio123.wav")
    result = speechToText.speech2Text("audio123.wav")
    return jsonify({"Result" : str(result)})



if __name__ == "__main__":
    app.run(host='192.168.1.9', port=5000, debug=True)