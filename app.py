import base64
from flask import Flask, jsonify
from codebase.gender_wise import GenderWisePlacementAnalysis
import PIL

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/graph')
def get_graph():
    analysis = GenderWisePlacementAnalysis()
    result = analysis.generateGraph()

    res = {
        "image": base64.b64encode(result)
    }

    return jsonify(res)



if __name__ == '__main__':
    app.run()
