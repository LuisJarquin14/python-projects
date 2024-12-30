import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
from pygame import mixer
import os


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Initialize Pygame mixer with custom settings
        mixer.init(frequency=44100, size=-16, channels=2, buffer=1024)

        # Variables
        self.playlist = []
        self.current_index = 0
        self.is_playing = False
        self.audio_length = 0
        self.update_interval = 100  # Update every 100 ms (0.1s)
        self.is_paused = False  # Track if the music is paused
        self.volume = tk.DoubleVar()
        self.volume.set(0.5)  # Volumen inicial al 50%
        mixer.music.set_volume(self.volume.get())

        # Create menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.load_music)
        file_menu.add_command(label="Remove", command=self.remove_music)
        file_menu.add_command(label="Exit", command=self.root.quit)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About Us", command=self.show_about)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Music title label
        self.music_title = tk.Label(
            self.root, text="No music playing", font=("Helvetica", 14))
        self.music_title.pack(pady=10)

        # Playlist box
        self.playlist_box = tk.Listbox(
            self.root, selectmode=tk.SINGLE, bg="lightyellow", fg="black", font=("Helvetica", 12))
        self.playlist_box.pack(fill=tk.BOTH, padx=15, pady=10, expand=True)
        self.playlist_box.bind('<<ListboxSelect>>', self.select_music)

        # Control frame
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=20)

        # Previous button
        prev_button = tk.Button(
            control_frame, text="⏮️", command=self.play_prev)
        prev_button.grid(row=0, column=0, padx=10)

        # Play/Pause button
        self.play_pause_button = tk.Button(
            control_frame, text="▶️", command=self.toggle_play_pause)
        self.play_pause_button.grid(row=0, column=1, padx=10)

        # Stop button
        stop_button = tk.Button(
            control_frame, text="⏹️", command=self.stop_music)
        stop_button.grid(row=0, column=2, padx=10)

        # Next button
        next_button = tk.Button(
            control_frame, text="⏭️", command=self.play_next)
        next_button.grid(row=0, column=3, padx=10)

        # Control de volumen
        volume_frame = tk.Frame(self.root)
        volume_frame.pack(pady=10)
        volume_label = tk.Label(volume_frame, text="🔊 Volumen")
        volume_label.pack(side=tk.LEFT)
        volume_scale = tk.Scale(volume_frame, from_=0, to=1, orient=tk.HORIZONTAL, resolution=0.01,
                                variable=self.volume, command=self.change_volume)
        volume_scale.pack(side=tk.RIGHT)

        # Progress bar
        self.progress = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL,
                                 length=500, showvalue=0, command=self.seek_music)
        self.progress.pack(pady=10)

        # Duration label
        self.duration_label = tk.Label(
            self.root, text="00:00 / 00:00", font=("Helvetica", 12))
        self.duration_label.pack(pady=10)

    def load_music(self):
        files = filedialog.askopenfilenames(
            filetypes=[("Audio Files", "*.mp3 *.wav")])
        if files:
            for file in files:
                try:
                    self.playlist.append(file)
                    self.playlist_box.insert(tk.END, os.path.basename(file))
                except Exception as e:
                    messagebox.showerror(
                        "Error", f"No se pudo cargar {file}: {e}")
            # Evitar la reproducción automática al agregar canciones
            if not self.is_playing:
                return
            else:
                self.play_music()  # Solo si ya estaba reproduciendo

    def remove_music(self):
        selected_song_index = self.playlist_box.curselection()
        if selected_song_index:
            self.playlist_box.delete(selected_song_index)
            del self.playlist[selected_song_index[0]]
            # Adjust current index if needed
            if self.current_index >= len(self.playlist):
                self.current_index = len(self.playlist) - 1
            if self.current_index >= 0:  # Play the previous song if available
                self.play_music()
            else:
                self.stop_music()

    def play_music(self):
        if self.playlist:
            try:
                self.current_index = self.playlist_box.curselection(
                )[0] if self.playlist_box.curselection() else self.current_index
                mixer.music.load(self.playlist[self.current_index])
                mixer.music.play()
                self.is_playing = True
                self.is_paused = False
                self.update_title()
                self.update_duration()
                self.start_progress_update()
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo reproducir la música: {e}")  # Error message

    def toggle_play_pause(self):
        if self.is_playing:
            if self.is_paused:
                mixer.music.unpause()  # Unpause music
                self.is_paused = False
                self.play_pause_button.config(text="⏸️")  # Pause icon
            else:
                mixer.music.pause()  # Pause music
                self.is_paused = True
                self.play_pause_button.config(text="▶️")  # Play icon
        else:
            self.play_music()

    def stop_music(self):
        mixer.music.stop()
        self.is_playing = False
        self.is_paused = False  # Reset pause state
        self.progress.set(0)
        self.duration_label.config(text="00:00 / 00:00")
        self.play_pause_button.config(text="▶️")  # Reset play icon

    def play_next(self):
        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            self.play_music()
        else:
            self.stop_music()  # Stop if at the end of the playlist

    def play_prev(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.play_music()
        else:
            self.stop_music()  # Stop if at the beginning of the playlist

    def select_music(self, event):
        if self.playlist_box.curselection():
            self.current_index = self.playlist_box.curselection()[0]
            self.play_music()

    def update_title(self):
        self.music_title.config(text=os.path.basename(
            self.playlist[self.current_index]))

    def show_about(self):
        messagebox.showinfo(
            "About Us", ("Music Player\n\n" "Created with Python and Tkinter.\n" "Version: 1.0.0\n" "Date of Creation: December 7, 2024\n\n" "This application allows you to play your favorite music " "files (mp3, wav) with features such as play, pause, stop, " "next, previous, and seek. Developed by a passionate team " "of developers to provide an intuitive and enjoyable user experience."))

    def update_duration(self):
        if self.playlist:
            audio_length = mixer.Sound(
                self.playlist[self.current_index]).get_length()
            self.audio_length = audio_length
            minutes = int(audio_length // 60)
            seconds = int(audio_length % 60)
            self.duration_label.config(
                text=f"00:00 / {minutes:02}:{seconds:02}")

    def start_progress_update(self):
        self.update_progress_bar()

    def update_progress_bar(self):
        if self.is_playing:
            current_pos = mixer.music.get_pos() / 1000  # Position in seconds
            minutes = int(current_pos // 60)
            seconds = int(current_pos % 60)
            total_minutes = int(self.audio_length // 60)
            total_seconds = int(self.audio_length % 60)
            self.duration_label.config(
                text=f"{minutes:02}:{seconds:02} / {total_minutes:02}:{total_seconds:02}")
            self.progress.set((current_pos / self.audio_length) * 100)
            # Schedule the next update
            if self.is_playing:
                self.root.after(self.update_interval, self.update_progress_bar)

    def seek_music(self, value):
        if self.is_playing:
            pos = float(value) / 100 * self.audio_length
            mixer.music.set_pos(pos)  # Use set_pos to set the position
        else:
            pos = float(value) / 100 * self.audio_length
            # Use play with start parameter only if not playing
            mixer.music.play(start=pos)

    def change_volume(self, value):
        mixer.music.set_volume(float(value))


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
