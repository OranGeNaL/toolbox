import flet as ft
from tools import base64converter

HEIGHT = 500

def main(page: ft.Page):
    def page_resize(e):
        tool_cards_view.width = int(page.width * 0.3)
        for tool in available_tools:
            tool.page_resized((page.width, page.height))
    # add/update controls on Page
    # page = HEIGHT
    page.on_resize=page_resize
    
    tool_cards_view = ft.ListView(expand=1, spacing=10, padding=20, width=10)
    tool_ui_container = ft.Container(content=ft.Text("Выберите инструмент..."))
    
    available_tools = [base64converter.Base64Converter(pg_tool_ui=tool_ui_container, pg=page)]
        
    for tool in available_tools:
        tool_cards_view.controls.append(tool.tool_card)
    
    page.add(ft.Row(
            [
                tool_cards_view,
                # ft.Container(
                #     width=300,
                #     content=tool_cards_view,
                #     bgcolor=ft.colors.GREY_600),
                tool_ui_container
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ))
    
    

    

ft.app(target=main)