import sys
import time
from pytube import YouTube,exceptions

def download(video):
  print('Título do vídeo: '+video.title)
  video.download()

previousprogress = 0
progress_info = ''
def progress_func(stream,chunck,bytes_remaining):
  global previousprogress
  global progress_info
  total_size = stream.filesize
  bytes_downloaded = total_size - bytes_remaining 

  liveprogress = (int)(bytes_downloaded / total_size * 100)
  if liveprogress > previousprogress:
    previousprogress = liveprogress

  progress_info = f"Progresso: {liveprogress}% [" + "=" * liveprogress+">" +"]"
  print(progress_info, end="\r")

def complete_func(a,b):
  print(progress_info)

def get_video(url):
  try:
    yt = YouTube(
      url,
      on_progress_callback=progress_func,
      on_complete_callback=complete_func
      )
  except:
    print(f'Vídeo {url} não pertence ao Youtube.')
    sys.exit()
  else:
    mp4_video = yt.streams.filter(progressive=True,file_extension='mp4').first()
    return mp4_video

def get_url():
  url = input('Insira a url do vídeo para baixar: ')
  return url.strip()

def main():
  print('--Youtube Downloader Video--')
  video_url = get_url()
  video = get_video(video_url)
  download(video)
  print('Download concluído com sucesso!')

main()