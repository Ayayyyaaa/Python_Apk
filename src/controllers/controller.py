from src.models.model import Model
from src.views.view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self) 

    def handle_increment(self, e):
        self.model.increment()
        self.view.update_display(self.model.count)

    def get_view(self):
        return self.view