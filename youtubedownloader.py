import yt_dlp
import tkinter as tk
from tkinter import ttk, messagebox
from tqdm import tqdm
import threading

# Function to download the video in the background
def download_video():
    url = url_entry.get()
    
    if url:
        ydl_opts = {
            'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
            'progress_hooks': [download_progress_hook]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
                messagebox.showinfo("Success", "Video downloaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error downloading video: {str(e)}")
    else:
        messagebox.showerror("Error", "Please enter a video link.")

# Function to update the progress bar
def download_progress_hook(data):
    if data['status'] == 'downloading':
        percent = data['_percent_str']
        download_bar.config(value=data['_percent'])
        status_label.config(text=f"Downloading: {percent}")
    elif data['status'] == 'finished':
        download_bar.config(value=100)
        status_label.config(text="Download complete")

# function to start the download process in a separate thread
def start_download_thread():
    download_thread = threading.Thread(target=download_video)
    download_thread.start()

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Set the output directory to your internal storage
output_directory = "/This PC/Downloads"

# Create a frame with a background color
frame = tk.Frame(window, bg="midnightblue", padx=80, pady=100)
frame.pack(fill="both", expand=True)

# Create a label and an entry field for entering the video link
url_label = tk.Label(frame, text="Enter the video link:", bg= "navy", fg="white")
url_label.pack(pady=5)
url_entry = tk.Entry(frame, width=40)
url_entry.pack(pady=5)

# Create a download button with a background color
download_button = tk.Button(frame, text="Download Video", command=start_download_thread, bg="blue", fg="white")
download_button.pack(pady=10)

# Create a progress bar
download_bar = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
download_bar.pack(pady=10)

# Create a label to display status
status_label = tk.Label(frame, text="", bg="lightgray")
status_label.pack(pady=5)

# Function to start the download process in a separate thread
def start_download_thread():
    download_thread = threading.Thread(target=download_video)
    download_thread.start()

# Start the GUI event loop
window.mainloop()
