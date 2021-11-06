from link_params import link_extend, link_params
from youtube import youtube
import json
import re

# Get video's link return the video's details and the channel details
vid_link = "https://www.youtube.com/watch?v=JeznW_7DlB0&ab_channel=TechWithTim"
vid_id = link_params(vid_link)["v"]

vid_req = youtube.videos().list(
    part="contentDetails,snippet,statistics",
    id=vid_id
)
vid_resp = vid_req.execute()
vid_items = vid_resp["items"][0]

# Video details
vid_title = vid_items["snippet"]["title"]
vid_has_caption = bool(vid_items["contentDetails"]["caption"])
# ---------------------------------------------------
# Regex for video duration
duration = vid_items["contentDetails"]["duration"]
hours = re.search(r"([0-9]+)H", duration)
minutes = re.search(r"([0-9]+)M", duration)
seconds = re.search(r"([0-9]+)S", duration)

hours = int(hours.group(1)) if hours else 0
minutes = int(minutes.group(1)) if minutes else 0
seconds = int(seconds.group(1)) if seconds else 0
# ---------------------------------------------------
vid_duration = f"{hours}:{minutes}:{seconds}"
vid_likes = vid_items["statistics"]["likeCount"]
vid_dislikes = vid_items["statistics"]["dislikeCount"]
vid_views = vid_items["statistics"]["viewCount"]

# Channel Id for the channel request
channel_id = vid_items["snippet"]["channelId"]


# Channel Request
channel_req = youtube.channels().list(
    part="contentDetails,snippet,statistics",
    id=channel_id
)
channel_resp = channel_req.execute()
channel_items = channel_resp["items"][0]

# Channel Details
channel_title = channel_items["snippet"]["title"]
channel_views = channel_items["statistics"]["viewCount"]
channel_sub = channel_items["statistics"]["subscriberCount"]
channel_vid_count = channel_items["statistics"]["videoCount"]

# Write information about video and channel to a JSON file
write_to_file = {
    "video": {
        "title": vid_title,
        "id": vid_id,
        "has_captions": vid_has_caption,
        "duration": vid_duration,
        "likes": vid_likes,
        "dislikes": vid_dislikes,
        "views": vid_views
    },
    "channel": {
        "title": channel_title,
        "id": channel_id,
        "views": channel_views,
        "subscribers": channel_sub,
        "videoCount": channel_vid_count
    }
}

with open("video_channel.json", "w") as file:
    output = json.dumps(write_to_file, indent=2)
    file.write(output)
