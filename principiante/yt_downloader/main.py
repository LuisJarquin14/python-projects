import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp
import webbrowser

class YTDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")

        # URL Entry
        self.url_label = tk.Label(root, text="URL del Video de YouTube:")
        self.url_label.pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        # Previsualizar Button
        self.preview_button = tk.Button(root, text="Previsualizar Video", command=self.preview_video)
        self.preview_button.pack()

        # Descargar Button
        self.download_button = tk.Button(root, text="Descargar Video", command=self.download_video)
        self.download_button.pack()

        # Estado del video
        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

    def preview_video(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Advertencia", "Por favor, introduce una URL válida.")
            return

        try:
            webbrowser.open(url)
            self.status_label.config(text="Previsualizando el video...")
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el navegador: {e}")

    def download_video(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Advertencia", "Por favor, introduce una URL válida.")
            return
    
        download_path = filedialog.askdirectory()
        if not download_path:
            return
    
        try:
            options = {
                'format': 'best',
                'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            }
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])
            self.status_label.config(text="Descarga completada.")
            messagebox.showinfo("Éxito", "Descarga completada.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al descargar el video: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = YTDownloader(root)
    root.mainloop()



