from win10toast import ToastNotifier
from pytube import YouTube
import moviepy.editor as mp
import re 
import os

toaster = ToastNotifier()
link = input("Digite o link do vídeo que deseja baixar: ")
path = "Downloads"
yt = YouTube(link)

ys = yt.streams.filter(only_audio=True).first().download(path)

for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
toaster.show_toast(
    "",
    "pronto",
    threaded = True,
    icon_path = None,
    duration = 3
)