import flet

class Tool:
    def __init__(self, pg_tool_ui, pg):
        self.tool_card = flet.Card()
        self.pg = pg
        self.tool_ui = fleet.Container()
        
        self.pg_tool_ui = pg_tool_ui
        
    def put_ui(self, e):
        self.pg_tool_ui.content = self.tool_ui
        self.pg.update()
        print("selected new tool")
        
    def page_resized(self, new_size):
        self.pg_tool_ui.height = new_size[1] - 60
        self.pg_tool_ui.width = int(new_size[0] * 0.7)
        self.pg.update()