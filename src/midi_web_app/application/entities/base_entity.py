import pygame
from typing import Tuple, Sequence

class BaseEntity(pygame.sprite.Sprite):
    """Base entity for building entities hereafter."""
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.size = size
        self.image = pygame.surface.Surface(size)
        self.rect = self.image.get_rect(center=position)

    def update(self, events: Sequence[pygame.event.Event]) -> None:
        """Base update class to be overridden by the child class."""
        pass
