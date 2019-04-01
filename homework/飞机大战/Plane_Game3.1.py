import random,time, pygame.mixer, pygame
pygame.mixer.init()
pygame.font.init()
score = 0
"""敌机开火"""


class GameSprite(pygame.sprite.Sprite):
    """游戏类型，流程和初始化资源"""
    def __init__(self, image_path, x=0, y=0, speed=3):
        """初始化资源，image,speed,rect,x,y"""
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """游戏更新"""
        self.event()
        self.move()
        self.colli_kill()

    def event(self):
        """游戏事件"""
        # 获取事件
        event_list = pygame.event.get()
        # 时间不为空，判断：
        if len(event_list) > 0:
            # 遍历
            for event in event_list:
                # 判断退出事件
                if event.type == pygame.QUIT:
                    # 清空资源
                    core.group_sprite.empty()
                    core.group_enemy.empty()
                    core.bullets_group.empty()
                    pygame.quit()
                # 生成敌机判断
                if event.type == core.CREATEMENY:
                    core.hero.creat_enemy()
                if event.type == core.CREATEBULLET:
                    # 船舰炮弹
                    p = PaoDan('./images/hero/timg.png', x=random.randint(1, core.screen_rect.width - 150), y=0, speed=6)
                    core.paodan_group.add(p)


    def move(self):
        """游戏移动方法"""
        # 移动：速度为正，向下运动
        self.rect.y += self.speed
        # 边界判断
        self.is_out()

    def is_out(self):
        """边界判断，越界死亡"""
        if self.rect.y < -self.rect.height or self.rect.y > core.screen_rect.height:
            self.kill()

    def colli_kill(self):
        """碰撞检测"""


class BackgroundSprite(GameSprite):
    """背景类型"""
    def is_out(self):
        """背景边界判断"""
        if self.rect.y > core.screen_rect.height:
            self.rect.y = -core.screen_rect.height


class PaoDan(GameSprite):
    """炮弹"""


class EnemySprite(GameSprite):
    """敌机类型"""
    def __init__(self, image_path, x=0, y=0, speed=3, life=10):
        """初始化添加生命值life, score,"""
        super().__init__(image_path, x, y, speed)
        self.life = life
        global score

    def fire(self):
        """开火,出现后调用"""
        # x坐标
        x = self.rect.x+20
        image_path = core.step_dict.get('bullet')[0]
        speed = core.step_dict.get('speed')[3]
        if len(core.bullets_group) < 100:
            bullet1 = BulletSprite(image_path, x=x, y=self.rect.y+10, speed=speed)
            core.player_music("./music/enemy_down.mp3", 1)
            # 添加到精灵族
            core.bullets_group.add(bullet1)
        if len(core.step_dict.get('enemy')) > 1:
            if len(core.bullets_group) < 100:
                bullet2 = BulletSprite(core.step_dict.get('bullet')[1], x=x + 34, y=self.rect.y - 10, speed=speed)
                core.player_music("./music/enemy_down.mp3", 1)
                core.bullets_group.add(bullet2)

    def is_out(self):
        """边界判断，敌机数位2，英雄死亡"""
        if self.rect.y < -self.rect.height or self.rect.y > core.screen_rect.height:
            self.kill()
            core.count += 1

    def colli_kill(self):
        """碰撞检测"""
        for enemy in core.group_enemy:
            # 将敌机与子弹精灵组做碰撞检测，若相撞返回被撞的子弹精灵对象，第三个参数表示销毁相撞的子弹，第四个表示非透明区碰撞检测
            collide_bullet = pygame.sprite.spritecollide(enemy, core.bullets_group, True)

            if collide_bullet:
                # 子弹击中敌机，敌机生命值减1
                enemy.life -= 1
                if enemy.life == 0:
                    # 敌机死亡分数加10
                    enemy.kill()
                    enemy.dead()
                    global score
                    if self.__class__ != EnemySprite:
                        score += 10
                        core.is_step(score)
        if self.__class__ == Hero:
            collide_hero = pygame.sprite.spritecollide(self, core.group_enemy, True)
            if collide_hero:
                # 同归于尽，游戏结束
                self.life -= 1

    def dead(self):
        """死亡特效"""
        for i in range(6, 10):
            im = "./images/boum/ting" + str(i) + '.png'
            iobj = BackgroundSprite(im, speed=0)
            iobj.rect.x = self.rect.x+15
            iobj.rect.y = self.rect.y+10
            gb = pygame.sprite.Group(iobj)
            gb.update()
            gb.draw(core.screen)
            pygame.display.update()
            time.sleep(0.01)


