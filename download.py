from __future__ import unicode_literals
import youtube_dl

youtube_video = input("Give me the link to the youtube video: ")

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print (msg)

def my_hook(d):
    if d['status'] == 'finished':
        print ('Done downloading')

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': './output/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([youtube_video])
