from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from boneFractureClassification.utils.common import decodeImage
from boneFractureClassification.pipeline.prediction import PredictionPipeline

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__, template_folder="./web/templates", static_url_path="/static", static_folder="./web/static")
CORS(app)

class ClassificationApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)
    
    
@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    os.system("dvc repro")
    return "Training successful!"

@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == "__main__":
    clApp = ClassificationApp()
    app.run(host="0.0.0.0", port=8080, debug=True)