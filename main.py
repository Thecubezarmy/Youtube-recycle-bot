import queryfunction
from pytube import YouTube
from moviepy.editor import *
import moviepy.editor as mp
import re
from os import listdir
import moviepy.editor


tgt_folder = "\youtube-recycle-bot\output"

print ("enter username")
username = input()
print("enter password")
password= input()
print("enter youtbe v3 data API key")
APIkey=input()
print("enter the number of songs")
videonumber=int(input())
listofsongs=[]
while videonumber > 0:
    print ("please type the name of the song")
    locallist=input()
    listofsongs.append(locallist)
    videonumber =  videonumber - 1

for x in listofsongs:
    z=queryfunction.youtubequery(x)
    youtube_link = z
    w = YouTube(youtube_link).streams.first()
    w.download(output_path="\youtube-recycle-bot\output")



#converts the mp4 to mp3
#for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
 #full_path = os.path.join(tgt_folder, file)
 #output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
 #clip = mp.AudioFileClip(full_path)
 #clip.write_audiofile(output_path)

filecounter = 0
for file_name in listdir(tgt_folder):
 os.rename(tgt_folder + "\\"+ file_name,tgt_folder + "\\"+"Video"+str(filecounter)+".mp4")
 filecounter = filecounter + 1

