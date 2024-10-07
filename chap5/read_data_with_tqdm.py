from tqdm import tqdm
import pandas as pd






spotify_data = [".\spotify_data\dataset-of-00s.csv", ".\data\spotify_data\dataset-of-10s.csv", ".\data\spotify_data\dataset-of-60s.csv",
    ".\data\spotify_data\dataset-of-70s.csv",
    ".\data\spotify_data\dataset-of-80s.csv", ".\data\spotify_data\dataset-of-90s.csv"]

all_data = {}
failures = []


for file_name in tqdm(spotify_data):
    try:
        all_data[file_name] = pd.read_csv(file_name)

    except Exception:
        failures.append(file_name)
        print(file_name)