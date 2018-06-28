import pygame as pg
from .. import constants as c
from .. import prepare_game


class Powerup(pg.sprite.Sprite):

    """
    Base class for all powerup groups
    """

    def __init__(self, x, y):
        super(Powerup, self).__init__()

    def setup_powerup(self, x, y, name, setup_frames):

        """
        This separated setup function allows to pass a different
        setup_frames method depending on what the powerup is
        """

        self.sprite_sheet = prepare_game.GFX['item_objects']
        self.frames = []
        self.frame_index = 0
        setup_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.state = c.REVEAL
        self.y_vel = -1
        self.x_vel = 0
        self.direction = c.RIGHT
        self.box_height = y
        self.gravity = 1
        self.max_y_vel = 8
        self.animate_timer = 0
        self.name = name

    def get_image(self, x, y, width, height):

        """
        Get the images frames from the sprite sheet
        """

        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)

        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image

    def update(self, game_labels, *args):

        """
        Updates powerup logic
        """

        self.current_time = game_labels[c.CURRENT_TIME]
        self.handle_state()

    def handle_state(self):

        """
        Placeholder
        """

        pass

    def revealing(self, *args):

        """
        Action when powerup leaves the coin box or brick
        """

        self.rect.y += self.y_vel

        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.y_vel = 0
            self.state = c.SLIDE

    def sliding(self):

        """
        Action for when powerup slides along the ground
        """

        if self.direction == c.RIGHT:
            self.x_vel = 3
        else:
            self.x_vel = -3

    def falling(self):

        """
        When powerups fall off a ledge
        """

        if self.y_vel < self.max_y_vel:
            self.y_vel += self.gravity


class BigChar(Powerup):

    """
    Powerup that makes the main char bigger
    """

    def __init__(self, x, y, name=c.BIGCHAR):
        super(BigChar, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)

    def setup_frames(self):

        """
        Sets up frame list
        """

        self.frames.append(self.get_image(0, 0, 16, 16))

    def handle_state(self):

        """
        Handles behavior based on state
        """

        if self.state == c.REVEAL:
            self.revealing()
        elif self.state == c.SLIDE:
            self.sliding()
        elif self.state == c.FALL:
            self.falling()


class OneLife(BigChar):

    """
    Gives one more life to the main char
    """

    def __init__(self, x, y, name=c.ONELIFE):
        super(OneLife, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)

    def setup_frames(self):
        self.frames.append(self.get_image(16, 0, 16, 16))


class FireChar(Powerup):

    """
    Powerup that allows the main char to throw fire balls
    """

    def __init__(self, x, y, name=c.FIRECHAR):
        super(FireChar, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)

    def setup_frames(self):

        """
        Sets up frame list
        """

        self.frames.append(
            self.get_image(0, 32, 16, 16))
        self.frames.append(
            self.get_image(16, 32, 16, 16))
        self.frames.append(
            self.get_image(32, 32, 16, 16))
        self.frames.append(
            self.get_image(48, 32, 16, 16))

    def handle_state(self):

        """
        Handles logic based on state
        """

        if self.state == c.REVEAL:
            self.revealing()
        elif self.state == c.RESTING:
            self.resting()

    def revealing(self):

        """
        Animation of powerup coming out of box
        """

        self.rect.y += self.y_vel

        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.state = c.RESTING
        self.animation()

    def resting(self):

        """
        Powerup staying still on opened box
        """

        self.animation()

    def animation(self):

        """
        Method to make the Powerup blink
        """

        if (self.current_time - self.animate_timer) > 30:
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 0

            self.image = self.frames[self.frame_index]
            self.animate_timer = self.current_time


