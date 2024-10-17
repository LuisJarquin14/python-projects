# Automatización de Emails

Esta herramienta permite enviar correos electrónicos de manera automatizada a través de una interfaz gráfica.

## Requisitos

- Python 3.x
- Bibliotecas:

  - smtplib
  - email
  - tkinter

**Recuerda que estas bibliotecas ya vienen instaladas en python y no debes instalarlas**

## Instalación

1. Clona este repositorio:

   ```sh
   git clone https://github.com/LuisJarquin14/python-projects.git
   ```

2. Navega al directorio del proyecto:

   ```sh
   cd automatizacion_emails
   ```

## Uso

1. Abre el archivo `email_sender.py` y remplaza `tu_email@gmail.com` y `tu_contrasena` con tus credenciales de Gmail.

- si no sabes como optener tu contraseña, puedes utilizar el siguiente enlace: https://myaccount.google.com/u/4/apppasswords?rapt=AEjHL4OKHBDK9YugcH9t6izhWE1_71rn2vmZl15RTGy7vP3H7LVNgVsKDsaexf8xviRN1dTjaL1soZyUbyPEPKTKeP2K62Ea0Auuv7nEgAewqfdDTpwcSAs

**Recuerda que la contrasena no es la misma que la de Gmail, sino una contrasena generada de forma aleatoria**

2. Ejecuta el script principal:

   ```sh
   python main.py
   ```

3. Ingresa el destinatario, el asunto y el cuerpo del correo en la interfaz y presiona "Enviar".

# Notas

- **No es seguro almacenar contraseñas directamente en el código. Considera utilizar métodos más seguros para manejar credenciales, como variables de entorno o gestores de secretos.**

- **Si usas Gmail, asegúrate de permitir "acceso a aplicaciones menos seguras" en tu cuenta o configurar OAuth para una autenticación más segura.**
