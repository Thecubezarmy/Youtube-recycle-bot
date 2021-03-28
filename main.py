import queryfunction
from pytube import YouTube
from moviepy.editor import *
import re
from os import listdir
import os
from moviepy import *
import time
from natsort import natsorted

#the tmp folder that is created to host the files
tgt_folder = "\youtube-recycle-bot\output"

#input
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

#downloads the files
for x in listofsongs:
    z=queryfunction.youtubequery(x)
    youtube_link = z
    w = YouTube(youtube_link).streams.first()
    w.download(output_path="\youtube-recycle-bot\output")



#converts the mp4 to mp3 (make sure to change the output path so it does not interfere with the other code)
#for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
 #full_path = os.path.join(tgt_folder, file)
 #output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
 #clip = mp.AudioFileClip(full_path)
 #clip.write_audiofile(output_path)

#renames the files for easier converion
filecounter = 0
for file_name in listdir(tgt_folder):
 os.rename(tgt_folder + "\\"+ file_name,tgt_folder + "\\"+"Video"+str(filecounter)+".mp4")
 filecounter = filecounter + 1

#end=False
#first = 0
#second = 1
fin = 0
#vid = "Video"
#this thing does not work but i'm keeping it anyway
#for file_name in listdir(tgt_folder):
    #try:
     #clip1= VideoFileClip(tgt_folder + "\\"+vid+str(first)+".mp4")
     #clip2= VideoFileClip(tgt_folder + "\\"+"Video"+str(second)+".mp4")
    #except IOError:
        #pass
    #final_clip= concatenate_videoclips([clip1,clip2])
    #final_clip.write_videofile(tgt_folder+"zfinal"+ str(fin)+".mp4",codec='libx264')
    #time.sleep(3)
    #os.remove(tgt_folder + "\\"+"Video"+str(first)+".mp4")
    #os.remove(tgt_folder + "\\"+"Video"+str(second)+".mp4")
    #fin = first
    #vid = "zfinal"
    #second = second+1


#this makes all the small mp4 files into a big mp4 file
L =[]
for root, dirs, files in os.walk(tgt_folder):

    #files.sort()
    files = natsorted(files)
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)

final_clip = concatenate_videoclips(L)
final_clip.to_videofile(tgt_folder+"final"+ str(fin)+".mp4", fps=24, remove_temp=True)

for file_name in listdir(tgt_folder):
    os.remove(tgt_folder + "\\"+ file_name)



