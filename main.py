import flet as ft
import asyncio
import requests
import re


async def main(page: ft.Page):
    global url, username, password, btn
    page.title = "XToken"
    page.window_width = 390
    page.window_height = 390
    page.window_resizable = False
    page.padding = 0

    # async def on_submit(e):
    #     await extract_token(url, username, password)

    # async def extract_token(url, username, password):
    #     # Hacer una solicitud HTTP a la página de inicio de sesión de Moodle
    #     session = requests.Session()
    #     login_url = url + '/login/index.php'
    #     response = session.get(login_url)

    #     # Buscar el token en la respuesta
    #     token_pattern = r'name="logintoken" value="([^"]+)"'
    #     match = re.search(token_pattern, response.text)
    #     if not match:
    #         raise ValueError(
    #             'No se pudo encontrar el token de inicio de sesión')
    #     token = match.group(1)

    #     # Iniciar sesión en Moodle
    #     data = {
    #         'username': username,
    #         'password': password,
    #         'logintoken': token,
    #     }
    #     response = session.post(login_url, data=data)

    #     # Buscar el token de sesión en las cookies
    #     if 'MoodleSession' not in session.cookies:
    #         raise ValueError('No se pudo encontrar el token de sesión')
    #     session_token = session.cookies['MoodleSession']

    # return await session_token

    # async def save_token(token):
    #     # Guardar el token en un archivo de texto
    #     with open('token.txt', 'w') as f:
    #         f.write(token)

    logo = ft.Image('bg.png', height=130)
    url = ft.TextField(label='URL Moodle', height=40,
                       text_size=15, border_color='#FF0066', border_radius=10)
    username = ft.TextField(label='Ususario', height=40,
                            text_size=15, border_color='#FF0066', border_radius=10)
    password = ft.TextField(label='Contraseña', height=40,
                            text_size=15, border_color='#FF0066', border_radius=10)
    btn = ft.ElevatedButton(text='Generar', color='#D41872',
                            bgcolor='#191919', data=page)

    # Centro
    contenido = ft.Column([
        logo,
        url,
        username,
        password,
        btn
    ])

    # Fondo de la app
    fondo = ft.Container(contenido, width=390, height=390,
                         bgcolor='#191919', padding=20)
    await page.add_async(fondo)


ft.app(target=main)
