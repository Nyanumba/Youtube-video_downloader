import yt_dlp

# Entering the URL for the video
url = input("Enter the video link: ")

# Set the output directory to your internal storage
output_directory = "/This PC/Downloads"

ydl_opts = {
    'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully!")
