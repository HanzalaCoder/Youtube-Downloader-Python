import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
import threading


def select_download_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        download_folder_entry.delete(0, tk.END)
        download_folder_entry.insert(0, folder_path)


def download_video():
    download_button.config(state=tk.DISABLED)
    select_folder_button.config(state=tk.DISABLED)

    video_url = video_url_entry.get()
    download_folder = download_folder_entry.get()

    download_thread = threading.Thread(target=download_video_thread, args=(video_url, download_folder))
    download_thread.start()


def download_video_thread(video_url, download_folder):
    try:
        yt = YouTube(video_url)
        title = yt.title
        video_url_label.config(text=f"{title}")

        video = yt.streams.get_highest_resolution()
        show_label.config(text="DOWNLOAD HAS STARTED>>>")
        video.download(download_folder)
        messagebox.showinfo("COMPLETE", "YOU VIDEO HAS BEEN DOWNLOADED")
    except Exception:
        messagebox.showerror("FAILED", "MAYBE BAD CONNECTION OR CHECK YOUR LINK?")
        show_label.config(text="ERROR ERROR")
    finally:
        download_button.config(state=tk.NORMAL)
        select_folder_button.config(state=tk.NORMAL)
        show_label.config(text="DOWNLOAD COMPLETE!")


root = tk.Tk()
root.title("HANZALA PROJECTS")
root.geometry("350x330")
root.resizable(False, False)
root.config(bg="#555c5b")

video_url_label = tk.Label(root, text="PASTE URL HERE", width=45, height=2, font=("Aerial", 10), bg="#1a1918",
                           fg="#4cc70a")
download_folder_label = tk.Label(root, text="SELECT FOLDER", width=45, height=2, font=("Aerial", 10), bg="#1a1918",
                                 fg="#4cc70a")
show_label = tk.Label(root, text="SHOW STATUS", width=45, height=3, font=("Aerial", 10), bg="#1a1918", fg="#4cc70a")

video_url_entry = tk.Entry(root, width=80, font=("Aerial", 12))
download_folder_entry = tk.Entry(root, width=50, font=("Aerial", 12))

select_folder_button = tk.Button(root, text="SELECT PATH", command=select_download_folder, width=22, height=4,
                                 bg="#1a1918", fg="#4cc70a", activebackground="#1a1918", font=("Aerial", 10))
download_button = tk.Button(root, text="DOWNLOAD", command=download_video, width=20, height=4,
                            bg="#1a1918", fg="#4cc70a", activebackground="#1a1918", font=("Aerial", 10))

video_url_label.place(x=0)
video_url_entry.place(x=5, y=40)
show_label.place(x=0, y=280)
download_folder_entry.place(x=5, y=100)
download_folder_label.place(x=0, y=60)
select_folder_button.place(x=0, y=205)
download_button.place(x=170, y=205)

root.mainloop()
