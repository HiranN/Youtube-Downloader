from pytube import YouTube
import logger

def download(url):
    yTVideo = YouTube(url)
    try:
        logger.debug('Baixando arquivo de vídeo!')
        yTVideo.streams.get_highest_resolution().download("Videos")
    except:
        logger.error("Não foi possível baixar o arquivo!")