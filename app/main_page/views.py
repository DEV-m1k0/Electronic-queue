import flet as ft
from main_page.components.texts import TitleText
from main_page.components.data_tables import TicketsDataTable


async def view(page: ft.Page):

    title = ft.Container(
        content=TitleText(value="Электронная очередь\nСтуденческого Центра БГТУ «Военмех»", text_align=ft.TextAlign.CENTER),
        alignment=ft.alignment.center
    )


    dt = TicketsDataTable(
        columns=[
            ft.DataColumn(ft.Text("Талон")),
            ft.DataColumn(ft.Text("Стол")),
            ft.DataColumn(ft.Text("ФИО")),
            ft.DataColumn(ft.Text("Группа"))
        ]
    )

    dt_container = ft.Container(
        content=ft.Column(
            controls=[
                dt
            ],
            scroll=ft.ScrollMode.ALWAYS
        ),
        adaptive=True,
        alignment=ft.alignment.center,
        height=250,
    )

    for _ in range(10):
        dt.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text("BC5346")),
                    ft.DataCell(ft.Text("12")),
                    ft.DataCell(ft.Text("Князев Антон Николаевич")),
                    ft.DataCell(ft.Text("ИС-33к"))
                ]
            ),
        )

    page.add(
        title,
        dt_container
    )