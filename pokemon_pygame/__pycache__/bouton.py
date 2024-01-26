import pygame
from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN

class Bouton:
    def __init__(self, rect, nom, font, couleur_fond):
        self.rect = rect
        self.nom = nom
        self.effet = False
        self.font = font
        self.couleur_fond = couleur_fond

    def afficher(self, screen):
        pygame.draw.rect(screen, self.couleur_fond, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        if self.effet:
            couleur_texte = (255, 0, 0)
        else:
            couleur_texte = (0, 0, 0)

        texte = self.font.render(self.nom, True, couleur_texte)
        text_rect = texte.get_rect(center=self.rect.center)
        screen.blit(texte, text_rect.topleft)

    def check_clic(self, pos):
        return self.rect.collidepoint(pos)

    def check_survol(self, pos):
        self.effet = self.rect.collidepoint(pos)


