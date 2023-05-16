from pytube import YouTube
import os
from sys import argv

link = argv[1]

cwd = os.getcwd()
dir_path = os.path.join(cwd, "youtube_videos")

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

yt = YouTube(link)
print("Title: ", yt.title)
print("View, ", yt.views)
yd = yt.streams.get_highest_resolution()
# yd.download(r"C:\Users\Chidalu.Chukwuneke\Documents\Projects\yt_downloader\videos")
yd.download(dir_path)
