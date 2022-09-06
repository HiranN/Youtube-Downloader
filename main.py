from threading import Thread
from pytube import Playlist
import mp3, mp4, gui

debugVar = True
processes = []

def main():
    gui.open()
    #downloadManagerMp3("https://www.youtube.com/watch?v=D9G1VOjN_84&list=PLep4cGi16m4Oi_7Pq5Ai590sjKIsEgdgd")

def downloadPlaylist(url, target):
    pL = Playlist(url)
    for videoUrl in pL.video_urls:
        # p = multiprocessing.Process(target=target, args=[videoUrl])
        p = Thread(target=target, args=[videoUrl])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    return

def downloadManagerMp3(url):
    if 'list' in url:
        downloadPlaylist(url, mp3.download)
    mp3.download(url)

def downloadManagerMp4(url):
    if 'list' in url:
        downloadPlaylist(url, mp4.download)
    mp4.download(url)

if __name__ == '__main__':
        main()