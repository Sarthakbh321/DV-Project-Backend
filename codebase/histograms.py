import matplotlib.pyplot as plt
import pandas
import base64
import io

def generateHistogram(params):
    column_list = ["sl_no", "gender", "ssc_p", "ssc_b", "hsc_p", "hsc_b", "hsc_s", "degree_p", "degree_t", "workexp",
                   "etest_p", "specialisation", "mba_p", "status", "salary"]

    df = pandas.read_csv("codebase/datasets/dataset.csv", usecols=column_list)

    if(params["filter"]["gender"] != "both"):
        df = df[(df["gender"] == params["filter"]["gender"])]

    if (params["filter"]["subjects"] != "all"):
        df = df[(df["degree_t"] == params["filter"]["subjects"])]

    labels = df[params["x_axis"]]


    plt.clf()
    
    plt.hist(labels, 50)
    plt.xlabel(params["x_axis"])
    plt.ylabel(params["y_axis"])
    plt.title("Generated Graph")

    bytes = io.BytesIO()

    plt.savefig(bytes, format="jpg")
    bytes.seek(0)

    b64 = base64.b64encode(bytes.read()).decode("ascii")

    return b64