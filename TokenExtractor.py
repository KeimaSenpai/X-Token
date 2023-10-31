import requests
import re
import tkinter as tk

def extract_token(url, username, password):
    # Hacer una solicitud HTTP a la página de inicio de sesión de Moodle
    session = requests.Session()
    login_url = url + '/login/index.php'
    response = session.get(login_url)

    # Buscar el token en la respuesta
    token_pattern = r'name="logintoken" value="([^"]+)"'
    match = re.search(token_pattern, response.text)
    if not match:
        raise ValueError('No se pudo encontrar el token de inicio de sesión')
    token = match.group(1)

    # Iniciar sesión en Moodle
    data = {
        'username': username,
        'password': password,
        'logintoken': token,
    }
    response = session.post(login_url, data=data)

    # Buscar el token de sesión en las cookies
    if 'MoodleSession' not in session.cookies:
        raise ValueError('No se pudo encontrar el token de sesión')
    session_token = session.cookies['MoodleSession']

    return session_token

def save_token(token):
    # Guardar el token en un archivo de texto
    with open('token.txt', 'w') as f:
        f.write(token)

# Crear la interfaz gráfica
def on_submit():
    url = url_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    try:
        token = extract_token(url, username, password)
        save_token(token)
        status_label.config(text='Token extraído y guardado en token.txt')
    except Exception as e:
        status_label.config(text=str(e))

root = tk.Tk()
root.title('Extractor de token de Moodle')

url_label = tk.Label(root, text='URL de Moodle:')
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

username_label = tk.Label(root, text='Nombre de usuario:')
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text='Contraseña:')
password_label.pack()
password_entry = tk.Entry(root, show='*')
password_entry.pack()

submit_button = tk.Button(root, text='Extraer token', command=on_submit)
submit_button.pack()

status_label = tk.Label(root, text='')
status_label.pack()

root.mainloop()
