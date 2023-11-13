import flet
import base64
import pyperclip
from .tool import Tool

class Base64Converter(Tool):
    def __init__(self, pg_tool_ui, pg):
        
        self.pg_tool_ui = pg_tool_ui
        self.pg = pg
        self.string_field = flet.TextField(hint_text="Текст", multiline=True, label="Текст")
        self.base64_field = flet.TextField(hint_text="Base64 текст", multiline=True, label="Base64 текст")
        
        self.tool_ui = flet.Column(
                controls=[
                    self.string_field,
                    flet.Row(controls=[
                                      flet.TextButton(text="Конвертировать", on_click=self.text_to_base64),
                                      flet.TextButton(text="Из буфера в поле", on_click=self.buff_to_field64),
                                      flet.TextButton(text="Из буфера в буфер", on_click=self.buff_to_buff64)
                                  ],
                             wrap=True),
                    
                    flet.Divider(height=10, color="white"),
                    
                    self.base64_field,
                    flet.Row(controls=[
                                      flet.TextButton(text="Конвертировать", on_click=self.base64_to_text),
                                      flet.TextButton(text="Из буфера в поле", on_click=self.buff64_to_field),
                                      flet.TextButton(text="Из буфера в буфер", on_click=self.buff64_to_buff)
                                  ],
                             wrap=True)
                ],
                scroll=flet.ScrollMode.ALWAYS,
                height=self.pg.height - 60,
                alignment=flet.MainAxisAlignment.CENTER
            )
        
        self.tool_card = flet.Card(
            content=flet.Container(
                content=flet.Text(value="Base64Converter"),
                padding=15,
                on_click=self.put_ui)
            )

    def text_to_base64(self, e):
        if self.string_field.value == "":
            return
        self.base64_field.value = base64.b64encode(self.string_field.value.encode()).decode()
        self.string_field.value = ""
        self.pg.update()
        
    def buff_to_field64(self, e):
        self.base64_field.value = base64.b64encode(pyperclip.paste().encode()).decode()
        self.pg.update()
        
    def buff_to_buff64(self, e):
        pyperclip.copy(base64.b64encode(pyperclip.paste().encode()).decode())
        
    def base64_to_text(self, e):
        if self.base64_field.value == "":
            return
        self.string_field.value = base64.b64decode(self.base64_field.value.encode()).decode()
        self.base64_field.value = ""
        self.pg.update()
        
    def buff64_to_field(self, e):
        self.string_field.value = base64.b64decode(pyperclip.paste().encode()).decode()
        self.pg.update()
        
    def buff64_to_buff(self, e):
        pyperclip.copy(base64.b64decode(pyperclip.paste().encode()).decode())
    
    def debug(self, e: flet.ContainerTapEvent):
        self.pg.update()
        print("click on base64converter")
        