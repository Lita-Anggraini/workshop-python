import json
from urllib import request

url = "https://www.bps.go.id/indikator/indikator/download_json/0000/api_pub/WVRlTTcySlZDa3lUcFp6czNwbHl4QT09/da_03/1"

response = request.urlopen(url)

data = json.loads(response.read())

#print(data)
for prov in data['data']:
    print(f"- {prov['label']}:")
    print(f"  populasi: {prov['nzudy5elv7']} Ribu")

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)