import tkinter as tk
from password_manager import PasswordManager

class PasswordManagerApp:
    def __init__(self, root):
        self.manager = PasswordManager()
        self.root = root
        self.root.title("Gestor de Contraseñas")
        
        # Crear botones y colocar en la ventana
        self.add_button = tk.Button(root, text="Agregar Contraseña", command=self.add_password)
        self.add_button.pack(pady=10)
        
        self.view_button = tk.Button(root, text="Ver Contraseñas", command=self.view_passwords)
        self.view_button.pack(pady=10)
        
        self.search_button = tk.Button(root, text="Buscar Contraseña", command=self.search_password)
        self.search_button.pack(pady=10)
        
        self.delete_button = tk.Button(root, text="Eliminar Contraseña", command=self.delete_password)
        self.delete_button.pack(pady=10)
        
    def add_password(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Agregar Contraseña")

        tk.Label(add_window, text="Sitio:").grid(row=0, column=0)
        tk.Label(add_window, text="Usuario:").grid(row=1, column=0)
        tk.Label(add_window, text="Contraseña:").grid(row=2, column=0)

        site_entry = tk.Entry(add_window)
        site_entry.grid(row=0, column=1)
        user_entry = tk.Entry(add_window)
        user_entry.grid(row=1, column=1)
        pwd_entry = tk.Entry(add_window)
        pwd_entry.grid(row=2, column=1)

        def save_password():
            site = site_entry.get()
            username = user_entry.get()
            password = pwd_entry.get()
            self.manager.add_password(site, username, password)
            add_window.destroy()

        tk.Button(add_window, text="Guardar", command=save_password).grid(row=3, columnspan=2, pady=10)

    def view_passwords(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Ver Contraseñas")
        
        passwords = self.manager.get_all_passwords()
        row = 0
        for site, (username, password) in passwords.items():
            tk.Label(view_window, text=f"Sitio: {site}").grid(row=row, column=0)
            tk.Label(view_window, text=f"Usuario: {username}").grid(row=row, column=1)
            tk.Label(view_window, text=f"Contraseña: {password}").grid(row=row, column=2)
            row += 1

    def search_password(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Buscar Contraseña")

        tk.Label(search_window, text="Sitio:").grid(row=0, column=0)
        site_entry = tk.Entry(search_window)
        site_entry.grid(row=0, column=1)

        def show_password():
            site = site_entry.get()
            result = self.manager.get_password(site)
            if result:
                username, password = result
                tk.Label(search_window, text=f"Usuario: {username}").grid(row=2, column=0)
                tk.Label(search_window, text=f"Contraseña: {password}").grid(row=2, column=1)
            else:
                tk.Label(search_window, text="Sitio no encontrado").grid(row=2, columnspan=2)

        tk.Button(search_window, text="Buscar", command=show_password).grid(row=1, columnspan=2, pady=10)
    
    def delete_password(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Eliminar Contraseña")

        tk.Label(delete_window, text="Sitio:").grid(row=0, column=0)
        site_entry = tk.Entry(delete_window)
        site_entry.grid(row=0, column=1)

        def confirm_delete():
            site = site_entry.get()
            self.manager.delete_password(site)
            delete_window.destroy()

        tk.Button(delete_window, text="Eliminar", command=confirm_delete).grid(row=1, columnspan=2, pady=10)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
