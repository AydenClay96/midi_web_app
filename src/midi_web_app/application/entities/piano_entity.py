import pygame
from entities.base_entity import BaseEntity

class PianoEntity(BaseEntity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.draw_keyboard()

    def draw_keyboard(self) -> None:
        pattern = [1,0,1,1,0,1,1]
        pattern_idx = 0
        n_white_keys = 52
        key_width = self.size[0]/n_white_keys
        key_height = self.size[1]
    
        self.white_rects = []
        self.black_rects = []
        for i in range(n_white_keys):
            rect = pygame.draw.rect(
                self.image,
                "white",
                [
                    i * key_width,
                    0,
                    key_width,
                    key_height,
                ],
                0,
                2,
            )
            self.white_rects.append(rect)
        for i in range(n_white_keys - 1):
            pygame.draw.rect(
                self.image,
                "black",
                [
                    i * key_width,
                    0,
                    key_width,
                    key_height,
                ],
                1,
                2,
            )
            if pattern[pattern_idx] == 1:
                rect = pygame.draw.rect(
                    self.image,
                    "black",
                    [
                        (i + 2/3) * key_width,
                        0,
                        key_width * (2/3),
                        key_height * 0.55,
                    ],
                    0,
                    2,
                )
                self.black_rects.append(rect)
            pattern_idx += 1
            if pattern_idx >= len(pattern):
                pattern_idx = 0
