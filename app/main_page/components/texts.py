import flet as ft


class TitleText(ft.Text):
    def __init__(self, value: str, text_align: ft.TextAlign = ft.TextAlign.START):
        super().__init__()
        self.value = value
        self.style = ft.TextStyle(size=16, weight=ft.FontWeight("bold"))
        self.text_align = text_align