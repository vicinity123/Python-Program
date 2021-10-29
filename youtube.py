from googleapiclient.discovery import build

with open("../Other/api_keys.txt", "r", encoding="utf-8") as f:
    api_key = f.read()

youtube = build("youtube", "v3", developerKey=api_key)
