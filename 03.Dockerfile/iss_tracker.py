from datetime import datetime
import json
import urllib.request

import pandas as pd


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
        
        print("Posição da ISS atualmente:")
        print(df.to_string(index=False))
    else:
        print(f"Erro na chamada: {response.status}")