class InvChar(Powerup):

    """
    A powerup that gives the main char invincibility
    """

    def __init__(self, x, y, name=c.INVCHAR):
        super(InvChar, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)
        self.animate_timer = 0
        self.rect.y += 1
        self.gravity = .4

    def setup_frames(self):

        """
        Creating the self.frames list where the images for the animation
        will be stored
        """

        self.frames.append(self.get_image(1, 48, 15, 16))
        self.frames.append(self.get_image(17, 48, 15, 16))
        self.frames.append(self.get_image(33, 48, 15, 16))
        self.frames.append(self.get_image(49, 48, 15, 16))

    def handle_state(self):

        """
        Handles logic based on state
        """

        if self.state == c.REVEAL:
            self.revealing()
        elif self.state == c.BOUNCE:
            self.bouncing()

    def revealing(self):

        """
        When the Powerup comes out of the box
        """

        self.rect.y += self.y_vel

        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.start_bounce(-2)
            self.state = c.BOUNCE

        self.animation()

    def animation(self):

        """
        Sets image for animation
        """

        if (self.current_time - self.animate_timer) > 30:
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 0
            self.animate_timer = self.current_time
            self.image = self.frames[self.frame_index]

    def start_bounce(self, vel):

        """
        Transitions into bouncing state
        """

        self.y_vel = vel

    def bouncing(self):

        """
        Action when the powerup is bouncing around
        """

        self.animation()
        if self.direction == c.LEFT:
            self.x_vel = -5
        else:
            self.x_vel = 5


class FireBullet(pg.sprite.Sprite):

    """
    Shots from fire char mode
    """

    def __init__(self, x, y, facing_right, name=c.FIREBULLET):
        super(FireBullet, self).__init__()
        self.sprite_sheet = prepare_game.GFX['item_objects']
        self.setup_frames()
        if facing_right:
            self.direction = c.RIGHT
            self.x_vel = 12
        else:
            self.direction = c.LEFT
            self.x_vel = -12
        self.y_vel = 10
        self.gravity = .9
        self.frame_index = 0
        self.animation_timer = 0
        self.state = c.FLYING
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.y = y
        self.name = name

    def setup_frames(self):

        """
        Sets up animation frames
        """

        self.frames = []
        self.frames.append(
            self.get_image(96, 144, 8, 8))  # Frame 1 of flying
        self.frames.append(
            self.get_image(104, 144, 8, 8))  # Frame 2 of Flying
        self.frames.append(
            self.get_image(96, 152, 8, 8))   # Frame 3 of Flying
        self.frames.append(
            self.get_image(104, 152, 8, 8))  # Frame 4 of flying
        self.frames.append(
            self.get_image(112, 144, 16, 16))  # frame 1 of exploding
        self.frames.append(
            self.get_image(112, 160, 16, 16))  # frame 2 of exploding
        self.frames.append(
            self.get_image(112, 176, 16, 16))  # frame 3 of exploding

    def get_image(self, x, y, width, height):

        """
        Get the images frames from the sprite sheet
        """

        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)

        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image

    def update(self, game_labels, viewport):

        """
        Updates firebullet behavior
        """

        self.current_time = game_labels[c.CURRENT_TIME]
        self.handle_state()
        self.check_if_off_screen(viewport)

    def handle_state(self):

        """
        Handles logic based on state
        """

        if self.state == c.FLYING:
            self.animation()
        elif self.state == c.BOUNCING:
            self.animation()
        elif self.state == c.EXPLODING:
            self.animation()

    def animation(self):

        """
        Adjusts frames for animation
        """

        if self.state == c.FLYING or self.state == c.BOUNCING:
            if (self.current_time - self.animation_timer) > 200:
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 0
                self.animation_timer = self.current_time
                self.image = self.frames[self.frame_index]

        elif self.state == c.EXPLODING:
            if (self.current_time - self.animation_timer) > 50:
                if self.frame_index < 6:
                    self.frame_index += 1
                    self.image = self.frames[self.frame_index]
                    self.animation_timer = self.current_time
                else:
                    self.kill()

    def explode_transition(self):

        """
        Transitions firebullet to EXPLODING state
        """

        self.frame_index = 4
        centerx = self.rect.centerx
        self.image = self.frames[self.frame_index]
        self.rect.centerx = centerx
        self.state = c.EXPLODING

    def check_if_off_screen(self, viewport):

        """
        Removes from sprite group if off screen
        """

        if (self.rect.x > viewport.right) or (self.rect.y > viewport.bottom) \
           or (self.rect.right < viewport.x):
            self.kill()
