"""面向对象扩展开发
修改数据字典step by bh at 20190223"""
import pygame
import random,time
pygame.font.init()
score = 0


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
        print("yflydfryjs")

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
                    pygame.quit()
                # 生成敌机判断
                if event.type == core.CREATEMENY:
                    core.creat_enemy()

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
            # 添加到精灵族
            core.bullets_group.add(bullet1)
        if len(core.step_dict.get('enemy')) > 1:
            if len(core.bullets_group) < 100:
                bullet2 = BulletSprite(core.step_dict.get('bullet')[1], x=x + 34, y=self.rect.y - 10, speed=speed)
                core.bullets_group.add(bullet2)

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
                    print(score, self.__class__)
                    if self.__class__ != EnemySprite:
                        score += 10
                        # self.kill()
                        core.is_step(score)
        if self.__class__ == Hero:
            collide_hero = pygame.sprite.spritecollide(self, core.group_enemy, True)
            if collide_hero:
                # 同归于尽，游戏结束
                core.end()

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
            time.sleep(0.05)


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
        if self.rect.y > core.screen_rect.height:
            self.rect.y = core.screen_rect.height

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
        # 发射子弹
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
        self.CREATEMENY = pygame.USEREVENT
        pygame.time.set_timer(self.CREATEMENY, random.randint(1000, 2000))
        self.step_dict = self.step_data.get('1')

        self.font = pygame.font.Font('./font/f.ttf', 30)

        # 英雄飞机
        hero_path = self.step_dict.get('hero')[0]
        hero_speed = self.step_dict.get('speed')[2]
        self.hero = Hero(image_path=hero_path, speed=hero_speed, life=500)
        self.hero.rect.x = 200
        self.hero.rect.y = 200
        # 界面资源组
        self.sprite_ziyuan = pygame.sprite.Group()

    def end(self):
        """展示结束界面"""
        # 清空资源
        self.group_sprite.empty()
        self.group_enemy.empty()
        self.bullets_group.empty()
        # 加载结束图片
        en = BackgroundSprite('./images/start/ending.jpg', speed=0)
        self.sprite_ziyuan.add(en)
        self.sprite_ziyuan.update()
        self.sprite_ziyuan.draw(self.screen)
        ziti = self.font.render((' '+str(score)), True, (255, 255, 255))
        self.screen.blit(ziti, (240, 320))
        pygame.display.update()
        time.sleep(12)

    def is_step(self, score=0):
        print("is_step", score)
        if 10 < score <= 20:
            self.group_sprite.empty()
            step = '2'
            self.step_dict = self.step_data.get(step)
            return self.engine()
        elif 20 < score:
            self.group_sprite.empty()
            step = '3'
            self.step_dict = self.step_data.get(step)
            return self.engine()
        elif 0 <= score <= 10:
            print("第1关")
        else:
            self.end()

    def creat_enemy(self):
        """生成敌机函数,速度为负，位置为随机数返回坐标值"""
        x = random.randint(1, self.screen_rect.width - 150)
        y = -20
        speed = random.randint(1, 3)
        emeny1 = EnemySprite(self.step_dict.get('enemy')[0], x=x, y=y, speed=speed)
        core.group_enemy.add(emeny1)
        if len(self.step_dict.get('enemy')) > 1:
            count = 1
            count += 1
            if (count % 1000) == 0:
                count = 0
                emeny2 = EnemySprite(self.step_dict.get('enemy')[1], x=random.randint(1, self.screen_rect.width - 150), y=y, speed=speed)
                self.group_enemy.add(emeny2)

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
        self.init_info()
        while True:
            print(score, self.step_dict)
            clock.tick(30)
            self.group_sprite.update()
            self.group_sprite.draw(self.screen)
            ziti = self.font.render(('score:'+str(score)), True, (239, 224, 60))
            core.screen.blit(ziti, (5, 5))
            self.group_enemy.update()
            self.group_enemy.draw(self.screen)

            self.bullets_group.update()
            self.bullets_group.draw(self.screen)
            self.sprite_ziyuan.update()
            self.sprite_ziyuan.draw(self.screen)
            pygame.display.update()

    def login(self):
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
                            return 'ok'
                            # self.engine()
                            # break


step = {
    '1': {"bg": ['./images/back/step1.jpg'],
          'enemy': ['./images/enemy/enemy3.png'],
          'hero': ['./images/hero/hero.png'],
          'bullet': ['./images/bullet/bullet1.png'],
          'speed': [3, random.randint(3, 6), 20, -8]
          },
    '2': {"bg": ['./images/back/step2.jpg'],
          'enemy': ['./images/enemy/enemy4.png'],
          'hero': ['./images/hero/hero.png'],
          'bullet': ['./images/bullet/bullet2.png'],
          'speed': [3, random.randint(3, 6), 20, -12]
          },
    '3': {"bg": ['./images/back/step3.jpg'],
          'enemy': ['./images/enemy/enemy4.png', './images/enemy/enemy3.png'],
          'hero': ['./images/hero/hero.png'],
          'bullet': ['./images/bullet/bullet1.png', './images/bullet/bullet3.png'],
          'speed': [3, random.randint(3, 6), 20, -15]
          }
}
core = Core(step)
core.login()
