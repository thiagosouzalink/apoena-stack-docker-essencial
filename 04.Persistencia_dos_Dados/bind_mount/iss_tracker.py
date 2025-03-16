from datetime import datetime
import json
import urllib.request
import os

import pandas as pd


output_dir = "/app/data/" # Considerando Filesystem do Container
output_file = os.path.join(output_dir, "iss_position.csv")

url = "http://api.open-notify.org/iss-now.json"

with urllib.request.urlopen(url) as response:
    if response.status == 200:
        print("Chama ok")
        data = response.read()
        obj = json.loads(data)
        
        timestamp = obj["timestamp"]
        latitude = obj["iss_position"]["latitude"]
        longitude = obj["iss_position"]["longitude"]
        
        date_time = datetime.fromtimestamp(timestamp)
        date_ = date_time.date()
        time_ = date_time.time()
        
        df = pd.DataFrame(
            {
                "Date": [date_],
                "Time": [time_],
                "Latitude": [latitude],
                "Longitude": [longitude]
            }
        )
        
        df.to_csv(output_file, index=False)
        print(f"Dados escritos em: {output_file}")
        print(pd.read_csv(output_file))
    else:
        print(f"Erro na chamada: {response.status}")