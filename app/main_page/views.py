import flet as ft
from main_page.components.texts import TitleText, DataTableColumnText
from main_page.components.data_tables import TicketsDataTable
from .button_logic import back, get_ticket

async def view(page: ft.Page):

    title, dt_container, get_ticket_container = await get_controls()

    page.add(
        ft.TextButton("Назад", on_click=back),
        title,
        dt_container,
        get_ticket_container
    )




async def get_controls() -> list[ft.Control]:
    title = ft.Container(
        content=TitleText(value="Электронная очередь\nСтуденческого Центра БГТУ «Военмех»", text_align=ft.TextAlign.CENTER),
        alignment=ft.alignment.center
    )


    dt = TicketsDataTable(
        columns=[
            ft.DataColumn(DataTableColumnText("Талон")),
            ft.DataColumn(DataTableColumnText("Стол")),
            ft.DataColumn(DataTableColumnText("ФИО")),
            ft.DataColumn(DataTableColumnText("Группа"))
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
        height=300,
        margin=ft.margin.only(top=50, bottom=50)
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


    get_ticket_container = ft.Container(
        content=ft.FilledButton("Получить талон", on_click=get_ticket),
        alignment=ft.alignment.center
    )

    return title, dt_container, get_ticket_container