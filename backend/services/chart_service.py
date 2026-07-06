import matplotlib.pyplot as plt
import os

CHART_DIR = "backend/charts"

os.makedirs(CHART_DIR, exist_ok=True)


def generate_chart(file_id, analysis):

    tests = []
    values = []

    for item in analysis["abnormal_parameters"]:

        tests.append(item["parameter"])

        number = item["value"].split()[0]

        try:
            values.append(float(number.replace(",", "")))
        except:
            values.append(0)

    plt.figure(figsize=(10,5))

    plt.bar(tests, values)

    plt.xticks(rotation=60)

    plt.tight_layout()

    path = os.path.join(
        CHART_DIR,
        f"{file_id}.png"
    )

    plt.savefig(path)

    plt.close()

    return path