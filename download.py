#Program to download Yotube music
#Author: Jack Cloudman

import pafy,os,shutil
from pydub import AudioSegment as convert
#Create song list
if os.path.exists('songs.txt'):
    pass
else:
    print("Creating songs.txt....")
    document= open('songs.txt','w')
    print("Paste yours songs in songs.txt")
    document.close()
#create directory
if os.path.exists('music'):
    if os.path.exists('music/temp'):
        pass
    else:
        os.mkdir('music/temp')
else:
    os.mkdir('music')
    os.mkdir('music/temp')
document = open('songs.txt','r')
music_list = document.readlines()
document.close()
error_list=[]
print("Download music....")
for music in music_list:
    try:
        url = music
        video = pafy.new(url)
        bestaudio = video.getbestaudio()
        bestaudio.download(filepath="music/temp/")
    except:
        error_list.append("Error download: "+music)
print("Converting to mp3.....")
for filename in os.listdir('music/temp/'):
    try:
        audio = convert.from_file('music/temp/'+filename)
        name = os.path.splitext(filename)
        audio.export('music/'+name[0]+'.mp3',format="mp3",bitrate="160k")
    except:
        error_list.append("Error convert: "+name[0])
shutil.rmtree("music/temp")
for error in  error_list:
    print(error)
print("Finished!")
