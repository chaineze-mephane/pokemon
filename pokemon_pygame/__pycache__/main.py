import pygame
from pygame.locals import MOUSEBUTTONDOWN, MOUSEMOTION
from bouton import Bouton
from game import game

pygame.init()
screen = pygame.display.set_mode((1300, 780))
pygame.mixer.init()
clic_sound = pygame.mixer.Sound("assets/song/menu.wav")  # Remplacez par le chemin de votre fichier son

clock = pygame.time.Clock()
running = True
current_mode = "menu"
loading = False
loading_timer = 180  # Nombre de boucles à attendre avant de passer au jeu (60 boucles par seconde, donc 3 secondes)
loading_progress = 0  # Pourcentage de chargement (de 0 à 100)

image_menu = pygame.image.load("assets/img/img_menu.png")
image_menu = pygame.transform.scale(image_menu, screen.get_size())

couleur_fond = (255, 255, 255)

boutons = [
    Bouton(pygame.Rect(0, 0, 450, 70), "Nouvelle Partie", pygame.font.Font('assets/police/PixelifySans-VariableFont_wght.ttf', 46), couleur_fond),
    Bouton(pygame.Rect(0, 0, 450, 70), "Accéder Pokédex", pygame.font.Font('assets/police/PixelifySans-VariableFont_wght.ttf', 46), couleur_fond),
    Bouton(pygame.Rect(0, 0, 450, 70), "Rajouter Pokémon", pygame.font.Font('assets/police/PixelifySans-VariableFont_wght.ttf', 46), couleur_fond),
]

for i, bouton in enumerate(boutons):
    bouton.rect.centerx = screen.get_rect().centerx
    bouton.rect.centery = screen.get_rect().centery + 100 + (i - len(boutons) // 2) * 90

def draw_loading_bar(surface, progress):
    bar_width = 400
    bar_height = 20
    bar_rect = pygame.Rect((screen.get_width() - bar_width) // 2, screen.get_height() // 2 - bar_height // 2, bar_width, bar_height)
    pygame.draw.rect(surface, (0, 0, 0), bar_rect, 2)
    fill_rect = pygame.Rect(bar_rect.left + 2, bar_rect.top + 2, int((bar_width - 4) * progress / 100), bar_height - 4)
    pygame.draw.rect(surface, (0, 0, 0), fill_rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            for bouton in boutons:
                if bouton.check_clic(event.pos):
                    print(f"Clic sur {bouton.nom}")
                    clic_sound.play()
                    if bouton.nom == "Nouvelle Partie":
                        current_mode = "loading"
                        loading = True

        elif event.type == MOUSEMOTION:
            for bouton in boutons:
                bouton.check_survol(event.pos)

    # Dessiner le fond normal
    screen.fill(couleur_fond)

    if current_mode == "menu":
        screen.blit(image_menu, (0, 0))
        for bouton in boutons:
            bouton.afficher(screen)

    elif current_mode == "loading":
        # Écran de chargement
        loading_text = "Chargement..."
        font = pygame.font.Font('assets/police/PixelifySans-VariableFont_wght.ttf', 36)
        text = font.render(loading_text, True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
        screen.blit(text, text_rect)

        # Barre de progression
        draw_loading_bar(screen, loading_progress)

        # Simuler le chargement
        loading_timer -= 1
        if loading_timer <= 0:
            current_mode = "jeu"
            loading = False
            loading_timer = 180  # Réinitialiser le compteur de chargement
            loading_progress = 0  # Réinitialiser la barre de progression

        # Mettez à jour la barre de progression
        loading_progress = 100 - (loading_timer / 180) * 100

    elif current_mode == "jeu":
        game(screen)
        current_mode = "menu"

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
