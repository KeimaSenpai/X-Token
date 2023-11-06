import flet as ft
from flet import alignment, Container, alignment, Page, Stack, Column, ElevatedButton, TextField, Image
import requests
import re


def main(page: Page):
    global url, username, password, btn
    page.title = "XToken"
    page.window_width = 390
    page.window_height = 400
    page.window_resizable = False
    page.padding = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def on_submit(e):
        try:
            token = extract_token(url, username, password)
            save_token(token)
        except:
            print('No se pudo hacer nada')

    def extract_token(url, username, password):
        # Hacer una solicitud HTTP a la página de inicio de sesión de Moodle
        session = requests.Session()
        login_url = url.value + '/login/index.php'
        response = session.get(login_url)

        # Buscar el token en la respuesta
        token_pattern = r'name="logintoken" value="([^"]+)"'
        match = re.search(token_pattern, response.text)
        if not match:
            raise ValueError(
                'No se pudo encontrar el token de inicio de sesión')
        token = match.group(1)

        # Iniciar sesión en Moodle
        data = {
            'username': username.value,
            'password': password.value,
            'logintoken': token,
        }
        response = session.post(login_url, data=data)

        if 'MoodleSession' not in session.cookies:
            raise ValueError('No se pudo encontrar el token de sesión')
        session_token = session.cookies['MoodleSession']
        return session_token

    def save_token(token):
        print(token)
        with open('token.txt', 'w') as f:
            f.write(token)

    logo = Image('bg.png', height=130)
    url = TextField(label='URL Moodle', height=40,
                    text_size=15, border_color='#FF0066', border_radius=10)
    username = TextField(label='Ususario', height=40,
                         text_size=15, border_color='#FF0066', border_radius=10)
    password = TextField(label='Contraseña', height=40,
                         text_size=15, border_color='#FF0066', border_radius=10, password=True, can_reveal_password=True)
    btn = Container(ElevatedButton(text='Generar', color='#D41872',
                                   bgcolor='#191919', on_click=on_submit, data=page), margin=10)

    # Centro
    contenido = ft.Column([
        url,
        username,
        password
    ])

    def column_with_horiz_alignment(align: ft.CrossAxisAlignment):
        return Column(
            [
                Container(
                    Column([logo, contenido, btn],
                           alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                           horizontal_alignment=align,
                           ),
                ),
            ]
        )

    page.add(Stack([
        ft.Row(
            [
                column_with_horiz_alignment(ft.CrossAxisAlignment.CENTER)
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    ]),

    )


ft.app(target=main, assets_dir="assets")
