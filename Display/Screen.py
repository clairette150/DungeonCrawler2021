import pygame
import pygame_gui
from Display.Gui import Gui
from Display.Bar import Bar
class DummyController:
    def __init__(self):
        self.player = {}
        self.player["hp"] = 10
        self.player["mp"] = 2

class Screen:
    def __init__(self, controller=DummyController()):
        self.controller = controller
        pygame.init()
        pygame.display.set_caption("DungeonCrawler2021")
        (width, height) = (800,600)
        self.screen = pygame.display.set_mode((width,height))
        self.manager =  pygame_gui.UIManager((800,600))
        self.clock = pygame.time.Clock()
        #self.button = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((0, height), (100, 50)),
           #                                  html_text="blub", manager=self.manager)
        pygame.display.flip()
        self.gui = Gui(pygame.Rect((600,0),(200,200)),self.manager)
        self.running = True
        while self.running:
            self.cycle()
    
    def cycle(self):
        time_delta = self.clock.tick(60)/1000.0
        for event in pygame.event.get():
            self.manager.process_events(event)
            self.gui.process_events(event, time_delta)
        ## HP 
        Bar(self.controller.player["hp"], (255,0,0),680,500, 20,100, self.screen)
        ## MP
        Bar(self.controller.player["mp"], (0,0,255), 700,500, 20,100, self.screen)
        self.manager.update(time_delta)
        self.manager.draw_ui(self.screen)
        pygame.display.update()

