import base64
from flask import Flask, jsonify, request
from codebase.gender_wise import GenderWisePlacementAnalysis
import PIL
from codebase.subject_wise import SubjectWisePlacementAnalysis
from codebase.bar_chart import generateBarChart
from codebase.pie_chart import generatePieChart
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/graph')
def get_graph():
    analysis = GenderWisePlacementAnalysis()
    result = analysis.generateGraph()

    subjectWise = SubjectWisePlacementAnalysis()
    result1 = subjectWise.generateGraph()

    res = {
        "image": result,
        "image2": result1
    }

    return jsonify(res)

@app.route('/generate', methods=["POST"])
def generate():
    print("HI")
    if(request.method == "POST"):
        params = request.json['params']

        if(params["chart"] == "bar"):
            b64 = generateBarChart(params)
        elif(params["chart"] == "pie"):
            b64 = generatePieChart(params)

        res = {
            "image": b64
        }

        return jsonify(res)

    return "NOT GET"


if __name__ == '__main__':
    app.run()
