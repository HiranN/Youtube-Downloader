from threading import Thread
from pytube import YouTube, Playlist
import pyautogui, os, logger, time, mp3, mp4

debugVar = False
runningVar = True
processes = []

def main():
    yT = pyautogui.prompt(text='Digite o Link do Vídeo/Playlist:', title='Baixar vídeo!' , default='')
    if yT == None:
        return

    downloadType = "mp3"
    downloadType = pyautogui.prompt(text='Qual o formato a ser salvo?', title='Formatos: (mp3, mp4)' , default=downloadType)
    if not("mp3" in downloadType):
        if not ("mp4" in downloadType):
            print("errado")
            return

    start = time.time()

    if 'list' in yT:
        pL = Playlist(yT)

        for videoUrl in pL.video_urls:
            #p = multiprocessing.Process(target=downloadMp3, args=[videoUrl])
            if "mp3" in downloadType:
                p = Thread(target=mp3.download, args=[videoUrl])
            elif "mp4" in downloadType:
                p = Thread(target=mp4.download, args=[videoUrl])
            p.start()
            processes.append(p)
        for process in processes:
            process.join()
        return

    if "mp3" in downloadType:
        mp3.download(yT)
    elif "mp4" in downloadType:
        mp4.download(yT)

    end = time.time()
    print(end - start)

if __name__ == '__main__':
    while runningVar:
        main()