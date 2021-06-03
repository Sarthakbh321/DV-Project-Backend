import matplotlib.pyplot as plt
import pandas
import base64
import io

def generateBarChart(params):
    column_list = ["sl_no", "gender", "ssc_p", "ssc_b", "hsc_p", "hsc_b", "hsc_s", "degree_p", "degree_t", "workexp",
                   "etest_p", "specialisation", "mba_p", "status", "salary"]

    df = pandas.read_csv("codebase/datasets/dataset.csv", usecols=column_list)

    if(params["filter"]["gender"] != "both"):
        df = df[(df["gender"] == params["filter"]["gender"])]

    if(params["filter"]["subjects"] != "all"):
        df = df[(df["degree_t"] == params["filter"]["subjects"])]

    x = df[params["x_axis"]]
    y = df[params["y_axis"]]

    plt.clf()
    plt.xlabel(params["x_axis"])
    plt.ylabel(params["y_axis"])


    # xticks = [i for i in range(1, len(x) + 1)]
    # yticks = [i for i in range(1, len(y) + 1)]
    #
    # plt.xticks(xticks, x, rotation='vertical')
    # plt.yticks(yticks, y)


    plt.title("Generated Chart")

    plt.bar(x, y)

    bytes = io.BytesIO()

    plt.savefig(bytes, format="jpg")
    bytes.seek(0)

    b64 = base64.b64encode(bytes.read()).decode("ascii")

    return b64


if __name__ == '__main__':
    params = {"x_axis": "sl_no", "y_axis": "salary"}
    generateBarChart(params)





