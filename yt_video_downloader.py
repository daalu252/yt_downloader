import tkinter as tk
import tkinter.messagebox
from pytube import YouTube
import os

cwd = os.getcwd()
dir_path = os.path.join(cwd, "youtube_videos")

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

top = tk.Tk()
top.title("Youtube Downloader")
top.geometry('400x200')
title = tk.Label(top, text="Enter Youtube link to download", font=("Helvetica", 24), fg='blue')

user_input = tk.Text(top, height=1, width=30)
user_input.pack()

link_entry = tk.Entry(top)


def download_video():
    link = user_input.get(1.0, "end-1c")
    video = YouTube(link)
    print("Title: ", video.title)
    print("View, ", video.views)
    video_download = video.streams.get_highest_resolution()
    video_download.download(dir_path)
    tk.messagebox.showinfo("Video Status", "Download Finished")


button = tk.Button(top, text="Click to Download Video", command=download_video)
button.pack()

top.mainloop()
