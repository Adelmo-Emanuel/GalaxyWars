import pygame
# COLOR
COLOR_LIME = (204, 255, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'JupterBg0': 0,
    'JupterBg1': 1,
    'JupterBg2': 2,
    'JupterBg3': 3,
    'SaturnoBg0': 0,
    'SaturnoBg1': 1,
    'SaturnoBg2': 2,
    'Player1': 7,
    'Player1Shot': 6,
    'Player2': 7,
    'Player2Shot': 6,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 5,
}

ENTITY_HEALTH = {
    'JupterBg0': 999,
    'JupterBg1': 999,
    'JupterBg2': 999,
    'JupterBg3': 999,
    'SaturnoBg0': 999,
    'SaturnoBg1': 999,
    'SaturnoBg2': 999,
    'Player1': 100,
    'Player1Shot': 1,
    'Player2': 100,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_DAMAGE = {
    'JupterBg0': 0,
    'JupterBg1': 0,
    'JupterBg2': 0,
    'JupterBg3': 0,
    'SaturnoBg0': 0,
    'SaturnoBg1': 0,
    'SaturnoBg2': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 10,
    'Enemy2': 1,
    'Enemy2Shot': 12,
}

ENTITY_SCORE = {
    'JupterBg0': 0,
    'JupterBg1': 0,
    'JupterBg2': 0,
    'JupterBg3': 0,
    'SaturnoBg0': 0,
    'SaturnoBg1': 0,
    'SaturnoBg2': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 6,
    'Player2': 6,
    'Enemy1': 25,
    'Enemy2': 25,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100  # 100milis
TIMEOUT_LEVEL = 30000 # 30segs
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }