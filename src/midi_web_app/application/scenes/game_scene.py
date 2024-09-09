import os
from typing import Sequence

import pygame
from settings import Settings

from utils import image
from entities.piano_entity import PianoEntity


class GameScene:
    def __init__(self) -> None:
        self.settings = Settings()
        self.background = image.load(
            os.path.join(self.settings.asset_location, "game_background"), ".jpg"
        )
        self.screen_size = self.settings.screen_size
        self.entities = pygame.sprite.Group()
        piano = PianoEntity((self.screen_size[0]/2, self.screen_size[1]*0.8), (self.screen_size[0], self.screen_size[1]*0.2))
        self.entities.add(piano)

    def tick(self, events: Sequence[pygame.event.Event]) -> bool:
        running = True
        for e in events:
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
        self.entities.update(events)
        return running

    def render(self, screen: pygame.surface.Surface) -> pygame.surface.Surface:
        if self.background.get_size() != screen.get_size():
            self.background = image.scale(self.background, screen.get_size())
        screen.blit(self.background)
        self.entities.draw(screen)
        return screen
