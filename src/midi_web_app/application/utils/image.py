import os
from typing import Optional, Tuple

import pygame


def load(filename: os.PathLike, file_extension: Optional[str] = ".jpg") -> None:
    image = pygame.image.load(filename + file_extension)
    return image


def scale(
    image: pygame.surface.Surface, size: Tuple[int, int]
) -> pygame.surface.Surface:
    return pygame.transform.scale(image, size)
