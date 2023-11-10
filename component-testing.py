import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    tool_ui_container = ft.Column(controls=[
                    ft.Text(value="Текст"),
                    ft.TextField(tooltip="Текст"),
                    ft.Row(controls=[
                                      ft.TextButton(text="Конвертировать"),
                                      ft.TextButton(text="Из буфера в поле"),
                                      ft.TextButton(text="Из буфера в буфер")
                                  ]),
                    
                    
                    ft.Text(value="Base64"),
                    ft.TextField(tooltip="Base64 текст"),
                    ft.Row(controls=[
                                      ft.TextButton(text="Конвертировать"),
                                      ft.TextButton(text="Из буфера в поле"),
                                      ft.TextButton(text="Из буфера в буфер")
                                  ])
            ])
    
    page.add(ft.Row(
            [
                tool_ui_container
            ]
        ))
    

ft.app(target=main)