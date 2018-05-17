import os
import pygame

keybinding = {
                'action': pygame.K_s,
                'jump': pygame.K_a,
                'left': pygame.K_LEFT,
                'right': pygame.K_RIGHT,
                'down': pygame.K_DOWN
            }


class Manage:

    """Clase Manage para gestionar el proyecto. Contiene el loop
       del juego, y contiene el loop de los states. Tambièn contiene
       la lógica para el cambio de states ."""

    def __init__(self, caption):

        self.screen = pygame.display.get_surface()
        self.done = False
        self.clock = pygame.time.Clock()
        self.caption = caption
        self.fps = 60
        self.show_fps = False
        self.current_time = 0.0
        self.keys = pygame.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None

    def setup_state(self, state_dict, start_state):

        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def change_state(self):

        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.previous = previous

    def update(self):

        self.current_time = pygame.time.get_ticks()
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.change_state()
        self.state.update(self.screen, self.keys, self.current_time)

    def event_loop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.keys = pygame.key.get_pressed()
                self.toggle_show_fps(event.key)
            elif event.type == pygame.KEYUP:
                self.keys = pygame.key.get_pressed()
                self.state.get_event(event)

    def toggle_show_fps(self, key):

        if key == pygame.K_F5:
            self.show_fps = not self.show_fps
        if not self.show_fps:
            pygame.display.set_caption(self.caption)

    def main(self):

        """Loop principal para el juego"""

        while not self.done:
            self.event_loop()
            self.update()
            pygame.display.update()
            self.clock.tick(self.fps)
            if self.show_fps:
                fps = self.clock.get_fps()
                with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
                pygame.display.set_caption(with_fps)


class State:

    """Clase State para definir y cargar los states."""

    def __init__(self):

        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}

    def get_event(self, event):
        pass

    def start_up(self, current_time, persistant):

        self.persist = persistant
        self.start_time = current_time

    def cleanup(self):

        self.done = False
        return self.persist

    def update(self, surface, keys, current_time):

        pass

def load_gfx(directory, colorkey=(255, 0, 255), accept=('.png', '.jpg', '.bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics

def load_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi')):
    songs = {}
    for song in os.listdir(directory):
        name,ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs

def load_fonts(directory, accept='.ttf'):
    return load_music(directory, accept)


def load_sfx(directory, accept=('.wav', '.mpe', '.ogg', '.mdi')):
    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pygame.mixer.Sound(os.path.join(directory, fx))
    return effects
