import flet as ft



class TicketsDataTable(ft.DataTable):
    def __init__(self, columns: list[ft.DataColumn] = None, rows: list[ft.DataRow] = None):
        super().__init__(columns, rows)
        self.columns = columns
        self.rows = rows
        self.column_spacing = 20
        self.data_row_max_height = 60