from moviepy.audio.io.AudioFileClip import AudioFileClip
from pytube import YouTube
import logger, os


def download(url):
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