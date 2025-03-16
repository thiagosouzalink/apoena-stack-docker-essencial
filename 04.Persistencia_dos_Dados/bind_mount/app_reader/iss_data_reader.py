import os

import pandas as pd


output_dir = "/app/data/" # Considerando Filesystem do Container
output_file = os.path.join(output_dir, "iss_position.csv")

print(pd.read_csv(output_file))