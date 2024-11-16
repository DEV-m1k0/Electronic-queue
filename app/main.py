import flet as ft
from main_page.views import view


async def main(page: ft.Page):
    page.title = "Flet Timer example"
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(), color_scheme_seed=ft.colors.RED)
    page.adaptive = True

    await view(page)


ft.app(main)