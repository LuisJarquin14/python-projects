import tkinter as tk
from tkinter import messagebox
from email_sender import send_email

def send_email_gui():
    to_email = entry_to.get()
    subject = entry_subject.get()
    body = text_body.get("1.0", tk.END)
    
    if to_email and subject and body:
        try:
            send_email(to_email, subject, body)
            messagebox.showinfo("Éxito", "Correo enviado exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al enviar el correo: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")

def create_gui():
    global entry_to, entry_subject, text_body

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Automatización de Emails")

    # Crear los widgets
    label_to = tk.Label(root, text="Para:")
    label_to.grid(row=0, column=0, padx=10, pady=10)
    entry_to = tk.Entry(root, width=50)
    entry_to.grid(row=0, column=1, padx=10, pady=10)

    label_subject = tk.Label(root, text="Asunto:")
    label_subject.grid(row=1, column=0, padx=10, pady=10)
    entry_subject = tk.Entry(root, width=50)
    entry_subject.grid(row=1, column=1, padx=10, pady=10)

    label_body = tk.Label(root, text="Cuerpo del correo:")
    label_body.grid(row=2, column=0, padx=10, pady=10)
    text_body = tk.Text(root, height=10, width=50)
    text_body.grid(row=2, column=1, padx=10, pady=10)

    button_send = tk.Button(root, text="Enviar", command=send_email_gui)
    button_send.grid(row=3, column=1, pady=10)

    # Ejecutar la aplicación
    root.mainloop()
