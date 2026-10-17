import pandas as pd

def generate_report(records):

    data = []

    for row in records:

        data.append({

            "timestamp":
            row.timestamp,

            "compliance":
            row.compliance,

            "masked":
            row.masked,

            "unmasked":
            row.unmasked
        })

    df = pd.DataFrame(data)

    report_path = "report.csv"

    df.to_csv(
        report_path,
        index=False
    )

    return report_path