
import flet as ft
from src.controllers.controller import Controller

def main(page: ft.Page):
    page.title = "Mon App MVC"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    app_controller = Controller()

    page.add(app_controller.get_view())

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")