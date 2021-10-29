from youtube import youtube
import re


# Video class
class Video:
    def __init__(self, vid_id):
        self.vid_id = vid_id
        vid_req = youtube.videos().list(
            part="contentDetails, snippet, statistics",
            id=self.vid_id
        )
        global vid_resp
        vid_resp = vid_req.execute()

    def get_response(self):
        return vid_resp

    def get_vid_id(self):
        return self.vid_id

    def get_channel_id(self):
        return vid_resp["items"][0]["snippet"]["channelId"]

    def get_likes(self):
        return vid_resp["items"][0]["statistics"]["likeCount"]

    def get_duration(self):
        pass


vid1 = Video("19E9RQC5kDo")

output = vid1.get_response()
print(output)
