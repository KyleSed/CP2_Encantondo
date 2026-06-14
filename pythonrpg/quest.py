import pygame
import math
import input
from sprite import Sprite


class QuestManager:
    def __init__(self, font_size=24):

        self.state = 0
        self.game_over = False

        self.current_dialogue = ""
        self.dialogue_timer = 0
        self.font = pygame.font.SysFont("Arial", font_size)
        self.end_font = pygame.font.SysFont("Arial", 64)

        self.npc1 = Sprite("images/npcssprite/npc4.png", 46 * 32, 9 * 32)
        self.npc2 = Sprite("images/npcssprite/npc3.png", 45 * 32, 14 * 32)

    def is_close(self, player, npc):
        dx = player.x - npc.x
        dy = player.y - npc.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance < 20

    def update(self, player):
        if self.dialogue_timer > 0:
            self.dialogue_timer -= 1
        else:
            self.current_dialogue = ""

        if input.is_key_pressed(pygame.K_SPACE):

            # Talking to NPC 1 (Quest Giver)
            if self.is_close(player, self.npc1):
                if self.state == 0:
                    self.current_dialogue = "Mama: Anak! Bili ka nga ng yelo diyan sa tapat!"
                    self.state = 1
                    self.dialogue_timer = 200
                elif self.state == 1:
                    self.current_dialogue = "Mama: Saan na yung yelo?"
                    self.dialogue_timer = 120
                elif self.state == 2:
                    self.current_dialogue = "Mama: Bat antagal mo? Pumirme ka na nga sa bahay at ggagawa nako ng halo-halo!"
                    self.state = 3
                    self.game_over = True
                    self.dialogue_timer = 200

            # Talking to NPC 2 (Item Holder)
            elif self.is_close(player, self.npc2):
                if self.state == 0:
                    self.current_dialogue = "tindero: Beautiful day out here, isn't it?"
                    self.dialogue_timer = 120
                elif self.state == 1:
                    self.current_dialogue = "tindero: Isang yelo? Plain ba or salted?."
                    self.state = 2
                    self.dialogue_timer = 120
                elif self.state == 2:
                    self.current_dialogue = "tindero: Eto sukli!"
                    self.dialogue_timer = 120

    def draw_ui(self, screen):
        # Draw Dialogue Box if there is text
        if self.current_dialogue != "":
            pygame.draw.rect(screen, (0, 0, 0), (50, 650, 1100, 100))
            pygame.draw.rect(screen, (255, 255, 255), (50, 650, 1100, 100), 3)

            text_surface = self.font.render(self.current_dialogue, True, (255, 255, 255))
            screen.blit(text_surface, (70, 685))

        # Draw endgamescreen
        if self.game_over and self.state == 3:
            # Darken screen overlay
            overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            screen.blit(overlay, (0, 0))

            # screen para sa endgmae text
            end_surface = self.end_font.render("THE END - YOU WIN!", True, (255, 215, 0))
            screen.blit(end_surface, (screen.get_width() // 2 - 250, screen.get_height() // 2 - 50))