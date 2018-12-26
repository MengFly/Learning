import pandas as pd
import json

data = pd.read_excel(r"data.xlsx")

result = []
for index, row in data.iterrows():
    item = {"name": row[0],
            "logo": row[1],
            "url": row[2]}
    result.append(item)

data_json = json.dumps(result, ensure_ascii=False)

with open("result.json", "w", encoding="utf8") as f:
    f.write(data_json)
