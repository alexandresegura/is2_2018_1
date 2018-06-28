import pygame as pg
from .. import constants as c
from .. import control, music_sound
from .. import prepare_game
from .. Classes import labels, collider
from .. Classes import bricks, coin_box
from .. Classes import char, checkpoint
from .. Classes import enemies, score


class Level1(control._State):

    """
    State where you can actually play the game.
    """

    def __init__(self):

        """
        Initializes the state
        """

        control._State.__init__(self)

    def startup(self, current_time, persist):

        """
        Called when the State object is created
        """

        self.game_labels = persist
        self.persist = self.game_labels
        self.game_labels[c.CURRENT_TIME] = current_time
        self.game_labels[c.LEVEL_STATE] = c.NOT_FROZEN
        self.game_labels[c.CHAR_DEAD] = False
        self.state = c.NOT_FROZEN
        self.death_timer = 0
        self.moving_score_list = []
        self.overhead_labels_display = labels.OverheadLabels(self.game_labels,
                                                             c.LEVEL)
        self.sound_manager = music_sound.Sound(self.overhead_labels_display)

        self.setup_background()
        self.setup_ground()
        self.setup_pipes()
        self.setup_steps()
        self.setup_bricks()
        self.setup_coin_boxes()
        self.setup_enemies()
        self.setup_char()
        self.setup_checkpoints()
        self.setup_spritegroups()

    def setup_background(self):

        """
        Sets the background image, rect and scales it to the correct
        proportions
        """

        self.background = prepare_game.GFX['level_1']
        self.back_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                             (int(self.back_rect.width *
                                                  c.BACKGROUND_MULTIPLER),
                                              int(self.back_rect.height *
                                                  c.BACKGROUND_MULTIPLER)))
        self.back_rect = self.background.get_rect()
        width = self.back_rect.width
        height = self.back_rect.height

        self.level = pg.Surface((width, height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = prepare_game.SCREEN.get_rect(bottom=self.level_rect.bottom)
        self.viewport.x = self.game_labels[c.CAMERA_START_X]

    def setup_ground(self):

        """
        Creates collidable, invisible rectangles over top of the ground for
        the character to walk on
        """

        ground_rect1 = collider.Collider(0, c.GROUND_HEIGHT,    2953, 60)
        ground_rect2 = collider.Collider(3048, c.GROUND_HEIGHT,  635, 60)
        ground_rect3 = collider.Collider(3819, c.GROUND_HEIGHT, 2735, 60)
        ground_rect4 = collider.Collider(6647, c.GROUND_HEIGHT, 2300, 60)

        self.ground_group = pg.sprite.Group(ground_rect1,
                                            ground_rect2,
                                            ground_rect3,
                                            ground_rect4)

    def setup_pipes(self):

        """
        Create collidable rects for all the pipes
        """

        pipe1 = collider.Collider(1202, 452, 83, 82)
        pipe2 = collider.Collider(1631, 409, 83, 140)
        pipe3 = collider.Collider(1973, 366, 83, 170)
        pipe4 = collider.Collider(2445, 366, 83, 170)
        pipe5 = collider.Collider(6989, 452, 83, 82)
        pipe6 = collider.Collider(7675, 452, 83, 82)

        self.pipe_group = pg.sprite.Group(pipe1, pipe2,
                                          pipe3, pipe4,
                                          pipe5, pipe6)

    def setup_steps(self):

        """
        Create collideable rects for all the steps
        """

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

        self.step_group = pg.sprite.Group(step1,  step2,
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

        """
        Creates all the breakable bricks for the level.  Coin and
        powerup groups are created so they can be passed to bricks.
        """

        self.coin_group = pg.sprite.Group()
        self.powerup_group = pg.sprite.Group()
        self.brick_pieces_group = pg.sprite.Group()

        brick1 = bricks.Brick(858, 365)
        brick2 = bricks.Brick(944, 365)
        brick3 = bricks.Brick(1030, 365)
        brick4 = bricks.Brick(3299, 365)
        brick5 = bricks.Brick(3385, 365)
        brick6 = bricks.Brick(3430, 193)
        brick7 = bricks.Brick(3473, 193)
        brick8 = bricks.Brick(3516, 193)
        brick9 = bricks.Brick(3559, 193)
        brick10 = bricks.Brick(3602, 193)
        brick11 = bricks.Brick(3645, 193)
        brick12 = bricks.Brick(3688, 193)
        brick13 = bricks.Brick(3731, 193)
        brick14 = bricks.Brick(3901, 193)
        brick15 = bricks.Brick(3944, 193)
        brick16 = bricks.Brick(3987, 193)
        brick17 = bricks.Brick(4030, 365, c.SIXCOINS, self.coin_group)
        brick18 = bricks.Brick(4287, 365)
        brick19 = bricks.Brick(4330, 365, c.INVCHAR, self.powerup_group)
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

        self.brick_group = pg.sprite.Group(brick1, brick2,
                                           brick3, brick4,
                                           brick5, brick6,
                                           brick7, brick8,
                                           brick9, brick10,
                                           brick11, brick12,
                                           brick13, brick14,
                                           brick15, brick16,
                                           brick17, brick18,
                                           brick19, brick20,
                                           brick21, brick22,
                                           brick23, brick24,
                                           brick25, brick26,
                                           brick27, brick28,
                                           brick29, brick30,
                                           brick31)

    def setup_coin_boxes(self):

        """
        Creates all the coin boxes and puts them in a sprite group
        """

        coin_box1 = coin_box.Coin_box(685, 365, c.COIN, self.coin_group)
        coin_box2 = coin_box.Coin_box(901, 365, c.BIGCHAR, self.powerup_group)
        coin_box3 = coin_box.Coin_box(987, 365, c.COIN, self.coin_group)
        coin_box4 = coin_box.Coin_box(943, 193, c.COIN, self.coin_group)
        coin_box5 = coin_box.Coin_box(3342, 365, c.BIGCHAR, self.powerup_group)
        coin_box6 = coin_box.Coin_box(4030, 193, c.COIN, self.coin_group)
        coin_box7 = coin_box.Coin_box(4544, 365, c.COIN, self.coin_group)
        coin_box8 = coin_box.Coin_box(4672, 365, c.COIN, self.coin_group)
        coin_box9 = coin_box.Coin_box(4672, 193, c.BIGCHAR, self.powerup_group)
        coin_box10 = coin_box.Coin_box(4800, 365, c.COIN, self.coin_group)
        coin_box11 = coin_box.Coin_box(5531, 193, c.COIN, self.coin_group)
        coin_box12 = coin_box.Coin_box(7288, 365, c.COIN, self.coin_group)

        self.coin_box_group = pg.sprite.Group(coin_box1,  coin_box2,
                                              coin_box3,  coin_box4,
                                              coin_box5,  coin_box6,
                                              coin_box7,  coin_box8,
                                              coin_box9,  coin_box10,
                                              coin_box11, coin_box12)

    def setup_enemies(self):

        """
        Creates all the enemies and stores them in a list of lists.
        """

        enemya0 = enemies.EnemyA()
        enemya1 = enemies.EnemyA()
        enemya2 = enemies.EnemyA()
        enemya3 = enemies.EnemyA()
        enemya4 = enemies.EnemyA(193)
        enemya5 = enemies.EnemyA(193)
        enemya6 = enemies.EnemyA()
        enemya7 = enemies.EnemyA()
        enemya8 = enemies.EnemyA()
        enemya9 = enemies.EnemyA()
        enemya10 = enemies.EnemyA()
        enemya11 = enemies.EnemyA()
        enemya12 = enemies.EnemyA()
        enemya13 = enemies.EnemyA()
        enemya14 = enemies.EnemyA()
        enemya15 = enemies.EnemyA()

        enemyb0 = enemies.EnemyB()

        enemy_group1 = pg.sprite.Group(enemya0)
        enemy_group2 = pg.sprite.Group(enemya1)
        enemy_group3 = pg.sprite.Group(enemya2, enemya3)
        enemy_group4 = pg.sprite.Group(enemya4, enemya5)
        enemy_group5 = pg.sprite.Group(enemya6, enemya7)
        enemy_group6 = pg.sprite.Group(enemyb0)
        enemy_group7 = pg.sprite.Group(enemya8, enemya9)
        enemy_group8 = pg.sprite.Group(enemya10, enemya11)
        enemy_group9 = pg.sprite.Group(enemya12, enemya13)
        enemy_group10 = pg.sprite.Group(enemya14, enemya15)

        self.enemy_group_list = [enemy_group1,
                                 enemy_group2,
                                 enemy_group3,
                                 enemy_group4,
                                 enemy_group5,
                                 enemy_group6,
                                 enemy_group7,
                                 enemy_group8,
                                 enemy_group9,
                                 enemy_group10]

    def setup_char(self):

        """Places the main char at the beginning of the level"""

        self.char = char.Char()
        self.char.rect.x = self.viewport.x + 110
        self.char.rect.bottom = c.GROUND_HEIGHT

    def setup_checkpoints(self):

        """
        Creates invisible checkpoints that when collided will trigger
        the creation of enemies from the self.enemy_group_list
        """

        check1 = checkpoint.Checkpoint(510, "1")
        check2 = checkpoint.Checkpoint(1400, '2')
        check3 = checkpoint.Checkpoint(1740, '3')
        check4 = checkpoint.Checkpoint(3080, '4')
        check5 = checkpoint.Checkpoint(3750, '5')
        check6 = checkpoint.Checkpoint(4150, '6')
        check7 = checkpoint.Checkpoint(4470, '7')
        check8 = checkpoint.Checkpoint(4950, '8')
        check9 = checkpoint.Checkpoint(5100, '9')
        check10 = checkpoint.Checkpoint(6800, '10')
        check12 = checkpoint.Checkpoint(8775, '12')
        check13 = checkpoint.Checkpoint(2740, 'secret_bigchar', 360, 40, 12)

        self.check_point_group = pg.sprite.Group(check1, check2, check3,
                                                 check4, check5, check6,
                                                 check7, check8, check9,
                                                 check10, check12, check13)

    def setup_spritegroups(self):

        self.sprites_about_to_die_group = pg.sprite.Group()
        self.shell_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()

        self.ground_step_pipe_group = pg.sprite.Group(self.ground_group,
                                                      self.pipe_group,
                                                      self.step_group)

        self.char_and_enemy_group = pg.sprite.Group(self.char,
                                                    self.enemy_group)

    def update(self, surface, keys, current_time):

        """
        Updates Entire level using states
        Called by the control object.
        """

        self.game_labels[c.CURRENT_TIME] = self.current_time = current_time
        self.handle_states(keys)
        self.check_if_time_out()
        self.blit_everything(surface)
        self.sound_manager.update(self.game_labels, self.char)

    def handle_states(self, keys):

        """
        If the level is in a FROZEN state,
        only the main char will update
        """

        if self.state == c.FROZEN:
            self.update_during_transition_state(keys)
        elif self.state == c.NOT_FROZEN:
            self.update_all_sprites(keys)
        elif self.state == c.IN_CASTLE:
            self.update_while_in_castle()
        elif self.state == c.FLAG_AND_FIREWORKS:
            self.update_fireworks()

    def update_during_transition_state(self, keys):

        """
        Updates the main char in a transition state.
        Checks if he leaves the transition state or dies to
        change the level state back
        """

        self.char.update(keys, self.game_labels, self.powerup_group)
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_labels)
        self.coin_box_group.update(self.game_labels)
        self.check_if_char_in_transition_state()
        self.check_for_char_death()
        self.overhead_labels_display.update(self.game_labels, self.char)

    def check_if_char_in_transition_state(self):

        """
        If the main char is in a transition state, the level will be
        in a FROZEN state.
        """

        if self.char.in_transition_state:
            self.game_labels[c.LEVEL_STATE] = self.state = c.FROZEN
        elif self.char.in_transition_state is False:
            if self.state == c.FROZEN:
                self.game_labels[c.LEVEL_STATE] = self.state = c.NOT_FROZEN

    def update_all_sprites(self, keys):

        """
        Updates the location of all sprites on the screen.
        """

        self.char.update(keys, self.game_labels, self.powerup_group)
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_labels)
        self.check_points_check()
        self.enemy_group.update(self.game_labels)
        self.sprites_about_to_die_group.update(self.game_labels, self.viewport)
        self.shell_group.update(self.game_labels)
        self.brick_group.update()
        self.coin_box_group.update(self.game_labels)
        self.powerup_group.update(self.game_labels, self.viewport)
        self.coin_group.update(self.game_labels, self.viewport)
        self.brick_pieces_group.update()
        self.adjust_sprite_positions()
        self.check_if_char_in_transition_state()
        self.check_for_char_death()
        self.update_viewport()
        self.overhead_labels_display.update(self.game_labels, self.char)

    def check_points_check(self):

        """
        Detect if checkpoint collision occurs, delete checkpoint,
        add enemies to self.enemy_group
        """

        checkpoint = pg.sprite.spritecollideany(self.char,
                                                self.check_point_group)
        if checkpoint:
            checkpoint.kill()
            for i in range(1, 11):
                if checkpoint.name == str(i):
                    for index, enemy in enumerate(self.enemy_group_list[i - 1]):
                        enemy.rect.x = self.viewport.right + (index * 60)
                    self.enemy_group.add(self.enemy_group_list[i-1])

            if checkpoint.name == '12':
                self.state = c.IN_CASTLE
                self.char.kill()
                self.char.state == c.STAND
                self.char.in_castle = True
                self.overhead_labels_display.state = c.FAST_COUNT_DOWN

            elif checkpoint.name == 'secret_bigchar' and self.char.y_vel < 0:
                bigchar_box = coin_box.Coin_box(checkpoint.rect.x,
                                                checkpoint.rect.bottom - 40,
                                                'onelife',
                                                self.powerup_group)
                bigchar_box.start_bump(self.moving_score_list)
                self.coin_box_group.add(bigchar_box)

                self.char.y_vel = 7
                self.char.rect.y = bigchar_box.rect.bottom
                self.char.state = c.FALL

            self.char_and_enemy_group.add(self.enemy_group)

    def adjust_sprite_positions(self):

        """
        Adjusts sprites by their x and y velocities and collisions
        """

        self.adjust_char_position()
        self.adjust_enemy_position()
        self.adjust_shell_position()
        self.adjust_powerup_position()

    def adjust_char_position(self):

        """
        Adjusts the main char's position based on his x, y velocities and
        potential collisions
        """

        self.last_x_position = self.char.rect.right
        self.char.rect.x += round(self.char.x_vel)
        self.check_char_x_collisions()

        if self.char.in_transition_state is False:
            self.char.rect.y += round(self.char.y_vel)
            self.check_char_y_collisions()

        if self.char.rect.x < (self.viewport.x + 5):
            self.char.rect.x = (self.viewport.x + 5)

    def check_char_x_collisions(self):

        """
        Check for collisions after the main char is moved on the x axis
        """

        collider = pg.sprite.spritecollideany(self.char, self.ground_step_pipe_group)
        coin_box = pg.sprite.spritecollideany(self.char, self.coin_box_group)
        brick = pg.sprite.spritecollideany(self.char, self.brick_group)
        enemy = pg.sprite.spritecollideany(self.char, self.enemy_group)
        shell = pg.sprite.spritecollideany(self.char, self.shell_group)
        powerup = pg.sprite.spritecollideany(self.char, self.powerup_group)

        if coin_box:
            self.adjust_char_for_x_collisions(coin_box)

        elif brick:
            self.adjust_char_for_x_collisions(brick)

        elif collider:
            self.adjust_char_for_x_collisions(collider)

        elif enemy:
            if self.char.invincible:
                prepare_game.SFX['kick'].play()
                self.game_labels[c.SCORE] += 100
                self.moving_score_list.append(
                    score.Score(self.char.rect.right - self.viewport.x,
                                self.char.rect.y, 100))
                enemy.kill()
                enemy.start_death_jump(c.RIGHT)
                self.sprites_about_to_die_group.add(enemy)
            elif self.char.big:
                prepare_game.SFX['pipe'].play()
                self.char.fire = False
                self.char.y_vel = -1
                self.char.state = c.BIG_TO_SMALL
                self.convert_firechar_to_bigchar()
            elif self.char.hurt_invincible:
                pass
            else:
                self.char.start_death_jump(self.game_labels)
                self.state = c.FROZEN

        elif shell:
            self.adjust_char_for_x_shell_collisions(shell)

        elif powerup:
            if powerup.name == c.INVCHAR:
                self.game_labels[c.SCORE] += 1000
                self.moving_score_list.append(
                    score.Score(self.char.rect.centerx - self.viewport.x,
                                self.char.rect.y, 1000))
                self.char.invincible = True
                self.char.invincible_start_timer = self.current_time
            elif powerup.name == c.BIGCHAR:
                prepare_game.SFX['powerup'].play()
                self.game_labels[c.SCORE] += 1000
                self.moving_score_list.append(
                    score.Score(self.char.rect.centerx - self.viewport.x,
                                self.char.rect.y - 20, 1000))

                self.char.y_vel = -1
                self.char.state = c.SMALL_TO_BIG
                self.char.in_transition_state = True
                self.convert_bigchar_to_firechar()
            elif powerup.name == c.ONELIFE:
                self.moving_score_list.append(
                    score.Score(powerup.rect.right - self.viewport.x,
                                powerup.rect.y,
                                c.ONEUP))

                self.game_labels[c.LIVES] += 1
                prepare_game.SFX['one_up'].play()
            elif powerup.name == c.FIRECHAR:
                prepare_game.SFX['powerup'].play()
                self.game_labels[c.SCORE] += 1000
                self.moving_score_list.append(
                    score.Score(self.char.rect.centerx - self.viewport.x,
                                self.char.rect.y, 1000))

                if self.char.big and self.char.fire is False:
                    self.char.state = c.BIG_TO_FIRE
                    self.char.in_transition_state = True
                elif self.char.big is False:
                    self.char.state = c.SMALL_TO_BIG
                    self.char.in_transition_state = True
                    self.convert_bigchar_to_firechar()

            if powerup.name != c.FIREBULLET:
                powerup.kill()

    def convert_bigchar_to_firechar(self):

        """
        When the main char becomees big, converts all firechar powerups to
        bigchar powerups
        """

        for brick in self.brick_group:
            if brick.contents == c.BIGCHAR:
                brick.contents = c.FIRECHAR
        for coin_box in self.coin_box_group:
            if coin_box.contents == c.BIGCHAR:
                coin_box.contents = c.FIRECHAR

    def convert_firechar_to_bigchar(self):

        """
        When the main char becomes small, converts all bigchar powerups to
        firechar powerups
        """

        for brick in self.brick_group:
            if brick.contents == c.FIRECHAR:
                brick.contents = c.BIGCHAR
        for coin_box in self.coin_box_group:
            if coin_box.contents == c.FIRECHAR:
                coin_box.contents = c.BIGCHAR

    def adjust_char_for_x_collisions(self, collider):

        """
        Puts the main char flush next to the collider
        after moving on the x axis
        """

        if self.char.rect.x < collider.rect.x:
            self.char.rect.right = collider.rect.left
        else:
            self.char.rect.left = collider.rect.right

        self.char.x_vel = 0

    def adjust_char_for_x_shell_collisions(self, shell):

        """
        Logic for the main char if he hits a shell
        moving on the x axis
        """

        if shell.state == c.JUMPED_ON:
            if self.char.rect.x < shell.rect.x:
                self.game_labels[c.SCORE] += 400
                self.moving_score_list.append(
                    score.Score(shell.rect.centerx - self.viewport.x,
                                shell.rect.y,
                                400))
                self.char.rect.right = shell.rect.left
                shell.direction = c.RIGHT
                shell.x_vel = 5
                shell.rect.x += 5
            else:
                self.char.rect.left = shell.rect.right
                shell.direction = c.LEFT
                shell.x_vel = -5
                shell.rect.x += -5

            shell.state = c.SHELL_SLIDE

        elif shell.state == c.SHELL_SLIDE:
            if self.char.big and not self.char.invincible:
                self.char.state = c.BIG_TO_SMALL
            elif self.char.invincible:
                self.game_labels[c.SCORE] += 200
                self.moving_score_list.append(
                    score.Score(shell.rect.right - self.viewport.x,
                                shell.rect.y, 200))
                shell.kill()
                self.sprites_about_to_die_group.add(shell)
                shell.start_death_jump(c.RIGHT)
            else:
                if not self.char.hurt_invincible and not self.char.invincible:
                    self.state = c.FROZEN
                    self.char.start_death_jump(self.game_labels)

    def check_char_y_collisions(self):

        """Checks for collisions when the main char
        moves along the y-axis"""

        ground_step_or_pipe = pg.sprite.spritecollideany(self.char, self.ground_step_pipe_group)
        enemy = pg.sprite.spritecollideany(self.char, self.enemy_group)
        shell = pg.sprite.spritecollideany(self.char, self.shell_group)
        brick = pg.sprite.spritecollideany(self.char, self.brick_group)
        coin_box = pg.sprite.spritecollideany(self.char, self.coin_box_group)
        powerup = pg.sprite.spritecollideany(self.char, self.powerup_group)

        brick, coin_box = self.prevent_collision_conflict(brick, coin_box)

        if coin_box:
            self.adjust_char_for_y_coin_box_collisions(coin_box)

        elif brick:
            self.adjust_char_for_y_brick_collisions(brick)

        elif ground_step_or_pipe:
            self.adjust_char_for_y_ground_pipe_collisions(ground_step_or_pipe)

        elif enemy:
            if self.char.invincible:
                prepare_game.SFX['kick'].play()
                enemy.kill()
                self.sprites_about_to_die_group.add(enemy)
                enemy.start_death_jump(c.RIGHT)
            else:
                self.adjust_char_for_y_enemy_collisions(enemy)

        elif shell:
            self.adjust_char_for_y_shell_collisions(shell)

        elif powerup:
            if powerup.name == c.INVCHAR:
                prepare_game.SFX['powerup'].play()
                powerup.kill()
                self.char.invincible = True
                self.char.invincible_start_timer = self.current_time

        self.test_if_char_is_falling()

    def prevent_collision_conflict(self, obstacle1, obstacle2):

        """
        Allows collisions only for the item closest
        to the main char's center x
        """

        if obstacle1 and obstacle2:
            obstacle1_distance = self.char.rect.centerx - obstacle1.rect.centerx
            if obstacle1_distance < 0:
                obstacle1_distance *= -1
            obstacle2_distance = self.char.rect.centerx - obstacle2.rect.centerx
            if obstacle2_distance < 0:
                obstacle2_distance *= -1

            if obstacle1_distance < obstacle2_distance:
                obstacle2 = False
            else:
                obstacle1 = False

        return obstacle1, obstacle2

    def adjust_char_for_y_coin_box_collisions(self, coin_box):

        """
        Main char collisions with coin boxes on the y-axis
        """

        if self.char.rect.y > coin_box.rect.y:
            if coin_box.state == c.RESTING:
                if coin_box.contents == c.COIN:
                    self.game_labels[c.SCORE] += 200
                    coin_box.start_bump(self.moving_score_list)
                    if coin_box.contents == c.COIN:
                        self.game_labels[c.COIN_TOTAL] += 1
                else:
                    coin_box.start_bump(self.moving_score_list)

            elif coin_box.state == c.OPENED:
                pass
            prepare_game.SFX['bump'].play()
            self.char.y_vel = 7
            self.char.rect.y = coin_box.rect.bottom
            self.char.state = c.FALL
        else:
            self.char.y_vel = 0
            self.char.rect.bottom = coin_box.rect.top
            self.char.state = c.WALK

    def adjust_char_for_y_brick_collisions(self, brick):

        """
        Main char collisions with bricks on the y-axis
        """

        if self.char.rect.y > brick.rect.y:
            if brick.state == c.RESTING:
                if self.char.big and brick.contents is None:
                    prepare_game.SFX['brick_smash'].play()
                    self.check_if_enemy_on_brick(brick)
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
                    prepare_game.SFX['bump'].play()
                    if brick.coin_total > 0:
                        self.game_labels[c.COIN_TOTAL] += 1
                        self.game_labels[c.SCORE] += 200
                    self.check_if_enemy_on_brick(brick)
                    brick.start_bump(self.moving_score_list)
            elif brick.state == c.OPENED:
                prepare_game.SFX['bump'].play()
            self.char.y_vel = 7
            self.char.rect.y = brick.rect.bottom
            self.char.state = c.FALL

        else:
            self.char.y_vel = 0
            self.char.rect.bottom = brick.rect.top
            self.char.state = c.WALK

    def check_if_enemy_on_brick(self, brick):

        """
        Kills enemy if on a bumped or broken brick
        """

        brick.rect.y -= 5

        enemy = pg.sprite.spritecollideany(brick, self.enemy_group)

        if enemy:
            prepare_game.SFX['kick'].play()
            self.game_labels[c.SCORE] += 100
            self.moving_score_list.append(
                score.Score(enemy.rect.centerx - self.viewport.x,
                            enemy.rect.y,
                            100))
            enemy.kill()
            self.sprites_about_to_die_group.add(enemy)
            if self.char.rect.centerx > brick.rect.centerx:
                enemy.start_death_jump('right')
            else:
                enemy.start_death_jump('left')

        brick.rect.y += 5

    def adjust_char_for_y_ground_pipe_collisions(self, collider):

        """
        Main char collisions with pipes on the y-axis
        """

        if collider.rect.bottom > self.char.rect.bottom:
            self.char.y_vel = 0
            self.char.rect.bottom = collider.rect.top
            if self.char.state == c.END_OF_LEVEL_FALL:
                self.char.state = c.WALKING_TO_CASTLE
            else:
                self.char.state = c.WALK
        elif collider.rect.top < self.char.rect.top:
            self.char.y_vel = 7
            self.char.rect.top = collider.rect.bottom
            self.char.state = c.FALL

    def test_if_char_is_falling(self):

        """
        Changes the main char to a FALL state if more than a pixel
        above a pipe, ground, step or box.
        """

        self.char.rect.y += 1
        test_collide_group = pg.sprite.Group(self.ground_step_pipe_group,
                                             self.brick_group,
                                             self.coin_box_group)

        if pg.sprite.spritecollideany(self.char, test_collide_group) is None:
            if self.char.state != c.JUMP \
                and self.char.state != c.DEATH_JUMP \
                and self.char.state != c.SMALL_TO_BIG \
                and self.char.state != c.BIG_TO_FIRE \
                and self.char.state != c.BIG_TO_SMALL \
                and self.char.state != c.WALKING_TO_CASTLE \
                    and self.char.state != c.END_OF_LEVEL_FALL:
                self.char.state = c.FALL
            elif self.char.state == c.WALKING_TO_CASTLE or \
                 self.char.state == c.END_OF_LEVEL_FALL:
                 self.char.state = c.END_OF_LEVEL_FALL

        self.char.rect.y -= 1

    def adjust_char_for_y_enemy_collisions(self, enemy):

        """
        Main char collisions with all enemies on the y-axis
        """

        if self.char.y_vel > 0:
            prepare_game.SFX['stomp'].play()
            self.game_labels[c.SCORE] += 100
            self.moving_score_list.append(
                score.Score(enemy.rect.centerx - self.viewport.x,
                            enemy.rect.y, 100))
            enemy.state = c.JUMPED_ON
            enemy.kill()
            if enemy.name == c.ENEMYA:
                enemy.death_timer = self.current_time
                self.sprites_about_to_die_group.add(enemy)
            elif enemy.name == c.ENEMYB:
                self.shell_group.add(enemy)

            self.char.rect.bottom = enemy.rect.top
            self.char.state = c.JUMP
            self.char.y_vel = -7

    def adjust_char_for_y_shell_collisions(self, shell):

        """
        Main char collisions with enemyb in their shells on the y axis
        """

        if self.char.y_vel > 0:
            self.game_labels[c.SCORE] += 400
            self.moving_score_list.append(
                score.Score(self.char.rect.centerx - self.viewport.x,
                            self.char.rect.y, 400))
            if shell.state == c.JUMPED_ON:
                prepare_game.SFX['kick'].play()
                shell.state = c.SHELL_SLIDE
                if self.char.rect.centerx < shell.rect.centerx:
                    shell.direction = c.RIGHT
                    shell.rect.left = self.char.rect.right + 5
                else:
                    shell.direction = c.LEFT
                    shell.rect.right = self.char.rect.left - 5
            else:
                shell.state = c.JUMPED_ON

    def adjust_enemy_position(self):

        """
        Moves all enemies along the x, y axes and check for collisions
        """

        for enemy in self.enemy_group:
            enemy.rect.x += enemy.x_vel
            self.check_enemy_x_collisions(enemy)

            enemy.rect.y += enemy.y_vel
            self.check_enemy_y_collisions(enemy)
            self.delete_if_off_screen(enemy)

    def check_enemy_x_collisions(self, enemy):

        """
        Enemy collisions along the x axis.  Removes enemy from enemy group
        in order to check against all other enemies then adds it back.
        """

        enemy.kill()
        collider = pg.sprite.spritecollideany(enemy, self.ground_step_pipe_group)
        enemy_collider = pg.sprite.spritecollideany(enemy, self.enemy_group)
        if collider:
            if enemy.direction == c.RIGHT:
                enemy.rect.right = collider.rect.left
                enemy.direction = c.LEFT
                enemy.x_vel = -2
            elif enemy.direction == c.LEFT:
                enemy.rect.left = collider.rect.right
                enemy.direction = c.RIGHT
                enemy.x_vel = 2
        elif enemy_collider:
            if enemy.direction == c.RIGHT:
                enemy.rect.right = enemy_collider.rect.left
                enemy.direction = c.LEFT
                enemy_collider.direction = c.RIGHT
                enemy.x_vel = -2
                enemy_collider.x_vel = 2
            elif enemy.direction == c.LEFT:
                enemy.rect.left = enemy_collider.rect.right
                enemy.direction = c.RIGHT
                enemy_collider.direction = c.LEFT
                enemy.x_vel = 2
                enemy_collider.x_vel = -2

        self.enemy_group.add(enemy)
        self.char_and_enemy_group.add(self.enemy_group)

    def check_enemy_y_collisions(self, enemy):

        """
        Enemy collisions on the y axis
        """

        collider = pg.sprite.spritecollideany(enemy, self.ground_step_pipe_group)
        brick = pg.sprite.spritecollideany(enemy, self.brick_group)
        coin_box = pg.sprite.spritecollideany(enemy, self.coin_box_group)

        if collider:
            if enemy.rect.bottom > collider.rect.bottom:
                enemy.y_vel = 7
                enemy.rect.top = collider.rect.bottom
                enemy.state = c.FALL
            elif enemy.rect.bottom < collider.rect.bottom:
                enemy.y_vel = 0
                enemy.rect.bottom = collider.rect.top
                enemy.state = c.WALK
        elif brick:
            if brick.state == c.BUMPED:
                enemy.kill()
                self.sprites_about_to_die_group.add(enemy)
                if self.char.rect.centerx > brick.rect.centerx:
                    enemy.start_death_jump('right')
                else:
                    enemy.start_death_jump('left')
            elif enemy.rect.x > brick.rect.x:
                enemy.y_vel = 7
                enemy.rect.top = brick.rect.bottom
                enemy.state = c.FALL
            else:
                enemy.y_vel = 0
                enemy.rect.bottom = brick.rect.top
                enemy.state = c.WALK
        elif coin_box:
            if coin_box.state == c.BUMPED:
                self.game_labels[c.SCORE] += 100
                self.moving_score_list.append(
                    score.Score(enemy.rect.centerx - self.viewport.x,
                                enemy.rect.y, 100))
                enemy.kill()
                self.sprites_about_to_die_group.add(enemy)
                if self.char.rect.centerx > coin_box.rect.centerx:
                    enemy.start_death_jump('right')
                else:
                    enemy.start_death_jump('left')

            elif enemy.rect.x > coin_box.rect.x:
                enemy.y_vel = 7
                enemy.rect.top = coin_box.rect.bottom
                enemy.state = c.FALL
            else:
                enemy.y_vel = 0
                enemy.rect.bottom = coin_box.rect.top
                enemy.state = c.WALK
        else:
            enemy.rect.y += 1
            test_group = pg.sprite.Group(self.ground_step_pipe_group,
                                         self.coin_box_group,
                                         self.brick_group)
            if pg.sprite.spritecollideany(enemy, test_group) is None:
                if enemy.state != c.JUMP:
                    enemy.state = c.FALL
            enemy.rect.y -= 1

    def adjust_shell_position(self):

        """
        Moves any enemyb in a shell along the x, y axes and checks for
        collisions
        """

        for shell in self.shell_group:
            shell.rect.x += shell.x_vel
            self.check_shell_x_collisions(shell)
            shell.rect.y += shell.y_vel
            self.check_shell_y_collisions(shell)
            self.delete_if_off_screen(shell)

    def check_shell_x_collisions(self, shell):

        """
        Shell collisions along the x axis
        """

        collider = pg.sprite.spritecollideany(shell, self.ground_step_pipe_group)
        enemy = pg.sprite.spritecollideany(shell, self.enemy_group)

        if collider:
            prepare_game.SFX['bump'].play()
            if shell.x_vel > 0:
                shell.direction = c.LEFT
                shell.rect.right = collider.rect.left
            else:
                shell.direction = c.RIGHT
                shell.rect.left = collider.rect.right
        if enemy:
            prepare_game.SFX['kick'].play()
            self.game_labels[c.SCORE] += 100
            self.moving_score_list.append(
                score.Score(enemy.rect.right - self.viewport.x,
                            enemy.rect.y, 100))
            enemy.kill()
            self.sprites_about_to_die_group.add(enemy)
            enemy.start_death_jump(shell.direction)

    def check_shell_y_collisions(self, shell):

        """
        Shell collisions along the y axis
        """

        collider = pg.sprite.spritecollideany(shell, self.ground_step_pipe_group)
        if collider:
            shell.y_vel = 0
            shell.rect.bottom = collider.rect.top
            shell.state = c.SHELL_SLIDE
        else:
            shell.rect.y += 1
            if pg.sprite.spritecollideany(shell, self.ground_step_pipe_group) is None:
                shell.state = c.FALL
            shell.rect.y -= 1

    def adjust_powerup_position(self):

        """
        Moves bigchar, invchar and firechar along the x, y axes
        """

        for powerup in self.powerup_group:
            if powerup.name == c.BIGCHAR:
                self.adjust_bigchar_position(powerup)
            elif powerup.name == c.INVCHAR:
                self.adjust_invchar_position(powerup)
            elif powerup.name == c.FIREBULLET:
                self.adjust_firebullet_position(powerup)
            elif powerup.name == 'onelife':
                self.adjust_bigchar_position(powerup)

    def adjust_bigchar_position(self, bigchar):

        """
        Moves bigchar powerup along the x, y axes.
        """

        if bigchar.state != c.REVEAL:
            bigchar.rect.x += bigchar.x_vel
            self.check_bigchar_x_collisions(bigchar)

            bigchar.rect.y += bigchar.y_vel
            self.check_bigchar_y_collisions(bigchar)
            self.delete_if_off_screen(bigchar)

    def check_bigchar_x_collisions(self, bigchar):

        """
        Bigchar powerup collisions along the x axis
        """

        collider = pg.sprite.spritecollideany(bigchar, self.ground_step_pipe_group)
        brick = pg.sprite.spritecollideany(bigchar, self.brick_group)
        coin_box = pg.sprite.spritecollideany(bigchar, self.coin_box_group)

        if collider:
            self.adjust_bigchar_for_collision_x(bigchar, collider)
        elif brick:
            self.adjust_bigchar_for_collision_x(bigchar, brick)
        elif coin_box:
            self.adjust_bigchar_for_collision_x(bigchar, coin_box)

    def check_bigchar_y_collisions(self, bigchar):

        """
        Bigchar powerup collisions along the y axis
        """

        collider = pg.sprite.spritecollideany(bigchar, self.ground_step_pipe_group)
        brick = pg.sprite.spritecollideany(bigchar, self.brick_group)
        coin_box = pg.sprite.spritecollideany(bigchar, self.coin_box_group)

        if collider:
            self.adjust_bigchar_for_collision_y(bigchar, collider)
        elif brick:
            self.adjust_bigchar_for_collision_y(bigchar, brick)
        elif coin_box:
            self.adjust_bigchar_for_collision_y(bigchar, coin_box)
        else:
            self.check_if_falling(bigchar, self.ground_step_pipe_group)
            self.check_if_falling(bigchar, self.brick_group)
            self.check_if_falling(bigchar, self.coin_box_group)

    def adjust_bigchar_for_collision_x(self, item, collider):
        """
        Changes bigchar powerup direction if collision along x axis
        """

        if item.rect.x < collider.rect.x:
            item.rect.right = collider.rect.x
            item.direction = c.LEFT
        else:
            item.rect.x = collider.rect.right
            item.direction = c.RIGHT

    def adjust_bigchar_for_collision_y(self, item, collider):

        """
        Changes bigchar powerup state to SLIDE after hitting ground from fall
        """

        item.rect.bottom = collider.rect.y
        item.state = c.SLIDE
        item.y_vel = 0

    def adjust_invchar_position(self, invchar):

        """
        Moves invchar powerup along x, y axes and checks for collisions
        """

        if invchar.state == c.BOUNCE:
            invchar.rect.x += invchar.x_vel
            self.check_bigchar_x_collisions(invchar)
            invchar.rect.y += invchar.y_vel
            self.check_invchar_y_collisions(invchar)
            invchar.y_vel += invchar.gravity
            self.delete_if_off_screen(invchar)

    def check_invchar_y_collisions(self, invchar):

        """
        Invchar powerup collisions along y axis.
        """

        collider = pg.sprite.spritecollideany(invchar, self.ground_step_pipe_group)
        brick = pg.sprite.spritecollideany(invchar, self.brick_group)
        coin_box = pg.sprite.spritecollideany(invchar, self.coin_box_group)

        if collider:
            self.adjust_invchar_for_collision_y(invchar, collider)
        elif brick:
            self.adjust_invchar_for_collision_y(invchar, brick)
        elif coin_box:
            self.adjust_invchar_for_collision_y(invchar, coin_box)

    def adjust_invchar_for_collision_y(self, invchar, collider):

        """
        Allows for a invchar powerup bounce off the ground
        and on the bottom of a box.
        """

        if invchar.rect.y > collider.rect.y:
            invchar.rect.y = collider.rect.bottom
            invchar.y_vel = 0
        else:
            invchar.rect.bottom = collider.rect.top
            invchar.start_bounce(-8)

    def adjust_firebullet_position(self, firebullet):

        """
        Moves the firebullet along the x, y axes
        and checks for collisions
        """

        if firebullet.state == c.FLYING:
            firebullet.rect.x += firebullet.x_vel
            self.check_firebullet_x_collisions(firebullet)
            firebullet.rect.y += firebullet.y_vel
            self.check_firebullet_y_collisions(firebullet)
        elif firebullet.state == c.BOUNCING:
            firebullet.rect.x += firebullet.x_vel
            self.check_firebullet_x_collisions(firebullet)
            firebullet.rect.y += firebullet.y_vel
            self.check_firebullet_y_collisions(firebullet)
            firebullet.y_vel += firebullet.gravity
        self.delete_if_off_screen(firebullet)

    def bounce_firebullet(self, firebullet):

        """
        Simulates firebullet bounce off ground
        """

        firebullet.y_vel = -8
        if firebullet.direction == c.RIGHT:
            firebullet.x_vel = 15
        else:
            firebullet.x_vel = -15
        if firebullet in self.powerup_group:
            firebullet.state = c.BOUNCING

    def check_firebullet_x_collisions(self, firebullet):

        """
        Firebullet collisions along x axis
        """

        collide_group = pg.sprite.Group(self.ground_group,
                                        self.pipe_group,
                                        self.step_group,
                                        self.coin_box_group,
                                        self.brick_group)

        collider = pg.sprite.spritecollideany(firebullet, collide_group)

        if collider:
            firebullet.kill()
            self.sprites_about_to_die_group.add(firebullet)
            firebullet.explode_transition()

    def check_firebullet_y_collisions(self, firebullet):

        """
        Firebullet collisions along y axis
        """

        collide_group = pg.sprite.Group(self.ground_group,
                                        self.pipe_group,
                                        self.step_group,
                                        self.coin_box_group,
                                        self.brick_group)

        collider = pg.sprite.spritecollideany(firebullet, collide_group)
        enemy = pg.sprite.spritecollideany(firebullet, self.enemy_group)
        shell = pg.sprite.spritecollideany(firebullet, self.shell_group)

        if collider and (firebullet in self.powerup_group):
            firebullet.rect.bottom = collider.rect.y
            self.bounce_firebullet(firebullet)
        elif enemy:
            self.firebullet_kill(firebullet, enemy)
        elif shell:
            self.firebullet_kill(firebullet, shell)

    def firebullet_kill(self, firebullet, enemy):

        """
        Kills enemy if hit with firebullet
        """

        prepare_game.SFX['kick'].play()
        self.game_labels[c.SCORE] += 100
        self.moving_score_list.append(
            score.Score(enemy.rect.centerx - self.viewport.x,
                        enemy.rect.y, 100))
        firebullet.kill()
        enemy.kill()
        self.sprites_about_to_die_group.add(enemy, firebullet)
        enemy.start_death_jump(firebullet.direction)
        firebullet.explode_transition()

    def check_if_falling(self, sprite, sprite_group):

        """
        Checks if sprite should enter a falling state
        """

        sprite.rect.y += 1
        if pg.sprite.spritecollideany(sprite, sprite_group) is None:
            if sprite.state != c.JUMP:
                sprite.state = c.FALL

        sprite.rect.y -= 1

    def delete_if_off_screen(self, enemy):

        """
        Removes enemy from sprite groups if 500 pixels left off the screen,
        underneath the bottom of the screen, or right of the screen if shell
        """

        if enemy.rect.x < (self.viewport.x - 300):
            enemy.kill()
        elif enemy.rect.y > (self.viewport.bottom):
            enemy.kill()
        elif enemy.state == c.SHELL_SLIDE:
            if enemy.rect.x > (self.viewport.right + 500):
                enemy.kill()

    def check_for_char_death(self):

        """
        Restarts the level if char is dead
        """

        if self.char.rect.y > c.SCREEN_HEIGHT and not self.char.in_castle:
            self.char.dead = True
            self.char.x_vel = 0
            self.state = c.FROZEN
            self.game_labels[c.CHAR_DEAD] = True
        if self.char.dead:
            self.play_death_song()

    def play_death_song(self):
        if self.death_timer == 0:
            self.death_timer = self.current_time
        elif (self.current_time - self.death_timer) > 3000:
            self.set_game_labels_values()
            self.done = True

    def set_game_labels_values(self):

        """
        Sets the new game values
        after a player's death
        """

        if self.game_labels[c.SCORE] > self.persist[c.TOP_SCORE]:
            self.persist[c.TOP_SCORE] = self.game_labels[c.SCORE]
        if self.char.dead:
            self.persist[c.LIVES] -= 1

        if self.persist[c.LIVES] == 0:
            self.next = c.GAME_OVER
            self.game_labels[c.CAMERA_START_X] = 0
        elif self.char.dead is False:
            self.next = c.MAIN_MENU
            self.game_labels[c.CAMERA_START_X] = 0
        elif self.overhead_labels_display.time == 0:
            self.next = c.TIME_OUT
        else:
            if self.char.rect.x > 3670 \
                    and self.game_labels[c.CAMERA_START_X] == 0:
                self.game_labels[c.CAMERA_START_X] = 3440
            self.next = c.LOAD_SCREEN

    def check_if_time_out(self):

        """
        Check if time has run down to 0
        """

        if self.overhead_labels_display.time <= 0 \
                and not self.char.dead \
                and not self.char.in_castle:
            self.state = c.FROZEN
            self.char.start_death_jump(self.game_labels)

    def update_viewport(self):

        """
        Changes the view of the camera
        """

        third = self.viewport.x + self.viewport.w//3
        char_center = self.char.rect.centerx
        char_right = self.char.rect.right

        if self.char.x_vel > 0 and char_center >= third:
            mult = 0.5 if char_right < self.viewport.centerx else 1
            new = self.viewport.x + mult * self.char.x_vel
            highest = self.level_rect.w - self.viewport.w
            self.viewport.x = min(highest, new)

    def update_while_in_castle(self):

        """
        Updates while the main char is in castle at the end of the level
        """

        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_labels)
        self.overhead_labels_display.update(self.game_labels)
        if self.overhead_labels_display.state == c.END_OF_LEVEL:
            self.state = c.FLAG_AND_FIREWORKS

    def update_fireworks(self):

        """
        Updates the level for the fireworks
        """

        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_labels)
        self.overhead_labels_display.update(self.game_labels)

        self.end_game()

    def end_game(self):

        """
        Ends the game
        """
        self.current_time = 0
        if self.current_time == 0:
            self.set_game_labels_values()
            self.next = c.LOAD_SCREEN2
            self.sound_manager.stop_music()
            self.done = True

    def blit_everything(self, surface):

        """
        Blit all sprites to the main surface
        """

        self.level.blit(self.background, self.viewport, self.viewport)
        self.powerup_group.draw(self.level)
        self.coin_group.draw(self.level)
        self.brick_group.draw(self.level)
        self.coin_box_group.draw(self.level)
        self.sprites_about_to_die_group.draw(self.level)
        self.shell_group.draw(self.level)

        self.brick_pieces_group.draw(self.level)
        self.char_and_enemy_group.draw(self.level)
        surface.blit(self.level, (0, 0), self.viewport)
        self.overhead_labels_display.draw(surface)
        for score in self.moving_score_list:
            score.draw(surface)
