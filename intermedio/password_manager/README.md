# Gestor de Contraseñas

**¡Gestiona y almacena tus contraseñas de manera segura y eficiente!**

## Descripción

Esta aplicación te permite gestionar y almacenar tus contraseñas de manera segura utilizando una interfaz gráfica intuitiva. Con funcionalidades para agregar, ver, buscar y eliminar contraseñas, este gestor asegura que tus datos estén siempre protegidos mediante cifrado.

## Objetivos

- **Almacenar contraseñas de manera segura**
- **Recuperar contraseñas fácilmente**
- **Eliminar contraseñas no deseadas**
- **Buscar contraseñas por sitio web**

## Características

- **Agregar nueva contraseña:** Introduce y guarda contraseñas de manera segura.
- **Ver todas las contraseñas:** Visualiza todas las contraseñas almacenadas.
- **Buscar contraseñas:** Encuentra rápidamente la contraseña que necesitas.
- **Eliminar contraseñas:** Borra las contraseñas que ya no necesites.
- **Interfaz gráfica intuitiva:** Fácil de usar y visualmente atractiva gracias a Tkinter.
- **Cifrado de contraseñas:** Protege tus contraseñas utilizando la biblioteca `cryptography`.

## Requisitos Previos

- Python 3.x instalado en tu sistema.
- Conocimiento básico de programación en Python.
- Biblioteca `cryptography` instalada.

## Instalación

Clona el repositorio en tu máquina local usando:

```bash
git clone https://github.com/LuisJarquin14/python-projects.git
```

## Como Usar

1. Navega a la carpeta correspondiente:

   ```bash
   cd password_manager
   ```

2. Instala las dependencias:

   ```bash
   pip install cryptography
   ```

3. Ejecuta la aplicación:

   ```bash
   python main.py
   ```

4. Agregar una contraseña:

- Haz clic en Agregar Contraseña.
- Introduce el sitio, usuario y contraseña, luego haz clic en Guardar.

5. Ver todas las contrasenas:

- Haz clic en Ver Contraseñas para visualizar todas las contraseñas almacenadas.

6. Buscar una contraseña:

- Haz clic en Buscar Contraseña, introduce el sitio y haz clic en Buscar.

7. Eliminar una contraseña:

- Haz clic en Eliminar Contraseña, introduce el sitio y haz clic en Eliminar.

# Seguridad

- **Todas las contraseñas se almacenan cifradas utilizando la biblioteca cryptography, asegurando que tus datos estén siempre protegidos.**
