import tkinter as t
from views.menu_principal import abrir_menu
from views import Login
from controllers.auth_login import token

def menu():
    if token():
        abrir_menu(nombre=None)
    else:
        datos_login = Login.login()
        if datos_login["exito"]:
            abrir_menu(nombre=datos_login["nombre"])

menu()

