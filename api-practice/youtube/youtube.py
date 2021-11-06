from googleapiclient.discovery import build

PATH = "../../../Other/youtube_keys.txt"

with open(PATH, "r", encoding="utf-8") as f:
    api_key = f.read()

youtube = build("youtube", "v3", developerKey=api_key)
