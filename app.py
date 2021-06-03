import base64
from flask import Flask, jsonify, request
from codebase.gender_wise import GenderWisePlacementAnalysis
import pandas
from codebase.subject_wise import SubjectWisePlacementAnalysis
from codebase.bar_chart import generateBarChart
from codebase.pie_chart import generatePieChart
from codebase.scatter_plot import generateScatterPlot
from flask_cors import CORS

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


@app.route("/stats")
def getStats():
    column_list = ["sl_no", "gender", "ssc_p", "ssc_b", "hsc_p", "hsc_b", "hsc_s", "degree_p", "degree_t", "workexp",
                   "etest_p", "specialisation", "mba_p", "status", "salary"]

    df = pandas.read_csv("codebase/datasets/dataset.csv", usecols=column_list)

    placed = df[(df["status"] == "Placed")]
    boysPlaced = placed[(placed["gender"] == "M")]
    girlsPlaced = placed[(placed["gender"] == "F")]

    res = {
        "total": len(df),
        "placed": len(placed),
        "boysPlaced": len(boysPlaced),
        "girlsPlaced": len(girlsPlaced),
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
        elif(params["chart"] == "scatter"):
            b64 = generateScatterPlot(params)

        res = {
            "image": b64
        }

        return jsonify(res)

    return "NOT GET"


if __name__ == '__main__':
    app.run()
