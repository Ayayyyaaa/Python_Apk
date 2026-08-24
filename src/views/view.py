import flet as ft

class HoverImageButton(ft.Container):
    def __init__(self, default_src: str, hover_src: str, on_click, width: int = 69, height: int = 60):
        super().__init__()
        self.default_src = default_src
        self.hover_src = hover_src
        
        self.image_control = ft.Image(
            src=self.default_src,
            width=width,
            height=height,
            fit="contain"
        )

        self.content = self.image_control
        self.on_click = on_click
        self.ink = True
        self.on_hover = self._handle_hover

    def _handle_hover(self, e):
        if e.data:
            self.image_control.src = self.hover_src
        else:
            self.image_control.src = self.default_src

        self.image_control.update() 


class View(ft.Column):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        self.text_display = ft.Text(value="0", size=40)

        self.btn = HoverImageButton(
            default_src="btn1.png",
            hover_src="btn2.png",
            on_click=self.controller.handle_increment
        )

        self.controls = [self.text_display, self.btn]

    def update_display(self, new_value):
        self.text_display.value = str(new_value)
        self.update()