from threading import Thread
from moviepy.audio.io.AudioFileClip import AudioFileClip
from pytube import Playlist, YouTube
import logger, os, time

processes = []
qCountMax = 5

def manager(url, type):
    if 'list' in url:
        playlist(url, type)
    single(url, type)

def playlist(url, type):
    pL = Playlist(url)
    for videoUrl in pL.video_urls:
        #p = multiprocessing.Process(target=single, args=[videoUrl, type])
        p = Thread(target=single, args=[videoUrl, type])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    return

def single(url, type):
    if "mp3" in type:
        yT = YouTube(url)
        yD = yT.streams.get_audio_only()
        try:
            logger.debug('Baixando arquivo de vídeo!')
            baixarMp4 = yD.download("Músicas")
        except:
            logger.error("Não foi possível baixar o arquivo!")
        novoArquivo = baixarMp4.replace('.mp4', '.mp3')
        audioFile = AudioFileClip(baixarMp4, nbytes=4)
        try:
            logger.debug('Convertendo mp4 para mp3!')
            audioFile.write_audiofile(novoArquivo)
        except:
            logger.error('Não foi possível converter o mp4 para mp3!')
        try:
            logger.debug('Deletando arquivo mp4 extra!')
            os.remove(baixarMp4)
        except:
            logger.error('Não foi possível deletar o arquivo mp4 extra! (' + baixarMp4 + ')')
    elif "mp4" in type:
        yTVideo = YouTube(url)
        try:
            logger.debug('Baixando arquivo de vídeo!')
            yTVideo.streams.get_highest_resolution().download("Videos")
        except:
            logger.error("Não foi possível baixar o arquivo!")