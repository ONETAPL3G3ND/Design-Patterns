from abc import ABC, abstractmethod

class Video(ABC):
    @abstractmethod
    def play(self):
        pass

class ShortVideo(Video):
    def play(self):
        return "Playing a short video."

class LongVideo(Video):
    def play(self):
        return "Playing a long video."

class VideoPlayer:
    def __init__(self, video: Video):
        self.video = video

    def play_video(self):
        return self.video.play()

short_video = ShortVideo()
long_video = LongVideo()

short_video_player = VideoPlayer(short_video)
long_video_player = VideoPlayer(long_video)

print(short_video_player.play_video())
print(long_video_player.play_video())
