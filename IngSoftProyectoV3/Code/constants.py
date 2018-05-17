SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Super Lima World"

# Atributos del personaje principal, luego podran ser modificados en el configurador

WALK_ACC = 0.15
RUN_ACC = 20
TURNAROUND = 0.35
GRAVITY = 1.01
JUMP_GRAVITY = 0.31
JUMP_SPEED = -10
FAST_JUMP_SPEED = -12.5
MAX_Y_SPEED = 11
MAX_RUN_SPEED = 800
MAX_WALK_SPEED = 6

#States del personaje principal

STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
DEATH_JUMP = 'death jump'
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'
WALKING_TO_CASTLE = 'walking to castle'
END_OF_LEVEL_FALL = 'end of level fall'
FIREBALL = 'fireball'
CHAR_DEAD = 'char dead'

#States de Musica y sonido

NORMAL = 'normal'
STAGE_CLEAR = 'stage clear'
WORLD_CLEAR = 'world clear'
TIME_WARNING = 'time warning'
SPED_UP_NORMAL = 'sped up normal'
CHAR_INVINCIBLE = 'char invincible'

# Información de los states y states del juego

MAIN_MENU = 'main menu'
LOAD_SCREEN = 'loading screen'
LEVEL = 'level'
LEVEL1 = 'level1'
LEVEL2 = 'level2'
LEVEL3 = 'level3'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
FAST_COUNT_DOWN = 'fast count down'
END_OF_LEVEL = 'end of level'

#Variables para la info del juego

COIN_TOTAL = 'coin total'
SCORE = 'score'
TOP_SCORE = 'top score'
LIVES = 'lives'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
CAMERA_START_X = 'camera start x'
GAME_DEAD = 'game dead'

#States de los niveles

FROZEN = 'frozen'
NOT_FROZEN = 'not frozen'
IN_CASTLE = 'in castle'
FLAG_AND_FIREWORKS = 'flag and fireworks'

#States del Dinero

OPENED = 'opened'
SPIN = 'spin'

#States de la bandera

TOP_OF_POLE = 'top of pole'
SLIDE_DOWN = 'slide down'
BOTTOM_OF_POLE = 'bottom of pole'

#States de los powerups

REVEAL = 'reveal'
SLIDE = 'slide'
BOUNCE = 'bounce'
FLYING = 'flying'
BOUNCING = 'bouncing'
EXPLODING = 'exploding'

#States de los obstaculos

RESTING = 'resting'
BUMPED = 'bumped'

#Contenido de los obstaculos

MUSHROOM = 'mushroom'
STAR = 'star'
FIREFLOWER = 'fireflower'
SIXCOINS = '6coins'
COIN = 'coin'
LIFE_MUSHROOM = '1up_mushroom'

#States del menu principal

PLAYER1 = '1 player'
CONTROLS = 'Controls'

#Colores

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)

BGCOLOR = WHITE

SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62
