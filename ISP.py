class ShortVideo:
    def GetShortVideo(self):
        ...


class LongVideo:
    def GetLongVideo(self):
        ...

class MultiVideo(ShortVideo, LongVideo):
    def __init__(self):
        ...

TikTok = ShortVideo()
Twitch = LongVideo()
YouTube = MultiVideo()