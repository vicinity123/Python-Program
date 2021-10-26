from youtube import youtube
import re

# Video class
class Video:
    def __init__(self, ids):
        self.ids = ids
        vid_req = youtube.videos().list(
            part="contentDetails, snippet, statistics",
            id=self.ids
        )
        global vid_resp, vid_items
        vid_resp = vid_req.execute()
        vid_items = vid_resp["items"][0]

    def get_video_id(self):
        return self.ids

    def get_channel_id(self):
        return vid_items["snippet"]["channelId"]

    def get_likes(self):
        return vid_items["statistics"]["likeCount"]

    def get_duration(self):
        pass

vid1 = Video("19E9RQC5kDo")

output = vid1.get_likes()
print(output)
