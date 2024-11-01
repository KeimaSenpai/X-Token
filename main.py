import json
import time
import flet as ft
import requests


def main(page: ft.Page):
    global url, username, password, btn
    page.title = "XToken"
    page.window.width = 390
    page.window.height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def on_submit(e):
        try:
            token_li = extract_token(url, username, password)
            print(token_li)
            copy_token(token_li)
        except:
            print('No se pudo hacer nada')
            text_status.value = 'No se pudo generar nada'
            page.update()

    text_status = ft.Text('', color='#FF0066')

    def copy_token(token_li):
        page.set_clipboard(token_li)
        
        # Crear un SnackBar y agregarlo a page.overlay
        snack_bar = ft.SnackBar(content=ft.Text("Texto copiado al portapapeles"))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    def extract_token(url, username, password):
        # Hacer una solicitud HTTP a la página de inicio de sesión de Moodle
        r = requests.get(f'{url.value}/login/token.php?username={username.value}&password={password.value}&service=moodle_mobile_app')
        token = json.loads(r.text)['token']
        return token
    

    logo = ft.Image('image.png', height=130)
    url = ft.TextField(
        label='URL Moodle', 
        height=40,
        text_size=15, 
        border_color='#FF0066', 
        border_radius=10,
        cursor_color='#FF0066',
        label_style= ft.TextStyle(
            color='#FF0066'
        ),
    )
    username = ft.TextField(
        label='Ususario', 
        height=40,
        text_size=15, 
        border_color='#FF0066', 
        border_radius=10,
        cursor_color='#FF0066',
        label_style= ft.TextStyle(
            color='#FF0066'
        ),
    )
    password = ft.TextField(
        label='Contraseña', 
        height=40,
        text_size=15, 
        border_color='#FF0066', 
        border_radius=10, password=True, 
        can_reveal_password=True,
        cursor_color='#FF0066',
        label_style= ft.TextStyle(
            color='#FF0066'
        ),
    )
    btn = ft.Container(
        ft.ElevatedButton(
                text='Generar', 
                color='#D41872',
                bgcolor='#191919', 
                on_click=on_submit, 
                data=page,
                adaptive=True,
            ), 
            margin=10
        )

    # Centro
    contenido = ft.Column(
        [
            url,
            username,
            password,
            btn,
            text_status,

        ],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    info_text = ''' 
XToken creado por ByteBloom. El cual permite la descargar y subir contenido sin gasto de megas. Todo es por una suscripción para poder disfrutar de todo en la app. 

'''

    dlg = ft.AlertDialog(
        title=ft.Text(
            f"XToken 1.0.1",
            size=15,
            ),
        content=ft.Column(
            spacing = 5,
            controls=[
                ft.Image(src='image.png', height=70),
                ft.Text(info_text,size=12,),
                ft.Row(
                    spacing = 4,
                    controls=[
                        ft.IconButton(
                            ft.icons.SEND,
                            # content=ft.Image(src='image/telegram.webp', height=30, width=30),
                            style=ft.ButtonStyle(
                                color="#5B0098",
                                bgcolor="#0C0C0C",
                                shape=ft.RoundedRectangleBorder(radius=5),
                            ),
                            on_click=lambda _: page.launch_url("https://t.me/+uMnCUP8to8owMjFh"),

                        
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        adaptive=True
    )

    page.appbar = ft.AppBar(
        # leading=ft.Icon(ft.icons.CLOUD, color='#FF0066'),
        leading_width=30,
        title=ft.Text("XToken", color='#FF0066', weight=ft.FontWeight.BOLD),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(
                ft.icons.INFO, 
                icon_color='#FF0066',
                on_click=lambda e: page.open(dlg)
            )
        ]
    )



    page.add(ft.Column(
            controls=[
                logo,
                contenido,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    ),


ft.app(target=main, assets_dir="assets")
