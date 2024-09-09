import pygame
from scenes.game_scene import GameScene
from settings import Settings


class Application:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.scenes = {"game": GameScene()}
        self.scene = self.scenes["game"]

    def run(self) -> None:
        running = True
        while running:
            self.screen.fill("black")
            running = self.scene.tick(pygame.event.get())
            self.scene.render(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


def main() -> None:
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
