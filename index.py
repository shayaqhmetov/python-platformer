import pygame

from main.scene import Scene
from scenes.main_scene import MainScene

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([1000,1000])
        self.clock = pygame.time.Clock()
        self.running = True
        self.scenes: Scene = []
        self.current_scene = None
        pass

    def exit(self):
        self.running = False

    def add_scenes(self, scene) -> None:
        self.scenes.append(scene)
    
    def set_background(self, color):
        self.screen.fill(color=color)

    def start(self) -> None:
        while self.running:
            # Required to exit game when pressign X
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()

            if self.current_scene == None:
                self.current_scene = self.scenes[0]
                pygame.display.set_caption(self.current_scene.get_title())
                
            # TODO: Understand how we can move scene logic to scene code itself
            # font = pygame.font.Font(None, 32)
            # text = font.render("Hello World", False, "white")
            # text_rect = text.get_rect()
            # self.screen.blit(text, text_rect)
            pygame.display.update()
            
        pygame.quit()
    
if __name__ == "__main__":
    game = Game()
    
    mainScene = MainScene("Main Scene")
    mainScene.set_background("red")

    game.add_scenes(mainScene)
    game.start()
