import base64
from flask import Flask, jsonify
from codebase.gender_wise import GenderWisePlacementAnalysis
import PIL
from codebase.subject_wise import SubjectWisePlacementAnalysis

app = Flask(__name__)


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



if __name__ == '__main__':
    app.run()
