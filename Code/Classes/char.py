import pygame as pg
from .. import prepare_game, control
from .. import constants as c
from . import powerups


class Char(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = prepare_game.GFX['mario_bros']

        self.setup_timers()
        self.setup_state_booleans()
        self.setup_forces()
        self.setup_counters()
        self.load_images_from_sheet()

        self.state = c.WALK
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        self.key_timer = 0

    def setup_timers(self):

        """
        Sets up timers for animations
        """

        self.walking_timer = 0
        self.invincible_animation_timer = 0
        self.invincible_start_timer = 0
        self.fire_transition_timer = 0
        self.death_timer = 0
        self.transition_timer = 0
        self.last_firebullet_time = 0
        self.hurt_invisible_timer = 0
        self.hurt_invisible_timer2 = 0

    def setup_state_booleans(self):

        """
        Sets up booleans that affects the main char logic
        """

        self.facing_right = True
        self.allow_jump = True
        self.dead = False
        self.invincible = False
        self.big = False
        self.fire = False
        self.allow_firebullet = True
        self.in_transition_state = False
        self.hurt_invincible = False
        self.in_castle = False
        self.crouching = False
        self.losing_invincibility = False

    def setup_forces(self):

        """
        Sets up forces that affect the main char velocity
        """

        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_Y_VEL
        self.x_accel = c.WALK_ACCEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY

    def setup_counters(self):

        """
        These keep track of various total for important values
        """

        self.frame_index = 0
        self.invincible_index = 0
        self.fire_transition_index = 0
        self.firebullet_count = 0

    def load_images_from_sheet(self):

        """
        Extracts the main char images from his sprite sheet and assigns
        them to appropriate lists
        """

        self.right_frames = []
        self.left_frames = []

        self.right_small_normal_frames = []
        self.left_small_normal_frames = []
        self.right_small_green_frames = []
        self.left_small_green_frames = []
        self.right_small_red_frames = []
        self.left_small_red_frames = []
        self.right_small_black_frames = []
        self.left_small_black_frames = []

        self.right_big_normal_frames = []
        self.left_big_normal_frames = []
        self.right_big_green_frames = []
        self.left_big_green_frames = []
        self.right_big_red_frames = []
        self.left_big_red_frames = []
        self.right_big_black_frames = []
        self.left_big_black_frames = []

        self.right_fire_frames = []
        self.left_fire_frames = []

        # Images for normal main char

        self.right_small_normal_frames.append(
            self.get_image(178, 32, 12, 16))
        self.right_small_normal_frames.append(
            self.get_image(80,  32, 15, 16))
        self.right_small_normal_frames.append(
            self.get_image(96,  32, 16, 16))
        self.right_small_normal_frames.append(
            self.get_image(112,  32, 16, 16))
        self.right_small_normal_frames.append(
            self.get_image(144, 32, 16, 16))
        self.right_small_normal_frames.append(
            self.get_image(130, 32, 14, 16))
        self.right_small_normal_frames.append(
            self.get_image(160, 32, 15, 16))
        self.right_small_normal_frames.append(
            self.get_image(320, 8, 16, 24))
        self.right_small_normal_frames.append(
            self.get_image(241, 33, 16, 16))
        self.right_small_normal_frames.append(
            self.get_image(194, 32, 12, 16))
        self.right_small_normal_frames.append(
            self.get_image(210, 33, 12, 16))

        # Images for invincible animation

        self.right_small_green_frames.append(
            self.get_image(178, 224, 12, 16))
        self.right_small_green_frames.append(
            self.get_image(80, 224, 15, 16))
        self.right_small_green_frames.append(
            self.get_image(96, 224, 16, 16))
        self.right_small_green_frames.append(
            self.get_image(112, 224, 15, 16))
        self.right_small_green_frames.append(
            self.get_image(144, 224, 16, 16))
        self.right_small_green_frames.append(
            self.get_image(130, 224, 14, 16))

        # Images for fire mode char

        self.right_small_red_frames.append(
            self.get_image(178, 272, 12, 16))
        self.right_small_red_frames.append(
            self.get_image(80, 272, 15, 16))
        self.right_small_red_frames.append(
            self.get_image(96, 272, 16, 16))
        self.right_small_red_frames.append(
            self.get_image(112, 272, 15, 16))
        self.right_small_red_frames.append(
            self.get_image(144, 272, 16, 16))
        self.right_small_red_frames.append(
            self.get_image(130, 272, 14, 16))

        self.right_small_black_frames.append(
            self.get_image(178, 176, 12, 16))
        self.right_small_black_frames.append(
            self.get_image(80, 176, 15, 16))
        self.right_small_black_frames.append(
            self.get_image(96, 176, 16, 16))
        self.right_small_black_frames.append(
            self.get_image(112, 176, 15, 16))
        self.right_small_black_frames.append(
            self.get_image(144, 176, 16, 16))
        self.right_small_black_frames.append(
            self.get_image(130, 176, 14, 16))

        # Images for normal big main char

        self.right_big_normal_frames.append(
            self.get_image(176, 0, 16, 32))
        self.right_big_normal_frames.append(
            self.get_image(81, 0, 16, 32))
        self.right_big_normal_frames.append(
            self.get_image(97, 0, 15, 32))
        self.right_big_normal_frames.append(
            self.get_image(113, 0, 15, 32))
        self.right_big_normal_frames.append(
            self.get_image(144, 0, 16, 32))
        self.right_big_normal_frames.append(
            self.get_image(128, 0, 16, 32))
        self.right_big_normal_frames.append(
            self.get_image(336, 0, 16, 32))
        self.right_big_normal_frames.append(
            self.get_image(160, 10, 16, 22))
        self.right_big_normal_frames.append(
            self.get_image(272, 2, 16, 29))
        self.right_big_normal_frames.append(
            self.get_image(193, 2, 16, 30))
        self.right_big_normal_frames.append(
            self.get_image(209, 2, 16, 29))

        # Images for green big main char

        self.right_big_green_frames.append(
            self.get_image(176, 192, 16, 32))
        self.right_big_green_frames.append(
            self.get_image(81, 192, 16, 32))
        self.right_big_green_frames.append(
            self.get_image(97, 192, 15, 32))
        self.right_big_green_frames.append(
            self.get_image(113, 192, 15, 32))
        self.right_big_green_frames.append(
            self.get_image(144, 192, 16, 32))
        self.right_big_green_frames.append(
            self.get_image(128, 192, 16, 32))
        self.right_big_green_frames.append(
            self.get_image(336, 192, 16, 32))
        self.right_big_green_frames.append(
            self.get_image(160, 202, 16, 22))

        self.right_big_black_frames.append(
            self.get_image(176, 144, 16, 32))
        self.right_big_black_frames.append(
            self.get_image(81, 144, 16, 32))
        self.right_big_black_frames.append(
            self.get_image(97, 144, 15, 32))
        self.right_big_black_frames.append(
            self.get_image(113, 144, 15, 32))
        self.right_big_black_frames.append(
            self.get_image(144, 144, 16, 32))
        self.right_big_black_frames.append(
            self.get_image(128, 144, 16, 32))
        self.right_big_black_frames.append(
            self.get_image(336, 144, 16, 32))
        self.right_big_black_frames.append(
            self.get_image(160, 154, 16, 22))

        # Images for red big main char

        self.right_big_red_frames.append(
            self.get_image(176, 240, 16, 32))
        self.right_big_red_frames.append(
            self.get_image(81, 240, 16, 32))
        self.right_big_red_frames.append(
            self.get_image(97, 240, 15, 32))
        self.right_big_red_frames.append(
            self.get_image(113, 240, 15, 32))
        self.right_big_red_frames.append(
            self.get_image(144, 240, 16, 32))
        self.right_big_red_frames.append(
            self.get_image(128, 240, 16, 32))
        self.right_big_red_frames.append(
            self.get_image(336, 240, 16, 32))
        self.right_big_red_frames.append(
            self.get_image(160, 250, 16, 22))

        # Images for fire mode char

        self.right_fire_frames.append(
            self.get_image(176, 48, 16, 32))
        self.right_fire_frames.append(
            self.get_image(81, 48, 16, 32))
        self.right_fire_frames.append(
            self.get_image(97, 48, 15, 32))
        self.right_fire_frames.append(
            self.get_image(113, 48, 15, 32))
        self.right_fire_frames.append(
            self.get_image(144, 48, 16, 32))
        self.right_fire_frames.append(
            self.get_image(128, 48, 16, 32))
        self.right_fire_frames.append(
            self.get_image(336, 48, 16, 32))
        self.right_fire_frames.append(
            self.get_image(160, 58, 16, 22))
        self.right_fire_frames.append(
            self.get_image(0, 0, 0, 0))
        self.right_fire_frames.append(
            self.get_image(193, 50, 16, 29))
        self.right_fire_frames.append(
            self.get_image(209, 50, 16, 29))

        for frame in self.right_small_normal_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_normal_frames.append(new_image)

        for frame in self.right_small_green_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_green_frames.append(new_image)

        for frame in self.right_small_red_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_red_frames.append(new_image)

        for frame in self.right_small_black_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_black_frames.append(new_image)

        for frame in self.right_big_normal_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_normal_frames.append(new_image)

        for frame in self.right_big_green_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_green_frames.append(new_image)

        for frame in self.right_big_red_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_red_frames.append(new_image)

        for frame in self.right_big_black_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_black_frames.append(new_image)

        for frame in self.right_fire_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_fire_frames.append(new_image)

        self.normal_small_frames = [self.right_small_normal_frames,
                                    self.left_small_normal_frames]

        self.green_small_frames = [self.right_small_green_frames,
                                   self.left_small_green_frames]

        self.red_small_frames = [self.right_small_red_frames,
                                 self.left_small_red_frames]

        self.black_small_frames = [self.right_small_black_frames,
                                   self.left_small_black_frames]

        self.invincible_small_frames_list = [self.normal_small_frames,
                                             self.green_small_frames,
                                             self.red_small_frames]

        self.normal_big_frames = [self.right_big_normal_frames,
                                  self.left_big_normal_frames]

        self.green_big_frames = [self.right_big_green_frames,
                                 self.left_big_green_frames]

        self.red_big_frames = [self.right_big_red_frames,
                               self.left_big_red_frames]

        self.black_big_frames = [self.right_big_black_frames,
                                 self.left_big_black_frames]

        self.fire_frames = [self.right_fire_frames,
                            self.left_fire_frames]

        self.invincible_big_frames_list = [self.normal_big_frames,
                                           self.green_big_frames,
                                           self.red_big_frames]

        self.all_images = [self.right_big_normal_frames,
                           self.right_big_black_frames,
                           self.right_big_red_frames,
                           self.right_big_green_frames,
                           self.right_small_normal_frames,
                           self.right_small_green_frames,
                           self.right_small_red_frames,
                           self.right_small_black_frames,
                           self.left_big_normal_frames,
                           self.left_big_black_frames,
                           self.left_big_red_frames,
                           self.left_big_green_frames,
                           self.left_small_normal_frames,
                           self.left_small_red_frames,
                           self.left_small_green_frames,
                           self.left_small_black_frames]

        self.right_frames = self.normal_small_frames[0]
        self.left_frames = self.normal_small_frames[1]

    def get_image(self, x, y, width, height):

        """
        Extracts the images from the sprite sheet
        """

        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image

    def update(self, keys, game_labels, fire_group):

        """
        Updates main char's states and animations once per frame
        """

        self.current_time = game_labels[c.CURRENT_TIME]
        self.handle_state(keys, fire_group)
        self.check_for_special_state()
        self.animation()

    def handle_state(self, keys, fire_group):

        """
        Determines main char's logic based on his state
        """

        if self.state == c.STAND:
            self.standing(keys, fire_group)
        elif self.state == c.WALK:
            self.walking(keys, fire_group)
        elif self.state == c.JUMP:
            self.jumping(keys, fire_group)
        elif self.state == c.FALL:
            self.falling(keys, fire_group)
        elif self.state == c.DEATH_JUMP:
            self.jumping_to_death()
        elif self.state == c.SMALL_TO_BIG:
            self.changing_to_big()
        elif self.state == c.BIG_TO_FIRE:
            self.changing_to_fire()
        elif self.state == c.BIG_TO_SMALL:
            self.changing_to_small()
        elif self.state == c.WALKING_TO_CASTLE:
            self.walking_to_castle()

    def standing(self, keys, fire_group):

        """
        This function is called if the main char is standing still
        """

        self.check_to_allow_jump(keys)
        self.check_to_allow_firebullet(keys)

        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0

        if keys[control.keybinding['action']]:
            if self.fire and self.allow_firebullet:
                self.shoot_firebullet(fire_group)

        if keys[control.keybinding['down']]:
            self.crouching = True

        if keys[control.keybinding['left']]:
            self.facing_right = False
            self.get_out_of_crouch()
            self.state = c.WALK
        elif keys[control.keybinding['right']]:
            self.facing_right = True
            self.get_out_of_crouch()
            self.state = c.WALK
        elif keys[control.keybinding['jump']]:
            if self.allow_jump:
                if self.big:
                    prepare_game.SFX['big_jump'].play()
                else:
                    prepare_game.SFX['small_jump'].play()
                self.state = c.JUMP
                self.y_vel = c.JUMP_VEL
        else:
            self.state = c.STAND

        if not keys[control.keybinding['down']]:
            self.get_out_of_crouch()

    def get_out_of_crouch(self):

        """
        Get out of crouch state
        """

        bottom = self.rect.bottom
        left = self.rect.x
        if self.facing_right:
            self.image = self.right_frames[0]
        else:
            self.image = self.left_frames[0]
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left
        self.crouching = False

    def check_to_allow_jump(self, keys):

        """
        Check to allow the main char to jump
        """

        if not keys[control.keybinding['jump']]:
            self.allow_jump = True

    def check_to_allow_firebullet(self, keys):

        """
        Check to allow the shooting of a firebullet
        """

        if not keys[control.keybinding['action']]:
            self.allow_firebullet = True

    def shoot_firebullet(self, powerup_group):

        """
        Shoots firebullet, allowing no more than two to exist at once
        """

        prepare_game.SFX['firebullet'].play()
        self.firebullet_count = self.count_number_of_firebullets(powerup_group)

        if (self.current_time - self.last_firebullet_time) > 200:
            if self.firebullet_count < 2:
                self.allow_firebullet = False
                powerup_group.add(
                    powerups.FireBullet(self.rect.right, self.rect.y,
                                        self.facing_right))
                self.last_firebullet_time = self.current_time

                self.frame_index = 6
                if self.facing_right:
                    self.image = self.right_frames[self.frame_index]
                else:
                    self.image = self.left_frames[self.frame_index]

    def count_number_of_firebullets(self, powerup_group):

        """
        Count the number of firebullets that exist in the level
        """

        firebullet_list = []

        for powerup in powerup_group:
            if powerup.name == c.FIREBULLET:
                firebullet_list.append(powerup)

        return len(firebullet_list)

    def walking(self, keys, fire_group):

        """
        This function is called when the main char is in a walking state.
        """

        self.check_to_allow_jump(keys)
        self.check_to_allow_firebullet(keys)

        if self.frame_index == 0:
            self.frame_index += 1
            self.walking_timer = self.current_time
        else:
            if (self.current_time - self.walking_timer >
                    self.calculate_animation_speed()):
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 1

                self.walking_timer = self.current_time

        if keys[control.keybinding['action']]:
            self.max_x_vel = c.MAX_RUN_SPEED
            self.x_accel = c.RUN_ACCEL
            if self.fire and self.allow_firebullet:
                self.shoot_firebullet(fire_group)
        else:
            self.max_x_vel = c.MAX_WALK_SPEED
            self.x_accel = c.WALK_ACCEL

        if keys[control.keybinding['jump']]:
            if self.allow_jump:
                if self.big:
                    prepare_game.SFX['big_jump'].play()
                else:
                    prepare_game.SFX['small_jump'].play()
                self.state = c.JUMP
                if self.x_vel > 4.5 or self.x_vel < -4.5:
                    self.y_vel = c.JUMP_VEL - .5
                else:
                    self.y_vel = c.JUMP_VEL

        if keys[control.keybinding['left']]:
            self.get_out_of_crouch()
            self.facing_right = False
            if self.x_vel > 0:
                self.frame_index = 5
                self.x_accel = c.SMALL_TURNAROUND
            else:
                self.x_accel = c.WALK_ACCEL

            if self.x_vel > (self.max_x_vel * -1):
                self.x_vel -= self.x_accel
                if self.x_vel > -0.5:
                    self.x_vel = -0.5
            elif self.x_vel < (self.max_x_vel * -1):
                self.x_vel += self.x_accel

        elif keys[control.keybinding['right']]:
            self.get_out_of_crouch()
            self.facing_right = True
            if self.x_vel < 0:
                self.frame_index = 5
                self.x_accel = c.SMALL_TURNAROUND
            else:
                self.x_accel = c.WALK_ACCEL

            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel

        else:
            if self.facing_right:
                if self.x_vel > 0:
                    self.x_vel -= self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.STAND
            else:
                if self.x_vel < 0:
                    self.x_vel += self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.STAND

    def calculate_animation_speed(self):

        """
        Used to make the walking animation speed be in a arithmetic relation to
        the main char's x-vel
        """

        if self.x_vel == 0:
            animation_speed = 130
        elif self.x_vel > 0:
            animation_speed = 130 - (self.x_vel * (13))
        else:
            animation_speed = 130 - (self.x_vel * (13) * -1)

        return animation_speed

    def jumping(self, keys, fire_group):

        """
        Called when the main char is in a JUMP state.
        """

        self.allow_jump = False
        self.frame_index = 4
        self.gravity = c.JUMP_GRAVITY
        self.y_vel += self.gravity
        self.check_to_allow_firebullet(keys)

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravity = c.GRAVITY
            self.state = c.FALL

        if keys[control.keybinding['left']]:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys[control.keybinding['right']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if not keys[control.keybinding['jump']]:
            self.gravity = c.GRAVITY
            self.state = c.FALL

        if keys[control.keybinding['action']]:
            if self.fire and self.allow_firebullet:
                self.shoot_firebullet(fire_group)

    def falling(self, keys, fire_group):

        """
        Called when the main char is in a FALL state
        """

        self.check_to_allow_firebullet(keys)
        if self.y_vel < c.MAX_Y_VEL:
            self.y_vel += self.gravity

        if keys[control.keybinding['left']]:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys[control.keybinding['right']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if keys[control.keybinding['action']]:
            if self.fire and self.allow_firebullet:
                self.shoot_firebullet(fire_group)

    def jumping_to_death(self):

        """
        Called when the main char is in a DEATH_JUMP state
        """

        if self.death_timer == 0:
            self.death_timer = self.current_time
        elif (self.current_time - self.death_timer) > 500:
            self.rect.y += self.y_vel
            self.y_vel += self.gravity

    def start_death_jump(self, game_labels):

        """
        Used to put the main char in a DEATH_JUMP state
        """
        self.dead = True
        game_labels[c.CHAR_DEAD] = True
        self.y_vel = -11
        self.gravity = .5
        self.frame_index = 6
        self.image = self.right_frames[self.frame_index]
        self.state = c.DEATH_JUMP
        self.in_transition_state = True

    def changing_to_big(self):

        """
        Changes the main char's image attributes while
        transitioning to big
        """
        self.in_transition_state = True

        if self.transition_timer == 0:
            self.transition_timer = self.current_time
        elif self.timer_between_these_two_times(135, 200):
            self.set_char_to_middle_image()
        elif self.timer_between_these_two_times(200, 365):
            self.set_char_to_small_image()
        elif self.timer_between_these_two_times(365, 430):
            self.set_char_to_middle_image()
        elif self.timer_between_these_two_times(430, 495):
            self.set_char_to_small_image()
        elif self.timer_between_these_two_times(495, 560):
            self.set_char_to_middle_image()
        elif self.timer_between_these_two_times(560, 625):
            self.set_char_to_big_image()
        elif self.timer_between_these_two_times(625, 690):
            self.set_char_to_small_image()
        elif self.timer_between_these_two_times(690, 755):
            self.set_char_to_middle_image()
        elif self.timer_between_these_two_times(755, 820):
            self.set_char_to_big_image()
        elif self.timer_between_these_two_times(820, 885):
            self.set_char_to_small_image()
        elif self.timer_between_these_two_times(885, 950):
            self.set_char_to_big_image()
            self.state = c.WALK
            self.in_transition_state = False
            self.transition_timer = 0
            self.become_big()

    def timer_between_these_two_times(self, start_time, end_time):

        """
        Checks if the timer is at the right time for the action.
        """

        if (self.current_time - self.transition_timer) >= start_time\
           and (self.current_time - self.transition_timer) < end_time:
            return True

    def set_char_to_middle_image(self):

        """
        During a change from small to big, sets the main char's image
        to the transition/middle size
        """

        if self.facing_right:
            self.image = self.normal_small_frames[0][7]
        else:
            self.image = self.normal_small_frames[1][7]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.centerx = centerx

    def set_char_to_small_image(self):

        """
        During a change from small to big, sets the main char's
        image to small.
        """

        if self.facing_right:
            self.image = self.normal_small_frames[0][0]
        else:
            self.image = self.normal_small_frames[1][0]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.centerx = centerx

    def set_char_to_big_image(self):

        """
        During a change from small to big, sets main char's
        image to big.
        """

        if self.facing_right:
            self.image = self.normal_big_frames[0][0]
        else:
            self.image = self.normal_big_frames[1][0]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.centerx = centerx

    def become_big(self):
        self.big = True
        self.right_frames = self.right_big_normal_frames
        self.left_frames = self.left_big_normal_frames
        bottom = self.rect.bottom
        left = self.rect.x
        image = self.right_frames[0]
        self.rect = image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left

    def changing_to_fire(self):

        """
        Called when the main char is in a BIG_TO_FIRE state
        """
        self.in_transition_state = True

        if self.facing_right:
            frames = [self.right_fire_frames[3],
                      self.right_big_green_frames[3],
                      self.right_big_red_frames[3],
                      self.right_big_black_frames[3]]
        else:
            frames = [self.left_fire_frames[3],
                      self.left_big_green_frames[3],
                      self.left_big_red_frames[3],
                      self.left_big_black_frames[3]]

        if self.fire_transition_timer == 0:
            self.fire_transition_timer = self.current_time
        elif (self.current_time - self.fire_transition_timer) > 65 and (self.current_time - self.fire_transition_timer) < 130:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 195:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 260:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 325:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 390:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 455:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 520:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 585:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 650:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 715:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 780:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 845:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 910:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 975:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 1040:
            self.image = frames[2]
            self.fire = True
            self.in_transition_state = False
            self.state = c.WALK
            self.transition_timer = 0

    def changing_to_small(self):

        """
        Main char's state and animation when he shrinks from big to small
        after colliding with an enemy
        """

        self.in_transition_state = True
        self.hurt_invincible = True
        self.state = c.BIG_TO_SMALL

        if self.facing_right:
            frames = [self.right_big_normal_frames[4],
                      self.right_big_normal_frames[8],
                      self.right_small_normal_frames[8]
                      ]
        else:
            frames = [self.left_big_normal_frames[4],
                      self.left_big_normal_frames[8],
                      self.left_small_normal_frames[8]
                      ]

        if self.transition_timer == 0:
            self.transition_timer = self.current_time
        elif (self.current_time - self.transition_timer) < 265:
            self.image = frames[0]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 330:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 395:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 460:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 525:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 590:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 655:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 720:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 785:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 850:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 915:
            self.image = frames[2]
            self.adjust_rect()
            self.in_transition_state = False
            self.state = c.WALK
            self.big = False
            self.transition_timer = 0
            self.hurt_invisible_timer = 0
            self.become_small()

    def adjust_rect(self):

        """
        Makes sure new Rect has the same bottom and left
        location as previous Rect
        """

        x = self.rect.x
        bottom = self.rect.bottom
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = bottom

    def become_small(self):
        self.big = False
        self.right_frames = self.right_small_normal_frames
        self.left_frames = self.left_small_normal_frames
        bottom = self.rect.bottom
        left = self.rect.x
        image = self.right_frames[0]
        self.rect = image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left

    def walking_to_castle(self):

        """
        State when the main char walks to the castle to end the level
        """

        self.max_x_vel = 5
        self.x_accel = c.WALK_ACCEL

        if self.x_vel < self.max_x_vel:
            self.x_vel += self.x_accel

        if (self.walking_timer == 0 or (self.current_time - self.walking_timer) > 200):
            self.walking_timer = self.current_time

        elif (self.current_time - self.walking_timer) > \
                self.calculate_animation_speed():
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 1
            self.walking_timer = self.current_time

    def check_for_special_state(self):

        """
        Determines if the main char is invincible or recently hurt.
        """

        self.check_if_invincible()
        self.check_if_fire()
        self.check_if_hurt_invincible()
        self.check_if_crouching()

    def check_if_invincible(self):
        if self.invincible:
            if ((self.current_time - self.invincible_start_timer) < 10000):
                self.losing_invincibility = False
                self.change_frame_list(30)
            elif ((self.current_time - self.invincible_start_timer) < 12000):
                self.losing_invincibility = True
                self.change_frame_list(100)
            else:
                self.losing_invincibility = False
                self.invincible = False
        else:
            if self.big:
                self.right_frames = self.right_big_normal_frames
                self.left_frames = self.left_big_normal_frames
            else:
                self.right_frames = self.invincible_small_frames_list[0][0]
                self.left_frames = self.invincible_small_frames_list[0][1]

    def change_frame_list(self, frame_switch_speed):
        if (self.current_time - self.invincible_animation_timer) > frame_switch_speed:
            if self.invincible_index < (len(self.invincible_small_frames_list) - 1):
                self.invincible_index += 1
            else:
                self.invincible_index = 0

            if self.big:
                frames = self.invincible_big_frames_list[self.invincible_index]
            else:
                frames = self.invincible_small_frames_list[self.invincible_index]

            self.right_frames = frames[0]
            self.left_frames = frames[1]

            self.invincible_animation_timer = self.current_time

    def check_if_fire(self):
        if self.fire and self.invincible is False:
            self.right_frames = self.fire_frames[0]
            self.left_frames = self.fire_frames[1]

    def check_if_hurt_invincible(self):

        """
        Check if the main char is still temporarily invincible
        after getting hurt.
        """

        if self.hurt_invincible and self.state != c.BIG_TO_SMALL:
            if self.hurt_invisible_timer2 == 0:
                self.hurt_invisible_timer2 = self.current_time
            elif (self.current_time - self.hurt_invisible_timer2) < 2000:
                self.hurt_invincible_check()
            else:
                self.hurt_invincible = False
                self.hurt_invisible_timer = 0
                self.hurt_invisible_timer2 = 0
                for frames in self.all_images:
                    for image in frames:
                        image.set_alpha(255)

    def hurt_invincible_check(self):

        """
        Makes the main char invincible on a fixed interval
        """

        if self.hurt_invisible_timer == 0:
            self.hurt_invisible_timer = self.current_time
        elif (self.current_time - self.hurt_invisible_timer) < 35:
            self.image.set_alpha(0)
        elif (self.current_time - self.hurt_invisible_timer) < 70:
            self.image.set_alpha(255)
            self.hurt_invisible_timer = self.current_time

    def check_if_crouching(self):

        """
        Checks if the main char is crouching
        """

        if self.crouching and self.big:
            bottom = self.rect.bottom
            left = self.rect.x
            if self.facing_right:
                self.image = self.right_frames[7]
            else:
                self.image = self.left_frames[7]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.x = left

    def animation(self):

        """
        Adjusts the main char's image for animation
        """

        if self.state == c.DEATH_JUMP \
            or self.state == c.SMALL_TO_BIG \
            or self.state == c.BIG_TO_FIRE \
            or self.state == c.BIG_TO_SMALL \
                or self.crouching:
            pass
        elif self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]
