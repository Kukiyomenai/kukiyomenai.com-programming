#app.py
from yt_dlp import YoutubeDL

ytdlp_option = YoutubeDL({'format': 'mp4'})
ytdlp_option.download(['https://youtu.be/TjOp7FZfGqI?si=xQjRTk3AJK_jjFsl'])