class Hero(EnemySprite):
    def move(self):
        """移动，"""
        self.is_out()

    def is_out(self):
        """边界判断，越界不动"""
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.x > core.screen_rect.width - self.rect.width:
            self.rect.x = core.screen_rect.width - self.rect.width
        if self.rect.y > core.screen_rect.height - self.rect.height:
            self.rect.y = core.screen_rect.height - self.rect.height

    def colli_kill(self):
        super().colli_kill()
        pao_list = pygame.sprite.spritecollide(self, core.paodan_group, True)

        if pao_list:
            global score
            score -= 20


    def creat_enemy(self):
        """生成敌机函数,速度为负，位置为随机数返回坐标值"""
        x = random.randint(1, core.screen_rect.width - 150)
        y = -20
        speed = core.step_dict.get('speed')[1]
        if len(core.step_dict.get('enemy')) > 1:
            i = random.randint(0, 1)
            image_path = core.step_dict.get('enemy')[i]
            emeny2 = EnemySprite(image_path, x=x, y=y, speed=speed)
            core.group_enemy.add(emeny2)
        else:
            emeny1 = EnemySprite(core.step_dict.get('enemy')[0], x=x, y=y, speed=speed)
            core.group_enemy.add(emeny1)

    def event(self):
        """事件判断"""
        super().event()
        # 判断上下左右移动
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if key_down[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if key_down[pygame.K_UP]:
            self.rect.y -= self.speed
        if key_down[pygame.K_DOWN]:
            self.rect.y += self.speed
        if key_down[pygame.K_SPACE]:
            # 连续发射子弹判断
            self.fire()
        self.colli_kill()


class BulletSprite(GameSprite):
    """运动速度为负"""


class Core:
    """系统初始化保存资源"""
    def __init__(self, step):
        """初始化资源组"""
        self.screen_rect = pygame.Rect(0, 0, 512, 768)
        self.screen = pygame.display.set_mode((self.screen_rect.width, self.screen_rect.height), 0, 32)
        # 资源字典
        self.step_data = step
        self.group_sprite = pygame.sprite.Group()
        self.group_enemy = pygame.sprite.Group()
        self.bullets_group = pygame.sprite.Group()
        self.paodan_group = pygame.sprite.Group()
        self.CREATEMENY = pygame.USEREVENT
        self.CREATEBULLET = pygame.USEREVENT
        pygame.time.set_timer(self.CREATEMENY, random.randint(1000, 2000))

        self.step_dict = self.step_data.get('1')
        # 字体
        self.font = pygame.font.Font('./font/f.ttf', 30)
        # 敌机生成及时期
        self.count = 0
        # 英雄飞机
        hero_path = self.step_dict.get('hero')[0]
        hero_speed = self.step_dict.get('speed')[2]
        self.hero = Hero(image_path=hero_path, speed=hero_speed, life=500)
        self.hero.rect.x = 200
        self.hero.rect.y = 200
        self.hero.life = 3
        # 界面资源组
        self.sprite_ziyuan = pygame.sprite.Group()
        # 历史记录
        self.history = self.read_data()

    def read_data(self):
        with open("./1.txt", "r") as file:
            n = file.read()
            return n

    def save_data(self):
        with open("./1.txt", "w") as file:
            file.write(str(self.history))

    def player_music(self, path, i):
        """"播放音乐"""
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(i)

    def end(self):
        """展示结束界面"""
        # 判断历史最高分
        if int(self.history) < score:
            self.history = score
            # 保存
            self.save_data()
        # 加载结束图片
        en = BackgroundSprite('./images/start/ending.jpg', speed=0)
        en1 = BackgroundSprite('./images/hero/hero.png', speed=0)
        self.sprite_ziyuan.add(en, en1)
        core.player_music("./music/game_over.mp3", 1)
        self.sprite_ziyuan.update()
        self.sprite_ziyuan.draw(self.screen)
        ziti = self.font.render((' '+str(score)), True, (255, 255, 255))
        self.screen.blit(ziti, (240, 320))
        pygame.display.update()

        while True:
            # 鼠标控制事件
            mouse_event = pygame.event.get()
            is_ok = False
            if len(mouse_event) > 0:
                for eve_mou in mouse_event:
                    if eve_mou.type == pygame.MOUSEBUTTONDOWN:
                        if eve_mou.button == 1 and en1.rect.collidepoint(eve_mou.pos):
                            is_ok = True
                    elif eve_mou.type == pygame.QUIT:
                        # 清空资源
                        core.group_sprite.empty()
                        core.group_enemy.empty()
                        core.bullets_group.empty()
                        pygame.quit()
            if is_ok:
                break

    def is_step(self, s=0):
        if 40 < s <= 80:
            step = '2'
            self.step_dict = self.step_data.get(step)
            if s == 50:
                global score
                score = 0
                core.count = 0
                return self.engine()
        elif 80 < s:
            step = '3'
            self.step_dict = self.step_data.get(step)
            if s == 90:
                score = 0
                core.count = 0
                return self.engine()
        elif 0 <= s <= 40:
            print("第1关")

    def init_info(self):
        """初始化资源组"""
        pygame.init()
        pygame.display.set_caption("雷霆战机")
        # 背景资源
        bg_path = self.step_dict.get('bg')[0]
        bg_speed = self.step_dict.get('speed')[0]
        bg1 = BackgroundSprite(image_path=bg_path, speed=bg_speed, x=0, y=0)
        bg2 = BackgroundSprite(image_path=bg_path, speed=bg_speed, x=0, y=-bg1.rect.height)
        self.group_sprite.add(bg1, bg2, self.hero)
        global clock
        # 刷新频率控制
        clock = pygame.time.Clock()

    def engine(self):
        self.sprite_ziyuan.empty()
        self.group_sprite.empty()
        self.group_enemy.empty()
        self.bullets_group.empty()

        self.init_info()

        if step == 1:
            pygame.time.set_timer(self.CREATEBULLET, random.randint(3000, 4000))
        elif step == 2:
            pygame.time.set_timer(self.CREATEBULLET, random.randint(2000, 3000))
        else:
            pygame.time.set_timer(self.CREATEBULLET, random.randint(2000, 3000))

        while True:
            clock.tick(30)

            self.sprite_ziyuan.update()
            self.sprite_ziyuan.draw(self.screen)

            self.group_sprite.update()
            self.group_sprite.draw(self.screen)

            ziti = self.font.render(('score:'+str(score)), True, (239, 224, 60))
            hp = self.font.render(('hp:'+str(self.hero.life)), True, (239, 224, 60))
            history = self.font.render(('history:'+str(self.history)), True, (239, 224, 60))
            core.screen.blit(ziti, (5, 5))
            core.screen.blit(hp, (5, 40))
            core.screen.blit(history, (5, 80))

            self.group_enemy.update()
            self.group_enemy.draw(self.screen)

            self.bullets_group.update()
            self.bullets_group.draw(self.screen)

            self.paodan_group.update()
            self.paodan_group.draw(self.screen)

            pygame.display.update()

            # 死亡
            if self.hero.life <= 0 or self.count == 5:
                # 重置判断条件
                self.count = 0
                self.hero.life = 3
                self.end()
                self.engine()

    def login(self):
        self.player_music("./music/game_music.mp3", -1)
        # 登录图片
        login = BulletSprite('./images/start/start.png', speed=0)
        start = BulletSprite('./images/start/start_ziti.png', 100, 450, speed=0)
        self.sprite_ziyuan.add(login, start)
        while True:
            self.sprite_ziyuan.update()
            self.sprite_ziyuan.draw(self.screen)
            pygame.display.update()
            # 鼠标控制事件
            mouse_enent = pygame.event.get()
            if len(mouse_enent) > 0:
                for eve_mou in mouse_enent:
                    if eve_mou.type == pygame.MOUSEBUTTONDOWN:
                        if eve_mou.button == 1 and start.rect.collidepoint(eve_mou.pos):
                            self.engine()


step = {
    '1': {"bg": ['./images/back/step1.jpg'],
          'enemy': ['./images/enemy/enemy3.png'],
          'hero': ['./images/hero/hero.png'],
          'bullet': ['./images/bullet/bullet1.png'],
          'speed': [3, random.randint(4, 6), 20, -12]
          },
    '2': {"bg": ['./images/back/step2.jpg'],
          'enemy': ['./images/enemy/enemy4.png'],
          'hero': ['./images/hero/hero.png'],
          'bullet': ['./images/bullet/bullet2.png'],
          'speed': [3, random.randint(6, 8), 20, -12]
          },
    '3': {"bg": ['./images/back/step3.jpg'],
          'enemy': ['./images/enemy/enemy4.png', './images/enemy/enemy3.png'],
          'hero': ['./images/hero/hero.png'],
          'bullet': ['./images/bullet/bullet1.png', './images/bullet/bullet3.png'],
          'speed': [3, random.randint(8, 10), 20, -15]
          }
}
core = Core(step)
core.login()
