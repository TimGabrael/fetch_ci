from datetime import datetime
import requests
import os
current_date = datetime.now().strftime("%Y-%m-%d")

url = f"https://spiele.spiegel.de/games/spiegel_Crosswords/js/data/levels/c003/{current_date}_9x9.json?_=1.14.112"
folder = "spiegel"

os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, f"{current_date}.json");

response = requests.get(url);

if response.status_code == 200:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)

suedeutsche_datetime = datetime.now().strftime("%Y%m%d");
url = f"https://www.sueddeutsche.de/tools/spiele/kreuzwortraetsel/iframe?currentDate={suedeutsche_datetime}"
folder = "sueddeutsche"

os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, f"{current_date}.html");

response = requests.get(url);

if response.status_code == 200:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)

url = "https://www.nytimes.com/svc/crosswords/v6/puzzle/mini.json"
folder = "nyt"

os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, f"{current_date}.json");

response = requests.get(url);

if response.status_code == 200:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)
