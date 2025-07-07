#!/usr/bin/python
# -*- coding: utf-8 -*-
from Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_direction = 1  # 1 baixo, -1 cima
        self.vertical_speed = 2  # velocidade vertical

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        # Movimento vertical oscilante
        self.rect.centery += self.vertical_direction * self.vertical_speed

        # Inverte a direção ao atingir os limites da tela
        if self.rect.top <= 0 or self.rect.bottom >= WIN_HEIGHT:
            self.vertical_direction *= -1

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))