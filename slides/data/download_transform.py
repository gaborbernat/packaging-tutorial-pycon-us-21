import json
from pathlib import Path
from datetime import datetime
from itertools import groupby

data = json.loads(Path("downloads.json").read_text()) + json.loads(Path("downloads_new.json").read_text())

# per week
# data = [{
#     'download_date': datetime.fromisocalendar(key[0], key[1], 1).isoformat(),
#     'download_count': sum(j[1] for j in group)} for key, group in
#     groupby([(datetime.fromisoformat(i["download_date"]).isocalendar()[0:2], i["download_count"]) for i in data],
#             key=lambda i: i[0])]

# per month
data = [{
    'download_date': key.isoformat(),
    'download_count': sum(j[1] for j in group)} for key, group in
    groupby([(datetime.fromisoformat(i["download_date"]).replace(day=1), i["download_count"]) for i in data],
            key=lambda i: i[0])]

result = {
    "chart": {"zoomType": "x"},
    "title": {"text": "download per day"},
    "xAxis": {"type": "datetime"},
    "yAxis": {"title": {"text": "Download count"}},
    "legend": {"enabled": False},
    "series": [
        {
            "type": "area",
            "name": "# download",
            "data": [
                [
                    datetime.fromisoformat(i["download_date"]).timestamp() * 1000,
                    i["download_count"],
                ]
                for i in data
            ],
        }
    ],
}

print(json.dumps(result))
