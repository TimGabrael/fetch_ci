from datetime import datetime
import requests
import os
current_date = datetime.now().strftime("%Y-%m-%d")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'x-games-auth-bypass': 'true'
}

url = f"https://api.spiegel.raetselzentrale.com/api/v3/l/spiegel/kreuzwortraetsel?channel=www.spiegel.de"
folder = "spiegel"
os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, f"{current_date}.json");
response = requests.get(url, headers=headers);
if response.status_code == 200:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)

suedeutsche_datetime = datetime.now().strftime("%Y%m%d");
url = f"https://www.sueddeutsche.de/tools/spiele/kreuzwortraetsel/iframe?currentDate={suedeutsche_datetime}"
folder = "sueddeutsche"

os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, f"{current_date}.html");

response = requests.get(url, headers=headers);

if response.status_code == 200:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)

url = "https://www.nytimes.com/svc/crosswords/v6/puzzle/mini.json"
folder = "nyt/mini"

os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, f"{current_date}.json");

response = requests.get(url, headers=headers);

if response.status_code == 200:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)

url = "https://www.nytimes.com/svc/crosswords/v6/puzzle/midi.json"
folder = "nyt/midi"

os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, f"{current_date}.json");

response = requests.get(url, headers=headers);

if response.status_code == 200:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)

url = "https://www.nytimes.com/svc/crosswords/v6/puzzle/daily.json"
folder = "nyt/daily"

os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, f"{current_date}.json");

response = requests.get(url, headers=headers);

if response.status_code == 200:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)