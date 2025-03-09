
import pygame
import sys 
import os 

class SherlockGameModule:

    def __init__(self):
        self.name = "Sherlock"


    def run(self): self.create()
    def create(self):
        pygame.init()
        clock = pygame.time.Clock() # Ikoreshwa mu kugena frame Rate
        ecran = pygame.display.set_mode((800, 400))
        pygame.display.set_caption(self.name)
        bg_image = self.get_files()[0]
        gr_image = self.get_files()[1]
        snail = self.get_files()[2] 
        snail_x = 600

        title = self.load_text()[0]



        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Iyo Umuntu Akanze Kuri Quit Button
                    sys.exit()

            ecran.blit(bg_image, (0,0))
            ecran.blit(gr_image, (0,300))
            ecran.blit(title, (370, 5))
            snail_x -= 10
            if snail_x < - 100: 
                snail_x = 800
            ecran.blit(snail, (snail_x,250))
            pygame.display.update()
            clock.tick(80) # Nuyongera Game Yawe FrameRate Yayo Iri Huta


    def get_files(self) -> list:
        background_image = pygame.image.load(os.path.join(".", "game-utils", "graphics", "Sky.png"))
        ground_image = pygame.image.load(os.path.join(".", "game-utils", "graphics", "ground.png"))
        snail = pygame.image.load(os.path.join(".", "game-utils", "graphics", "snail", "snail1.png"))
        return [background_image, ground_image, snail]

    def load_text(self) -> list:
        game_title = pygame.font.Font(None, 40).render(self.name, None, "Black")
        return [game_title]


if __name__ == "__main__":
    SherlockGameModule().run()
