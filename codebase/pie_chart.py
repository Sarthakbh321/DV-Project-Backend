import matplotlib.pyplot as plt
import pandas
import base64
import io

def percentage(pct, data):
    absolute = int(pct / 100. * sum(data))
    return "{:.1f}%\n({:d})".format(pct, absolute)

def generatePieChart(params):
    column_list = ["sl_no", "gender", "ssc_p", "ssc_b", "hsc_p", "hsc_b", "hsc_s", "degree_p", "degree_t", "workexp",
                   "etest_p", "specialisation", "mba_p", "status", "salary"]

    df = pandas.read_csv("codebase/datasets/dataset.csv", usecols=column_list)

    if(params["filter"]["gender"] != "both"):
        df = df[(df["gender"] == params["filter"]["gender"])]

    labels = df[params["x_axis"]]

    labelArr = []
    countArr = []

    for (label, count) in labels.value_counts().iteritems():
        labelArr.append(label)
        countArr.append(count)

    plt.clf()

    plt.title("Generated Chart")
    patches, texts, junk = plt.pie(countArr, labels=labelArr, autopct=lambda pct: percentage(pct, countArr))

    if (params["filter"]["legend"]):
        plt.legend(patches, labelArr)

    bytes = io.BytesIO()

    plt.savefig(bytes, format="jpg")
    bytes.seek(0)

    b64 = base64.b64encode(bytes.read()).decode("ascii")

    return b64