import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание экземпляров GameStats и Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Создание корабля.
    ship = Ship(ai_settings, screen)
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")
    # Создание группы для хранения пуль.
    bullets = Group()
    aliens = Group()
    alien = Alien(ai_settings, screen)
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        # Отображение последнего прорисованного экрана.
        screen.fill(ai_settings.bg_color)
        aliens.draw(screen)
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        # Удаление пуль, вышедших за край экрана.
        for bullet in bullets.copy():
            if bullet.rect.bottom == 0:
                bullets.remove(bullet)
        print(len(bullets))
        ship.blitme()
        pygame.display.flip()


run_game()