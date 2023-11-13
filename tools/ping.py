import flet
import ping3
from .tool import Tool

class Ping(Tool):
    def __init__(self, pg_tool_ui, pg):
        self.pg_tool_ui = pg_tool_ui
        self.pg = pg
        
        self.one_server_field = flet.TextField(hint_text="Один сервер", label="Один сервер")
        self.one_server_result = flet.Text(value="")
        self.snack_bar = flet.SnackBar(flet.Text(value="Пингуем"))
        
        self.tool_card = flet.Card(
            content=flet.Container(
                content=flet.Text(value="Ping servers"),
                padding=15,
                on_click=self.put_ui)
            )
        
        self.tool_ui = flet.Column(
            controls=[
                flet.Row(controls=[
                    self.one_server_field,
                    self.one_server_result
                ]),
                
                flet.TextButton(text="ping", on_click=self.ping_one_server),
                
                flet.Divider(height=10, color="white"),
                
                self.snack_bar
            ]
        )
        
        
    def ping_one_server(self, e):
        self.snack_bar.content = flet.Text(value=f"Пингуем {self.one_server_field.value}")
        self.snack_bar.open = True
        self.pg.update()
        
        result = ping3.ping(self.one_server_field.value)
        if result:
            self.one_server_result.value = "Сервер доступен."
        else:
            self.one_server_result.value = "Не доступен"
        
        self.pg.update()