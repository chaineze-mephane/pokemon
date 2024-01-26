import pygame
pygame.mixer.init()
clic_sound = pygame.mixer.Sound("assets/song/click.wav")

def game(screen):
    clock = pygame.time.Clock()
    running = True

    # Charger l'image de fond
    background = pygame.image.load("assets/img/intro.png")
    background = pygame.transform.scale(background, screen.get_size())

    # Liste de textes à afficher
    textes = [
        "Bienvenue nouveau dresseur!",
        "Je suis le professeur Shen",
        "Je suis chargé de vous guider dans votre aventure",
        "Je vous conseille de consulter la Rubrique Guide",
        "Afin de savoir comment fonctionne le jeu",
        "Dans ce périple vous serez confronté à beaucoup d'adversaires.",
        "Il y a en tout 4 régions différentes.",
        "Dessert , Volcanique , Montagne , Mer",
        "Dans chacune des régions vous trouverez une arène",
        "Lorsque que vous gagnerez tous vos combats",
        "Vous gagnerez un badge",
        "Est-ce que vous réussirez à tous les obtenir ",
        "Je vous souhaite bonne chance",
    ]

    # Indice du texte actuel
    indice_texte = 0

    # Charger l'image de la bordure
    bordure = pygame.image.load("assets/img/bordure.png")
    bordure = pygame.transform.scale(bordure, (screen.get_width() - 40, screen.get_height() - 40))  # Ajustez la taille selon vos besoins
    nouvelle_taille = (1200, 200)  # par exemple, 300 pixels de largeur et 200 pixels de hauteur
    bordure = pygame.transform.scale(bordure, nouvelle_taille)

    # Charger l'image au milieu du fond
    image_au_milieu = pygame.image.load("assets/img/chen.png")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    clic_sound.play()
                    indice_texte += 1
                    if indice_texte >= len(textes):
                        running = False

        # Dessiner le fond
        screen.blit(background, (0, 0))

        # Afficher l'image au milieu du fond
        image_rect = image_au_milieu.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(image_au_milieu, image_rect)

        # Dessiner la bordure au bas au milieu
        bordure_rect = bordure.get_rect(
            center=(screen.get_width() // 2, screen.get_height() - bordure.get_height() // 2 - 20))
        screen.blit(bordure, bordure_rect)

        # Afficher le texte actuel
        font = pygame.font.Font('assets/police/PixelifySans-VariableFont_wght.ttf', 36)
        texte = font.render(textes[indice_texte], True, (0, 0, 0))

        # Calculer la position verticale du texte pour l'aligner avec le bas de la bordure
        texte_rect = texte.get_rect(center=(screen.get_width() // 2, bordure_rect.centery))
        screen.blit(texte, texte_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
