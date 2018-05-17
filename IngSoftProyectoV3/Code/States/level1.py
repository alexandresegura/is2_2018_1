import pygame
from .. import setup, means
from .. import constants
from .. import music_sound
from .. Classes import character
from .. Classes import info
from .. Classes import collider
from .. Classes import bricks


class Level1(means.State):

    def __init__(self):
        means.State.__init__(self)

    def startup(self, current_time, persist):

        """Metodo para crear el state"""

        self.game_info = persist
        self.persist = self.game_info
        self.game_info[constants.CURRENT_TIME] = current_time
        self.game_info[constants.LEVEL_STATE] = constants.NOT_FROZEN
        self.game_info[constants.CHAR_DEAD] = False

        self.state = constants.NOT_FROZEN
        self.death_timer = 0
        self.flag_timer = 0
        self.flag_score = None
        self.flag_score_total = 0

        self.moving_score_list = []
        self.additional_info_display = info.AdditionalInfo(self.game_info, constants.LEVEL)
        self.sound_manager = music_sound.Sound(self.additional_info_display)

        self.setup_background()
        self.setup_ground()
        self.setup_steps()
        self.setup_char()
        self.setup_bricks()
        self.setup_pipes()
        self.setup_spritegroups()


    def setup_background(self):

        """Configura el escenario del juego y lo redimensiona adecuadamente"""

        self.background = setup.GFX['level_1a']
        self.back_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background,
                                  (int(self.back_rect.width*constants.BACKGROUND_MULTIPLER),
                                  int(self.back_rect.height*constants.BACKGROUND_MULTIPLER)))
        self.back_rect = self.background.get_rect()
        width = self.back_rect.width
        height = self.back_rect.height
        self.level = pygame.Surface((width, height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = setup.SCREEN.get_rect(bottom=self.level_rect.bottom)
        self.viewport.x = self.game_info[constants.CAMERA_START_X]

    def setup_ground(self):

        """Metodo utilizado para crear el suelo (objetos que pertenecen a la clase colliders)"""

        ground_rect1 = collider.Collider(0, constants.GROUND_HEIGHT, 2953, 60)
        ground_rect2 = collider.Collider(3048, constants.GROUND_HEIGHT,  635, 60)
        ground_rect3 = collider.Collider(3819, constants.GROUND_HEIGHT, 2735, 60)
        ground_rect4 = collider.Collider(6647, constants.GROUND_HEIGHT, 2300, 60)

        self.ground_group = pygame.sprite.Group(ground_rect1,
                                                ground_rect2,
                                                ground_rect3,
                                                ground_rect4)
    def setup_steps(self):

        """Metodo para crear los Rect (pygame) collisionables para los pasos"""

        step1 = collider.Collider(5745, 495, 40, 44)
        step2 = collider.Collider(5788, 452, 40, 44)
        step3 = collider.Collider(5831, 409, 40, 44)
        step4 = collider.Collider(5874, 366, 40, 176)
        step5 = collider.Collider(6001, 366, 40, 176)
        step6 = collider.Collider(6044, 408, 40, 40)
        step7 = collider.Collider(6087, 452, 40, 40)
        step8 = collider.Collider(6130, 495, 40, 40)
        step9 = collider.Collider(6345, 495, 40, 40)
        step10 = collider.Collider(6388, 452, 40, 40)
        step11 = collider.Collider(6431, 409, 40, 40)
        step12 = collider.Collider(6474, 366, 40, 40)
        step13 = collider.Collider(6517, 366, 40, 176)
        step14 = collider.Collider(6644, 366, 40, 176)
        step15 = collider.Collider(6687, 408, 40, 40)
        step16 = collider.Collider(6728, 452, 40, 40)
        step17 = collider.Collider(6771, 495, 40, 40)
        step18 = collider.Collider(7760, 495, 40, 40)
        step19 = collider.Collider(7803, 452, 40, 40)
        step20 = collider.Collider(7845, 409, 40, 40)
        step21 = collider.Collider(7888, 366, 40, 40)
        step22 = collider.Collider(7931, 323, 40, 40)
        step23 = collider.Collider(7974, 280, 40, 40)
        step24 = collider.Collider(8017, 237, 40, 40)
        step25 = collider.Collider(8060, 194, 40, 40)
        step26 = collider.Collider(8103, 194, 40, 360)
        step27 = collider.Collider(8488, 495, 40, 40)

        self.step_group = pygame.sprite.Group(step1,  step2,
                                          step3,  step4,
                                          step5,  step6,
                                          step7,  step8,
                                          step9,  step10,
                                          step11, step12,
                                          step13, step14,
                                          step15, step16,
                                          step17, step18,
                                          step19, step20,
                                          step21, step22,
                                          step23, step24,
                                          step25, step26,
                                          step27)

    def setup_bricks(self):

        """Crea todos los obstaculos para este nivel."""

        self.brick_pieces_group = pygame.sprite.Group()

        brick1  = bricks.Brick(858,  365)
        brick2  = bricks.Brick(944,  365)
        brick3  = bricks.Brick(1030, 365)
        brick4  = bricks.Brick(3299, 365)
        brick5  = bricks.Brick(3385, 365)
        brick6  = bricks.Brick(3430, 193)
        brick7  = bricks.Brick(3473, 193)
        brick8  = bricks.Brick(3516, 193)
        brick9  = bricks.Brick(3559, 193)
        brick10 = bricks.Brick(3602, 193)
        brick11 = bricks.Brick(3645, 193)
        brick12 = bricks.Brick(3688, 193)
        brick13 = bricks.Brick(3731, 193)
        brick14 = bricks.Brick(3901, 193)
        brick15 = bricks.Brick(3944, 193)
        brick16 = bricks.Brick(3987, 193)
        brick18 = bricks.Brick(4287, 365)
        brick20 = bricks.Brick(5058, 365)
        brick21 = bricks.Brick(5187, 193)
        brick22 = bricks.Brick(5230, 193)
        brick23 = bricks.Brick(5273, 193)
        brick24 = bricks.Brick(5488, 193)
        brick25 = bricks.Brick(5574, 193)
        brick26 = bricks.Brick(5617, 193)
        brick27 = bricks.Brick(5531, 365)
        brick28 = bricks.Brick(5574, 365)
        brick29 = bricks.Brick(7202, 365)
        brick30 = bricks.Brick(7245, 365)
        brick31 = bricks.Brick(7331, 365)

        self.brick_group = pygame.sprite.Group(brick1,  brick2,
                                           brick3,  brick4,
                                           brick5,  brick6,
                                           brick7,  brick8,
                                           brick9,  brick10,
                                           brick11, brick12,
                                           brick13, brick14,
                                           brick15, brick16,
                                           brick18, brick20,
                                           brick21, brick22,
                                           brick23, brick24,
                                           brick25, brick26,
                                           brick27, brick28,
                                           brick29, brick30,
                                           brick31)

    def setup_pipes(self):

        """Metodo para crear Rect (pygame) colisionables para todos los pipes"""

        pipe1 = collider.Collider(1202, 452, 83, 82)
        pipe2 = collider.Collider(1631, 409, 83, 140)
        pipe3 = collider.Collider(1973, 366, 83, 170)
        pipe4 = collider.Collider(2445, 366, 83, 170)
        pipe5 = collider.Collider(6989, 452, 83, 82)
        pipe6 = collider.Collider(7675, 452, 83, 82)

        self.pipe_group = pygame.sprite.Group(pipe1, pipe2,
                                          pipe3, pipe4,
                                          pipe5, pipe6)

    def setup_char(self):

        """Metodo para ubicar al personaje principal al inicio del nivel"""

        self.character = character.Character()
        self.character.rect.x = self.viewport.x + 110
        self.character.rect.bottom = constants.GROUND_HEIGHT

    def setup_spritegroups(self):

        self.sprites_about_to_die_group = pygame.sprite.Group()
        self.ground_step_pipe_group = pygame.sprite.Group(self.ground_group,
                                                      self.pipe_group,
                                                      self.step_group)

    def update(self, surface, keys, current_time):

        """Updates este nivel utilizando los states."""

        self.game_info[constants.CURRENT_TIME] = self.current_time = current_time
        self.handle_states(keys)
        self.check_if_time_out()
        self.blit_everything(surface)
        self.sound_manager.update(self.game_info, self.character)

    def handle_states(self, keys):

        """Si el nivel se encuentra en state estatico, solo se se hace update al personaje principal"""

        if self.state == constants.FROZEN:
            self.update_during_transition_state(keys)
        elif self.state == constants.NOT_FROZEN:
            self.update_all_sprites(keys)
        elif self.state == constants.IN_CASTLE:
            self.update_while_in_castle()
        elif self.state == constants.FLAG_AND_FIREWORKS:
            self.update_flag_and_fireworks()

    def update_during_transition_state(self, keys):

        """Update al personaje principal en el cambio de un state a otro (cuando muere o cuando agarra un powerup). """

        self.character.update(keys, self.game_info, self.fire_group)
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        if self.flag_score:
            self.flag_score.update(None, self.game_info)
        self.check_if_character_in_transition_state()
        self.check_for_character_death()
        self.additional_info_display.update(self.game_info, self.character)

    def check_if_character_in_transition_state(self):

        """Si el personaje principal esta en un state de cambio el juego parasara
           al state estatico"""

        if self.character.in_transition_state:
            self.game_info[constants.LEVEL_STATE] = self.state = constants.FROZEN
        elif self.character.in_transition_state == False:
            if self.state == constants.FROZEN:
                self.game_info[constants.LEVEL_STATE] = self.state = constants.NOT_FROZEN


    def update_all_sprites(self, keys):

        """Update al posicionamiento de los sprites en la pantalla."""

        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        if self.flag_score:
            self.flag_score.update(None, self.game_info)
        self.sprites_about_to_die_group.update(self.game_info, self.viewport)
        self.check_if_character_in_transition_state()
        self.check_for_character_death()
        self.brick_group.update()
        self.brick_pieces_group.update()
        self.update_viewport()
        self.adjust_sprite_positions()
        self.additional_info_display.update(self.game_info, self.character)

    def check_for_character_death(self):

        """Reinicia el nivel si el personaje principal muere"""

        if self.character.rect.y > constants.SCREEN_HEIGHT and not self.character.in_castle:
            self.character.dead = True
            self.character.x_vel = 0
            self.state = constants.FROZEN
            self.game_info[constants.CHAR_DEAD] = True

    def check_if_time_out(self):

        """Revisa si el tiempo llego a 0"""

        if self.additional_info_display.time <= 0 \
                and not self.character.dead \
                and not self.character.in_castle:
            self.state = constants.FROZEN
            self.character.start_death_jump(self.game_info)

    def adjust_sprite_positions(self):

        """Reconfigura la posicion de los sprites de acuerdo a su speed en el eje x e y """

        self.adjust_character_position()

    def adjust_character_position(self):

        """Reconfigura la posicion del personaje principal de acuerdo a su speed en el eje x e y"""

        self.last_x_position = self.character.rect.right
        self.character.rect.x += round(self.character.x_vel)
        self.check_character_x_collisions()

        if self.character.in_transition_state == False:
            self.character.rect.y += round(self.character.y_vel)
            self.check_character_y_collisions()

        if self.character.rect.x < (self.viewport.x + 5):
            self.character.rect.x = (self.viewport.x + 5)

    def check_character_x_collisions(self):

        """Revisa las collisiones del personaje principal en el eje x"""

        collider = pygame.sprite.spritecollideany(self.character, self.ground_step_pipe_group)
        brick = pygame.sprite.spritecollideany(self.character, self.brick_group)

        if brick:
            self.adjust_character_for_x_collisions(brick)

        elif collider:
            self.adjust_character_for_x_collisions(collider)

    def adjust_character_for_x_collisions(self, collider):

        """Reduce la velocidad de mario a 0 cuando choca con algun collider"""

        if self.character.rect.x < collider.rect.x:
            self.character.rect.right = collider.rect.left
        else:
            self.character.rect.left = collider.rect.right

        self.character.x_vel = 0

    def check_character_y_collisions(self):

        """Revisa las collisiones del personaje principal en el eje y"""

        ground_step_or_pipe = pygame.sprite.spritecollideany(self.character, self.ground_step_pipe_group)
        brick = pygame.sprite.spritecollideany(self.character, self.brick_group)

        if brick:
            self.adjust_character_for_y_brick_collisions(brick)

        elif ground_step_or_pipe:
            self.adjust_character_for_y_ground_pipe_collisions(ground_step_or_pipe)

        self.test_if_character_is_falling()

    def adjust_character_for_y_brick_collisions(self, brick):

        """Collision del personaje principal con los obstaculos en el eje y"""

        if self.character.rect.y > brick.rect.y:
            if brick.state == constants.RESTING:
                if self.character.big and brick.contents is None:
                    setup.SFX['brick_smash'].play()
                    brick.kill()
                    self.brick_pieces_group.add(
                        bricks.BrickPiece(brick.rect.x,
                                               brick.rect.y - (brick.rect.height/2),
                                               -2, -12),
                        bricks.BrickPiece(brick.rect.right,
                                               brick.rect.y - (brick.rect.height/2),
                                               2, -12),
                        bricks.BrickPiece(brick.rect.x,
                                               brick.rect.y,
                                               -2, -6),
                        bricks.BrickPiece(brick.rect.right,
                                               brick.rect.y,
                                               2, -6))
                else:
                    setup.SFX['bump'].play()
                    if brick.coin_total > 0:
                        self.game_info[constants.COIN_TOTAL] += 1
                        self.game_info[constants.SCORE] += 200
                    self.check_if_enemy_on_brick(brick)
                    brick.start_bump(self.moving_score_list)
            elif brick.state == constants.OPENED:
                setup.SFX['bump'].play()
            self.character.y_vel = 7
            self.character.rect.y = brick.rect.bottom
            self.character.state = constants.FALL

        else:
            self.character.y_vel = 0
            self.character.rect.bottom = brick.rect.top
            self.character.state = constants.WALK

    def adjust_character_for_y_ground_pipe_collisions(self, collider):

        """Collision del personaje principal con los pipes en el eje y"""

        if collider.rect.bottom > self.character.rect.bottom:
            self.character.y_vel = 0
            self.character.rect.bottom = collider.rect.top
            if self.character.state == constants.END_OF_LEVEL_FALL:
                self.character.state = constants.WALKING_TO_CASTLE
            else:
                self.character.state = constants.WALK
        elif collider.rect.top < self.character.rect.top:
            self.character.y_vel = 7
            self.character.rect.top = collider.rect.bottom
            self.character.state = constants.FALL

    def test_if_character_is_falling(self):

        """Camia al personaje principal al state Caerse si mas de un pixel esta fuera
           de un obstaculo, el piso, etc"""

        self.character.rect.y += 1
        test_collide_group = pygame.sprite.Group(self.ground_step_pipe_group,
                                                 self.brick_group)


        if pygame.sprite.spritecollideany(self.character, test_collide_group) is None:
            if self.character.state != constants.JUMP \
                and self.character.state != constants.DEATH_JUMP \
                and self.character.state != constants.SMALL_TO_BIG \
                and self.character.state != constants.BIG_TO_FIRE \
                and self.character.state != constants.BIG_TO_SMALL \
                and self.character.state != constants.FLAGPOLE \
                and self.character.state != constants.WALKING_TO_CASTLE \
                and self.character.state != constants.END_OF_LEVEL_FALL:
                self.character.state = constants.FALL
            elif self.character.state == constants.WALKING_TO_CASTLE or \
                self.character.state == constants.END_OF_LEVEL_FALL:
                self.character.state = constants.END_OF_LEVEL_FALL

        self.character.rect.y -= 1

    def check_if_falling(self, sprite, sprite_group):

        """Checks if sprite should enter a falling state"""

        sprite.rect.y += 1

        if pygame.sprite.spritecollideany(sprite, sprite_group) is None:
            if sprite.state != constants.JUMP:
                sprite.state = constants.FALL

        sprite.rect.y -= 1

    def set_game_info_values(self):

        """Valores del juego cuando el personaje muere"""

        if self.game_info[constants.SCORE] > self.persist[constants.TOP_SCORE]:
            self.persist[constants.TOP_SCORE] = self.game_info[constants.SCORE]
        if self.character.dead:
            self.persist[constants.LIVES] -= 1

        if self.persist[constants.LIVES] == 0:
            self.next = constants.GAME_OVER
            self.game_info[constants.CAMERA_START_X] = 0
        elif self.character.dead == False:
            self.next = constants.MAIN_MENU
            self.game_info[constants.CAMERA_START_X] = 0
        elif self.additional_info_display.time == 0:
            self.next = constants.TIME_OUT
        else:
            if self.character.rect.x > 3670 \
                    and self.game_info[constants.CAMERA_START_X] == 0:
                self.game_info[constants.CAMERA_START_X] = 3440
            self.next = constants.LOAD_SCREEN


    def blit_everything(self, surface):

        self.level.blit(self.background, self.viewport, self.viewport)
        if self.flag_score:
            self.flag_score.draw(self.level)

        self.sprites_about_to_die_group.draw(self.level)
        self.brick_group.draw(self.level)
        self.brick_pieces_group.draw(self.level)
        #self.check_point_group.draw(self.level)
        surface.blit(self.level, (0,0), self.viewport)
        self.additional_info_display.draw(surface)
        for score in self.moving_score_list:
            score.draw(surface)

    def update_viewport(self):

        """Cambia el posicionamiento de la camara"""

        third = self.viewport.x + self.viewport.w//3
        character_center = self.character.rect.centerx
        character_right = self.character.rect.right

        if self.character.x_vel > 0 and character_center >= third:
            mult = 0.5 if character_right < self.viewport.centerx else 1
            new = self.viewport.x + mult * self.character.x_vel
            highest = self.level_rect.w - self.viewport.w
            self.viewport.x = min(highest, new)

    def end_game(self):

        """Termina el juego"""

        if self.flag_timer == 0:
            self.flag_timer = self.current_time
        elif (self.current_time - self.flag_timer) > 2000:
            self.set_game_info_values()
            self.next = constants.GAME_OVER
            self.sound_manager.stop_music()
            self.done = True
