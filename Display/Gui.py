import pygame
import pygame_gui
from Display.Bar import Bar

class Gui(pygame_gui.elements.UIWindow):
    def __init__(self, rect,  manager):
        super().__init__(rect, manager=manager)
        self.manager = manager
        self.input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((0, 500), (200, 200)), container=self, parent_element=self, manager=self.manager)
        
    def process_events(self,event,delta):
        super().process_event(event)
        self.input.update(delta)