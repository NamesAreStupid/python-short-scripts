import subprocess
import os

lamePath = "C:\Program Files (x86)\lame3.99.5\lame.exe"

# tags
tagArtist = " --ta "
tagTitle = " --tt "
tagGenre = " --tg "
tagAlbum = " --tl "
tagYear = " --ty "
tagTrack = " --tn "

# additional lame options
lameQualityPreset = "-V 2"

# !!!insert manually!!!
genre = "17"  # Rock
year = "1980"

bitrate = " -b320 "
sourceDir = "E:\Musik\Motörhead\Ace Of Spades (1980)"
destinationDir = sourceDir + "\mp3\\"

# global lame tags
ty = tagYear + year
tg = tagGenre + genre


source = ""
destination = ""

# python is too stupid to correctly handle a different directory
# easiest fix was to change the cwd
# changes cwd to sourceDir for ease of use
os.chdir(sourceDir)
for fn in os.listdir(sourceDir):
    # print(os.path.isfile(fn))
    # if os.path.isfile(fn):
    if fn.endswith('.wav'):
        full_path = os.path.realpath(fn)
        pathAlbum, filename = os.path.split(full_path)
        pathArtist, album = os.path.split(pathAlbum)
        musicPath, artist = os.path.split(pathArtist)
        # remove year from album
        album = album.replace(' (' + year + ')', '')
        title = filename.replace('.wav', '')
        track, title = title.split(' ', 1)
        # make tags
        ta = tagArtist + '"' + artist + '" '
        tt = tagTitle + '"' + title + '" '
        tl = tagAlbum + '"' + album + '" '
        tn = tagTrack + '"' + track + '" '
        # lameTagArray = [lamePath, ta, tt, tl, tn, tg, ty, bitrate, full_path, destination]
        lameTagArray = [lamePath, tl, bitrate, ' "' + full_path + '"', '"' + destination + '"']
        # use lame for conversion
        if not os.path.exists(destinationDir):
            os.makedirs(destinationDir)
        destination = destinationDir + track + ' ' + title + '.mp3'
        subprocess.run(lamePath + ta + tt + tl + tn + ty + tg + bitrate + ' \"' + full_path + '\" \"' + destination + '\"')
        # THe fuckign array jsut wont work... no idea why
        # subprocess.run(lameTagArray)
'''            print('Artist: ' + artist)
            print('Album: ' + album)
            print('Title: ' + title)
            print('Track: ' + track)
'''
'''
            print(fn)
            print(fn2)

            print("Path at terminal when executing this file")
            print(os.getcwd() + "\n")

            print("This file path, relative to os.getcwd()")
            print(fn + "\n")

            print("This file full path (following symlinks)")
            full_path = os.path.realpath(fn)
            print(full_path + "\n")

            print("This file directory and name")
            path, filename = os.path.split(full_path)
            print(path + ' --> ' + filename + "\n")

            print("This file directory only")
            print(os.path.dirname(full_path))
'''