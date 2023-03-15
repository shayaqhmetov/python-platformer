
class Scene:
    def __init__(self, title):
        self.title = title
        self.counter = 0
        self.background = "black"

    def set_background(self, color):
        self.background = color
    
    def get_background(self):
        return self.background

    def get_title(self):
        return self.title

    def execute(self):
        pass