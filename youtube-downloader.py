from pytube import YouTube

# https://github.com/nficano/pytube
# python -m venv venv
# .\venv\Scripts\activate
# pip install pytube3 --upgrade

#videourl = 'https://www.youtube.com/watch?v=U7CZcd-UYmU0'


print('test136')
videourl = input("Video URL: ")
from pytube import YouTube
video = YouTube(videourl)
video.streams[0].download()


#streams = video.streams.filter(res='1080p', mime_type='video/mp4')