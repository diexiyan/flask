"""面向对象扩展开发"""
import pygame
import random


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
                    # 退出
                    pygame.quit()
                # 生成敌机判断
                 # 添加一个地方飞机创建事件
                #
                if event.type == core.CREATEMENY:
                    # 添加时间限制
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
            print("越界了!")

    def colli_kill(self):
        """碰撞检测"""
        pass


class BackgroundSprite(GameSprite):
    """背景类型"""
    def is_out(self):
        """背景边界判断"""
        if self.rect.y > core.screen_rect.height:
            self.rect.y = -core.screen_rect.height


class EnemySprite(GameSprite):
    """敌机类型"""
    def __init__(self, image_path, x=0, y=0, speed=3):
        """初始化添加生命值life, score,"""
        super().__init__(image_path, x, y, speed)
        self.life = None
        self.score = None

    def fire(self, screen_rect, speed=-3):
        """开火,出现后调用"""
        # x坐标
        x = self.rect.x+20
        if len(core.bullets_group) < 10:
            bullet = BulletSprite(core.step_data.get('bullet')[0], x=x, y=self.rect.y+10, speed=speed)
            # 添加到精灵族
            core.bullets_group.add(bullet)

    def wound(self):
        """受伤,碰撞测试调用"""
        pass


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
            print("开火")
            # 连续发射子弹判断
            self.fire(core.screen_rect)


class BulletSprite(GameSprite):
    """运动速度为负"""


class Core:
    """系统初始化保存资源"""

    def __init__(self, step):
        """初始化资源组"""
        self.screen_rect = pygame.Rect(0, 0, 520, 780)
        self.screen = pygame.display.set_mode((self.screen_rect.width, self.screen_rect.height), 0, 32)
        # 资源字典
        self.step_data = step.get('1')
        self.group_sprite = pygame.sprite.Group()
        # self.group_hero = pygame.sprite.Group()
        self.group_enemy = pygame.sprite.Group()
        self.bullets_group = pygame.sprite.Group()
        self.CREATEMENY = pygame.USEREVENT
        pygame.time.set_timer(self.CREATEMENY, random.randint(1000, 3000))

    def creat_enemy(self):
        """生成敌机函数,速度为负，位置为随机数返回坐标值"""
        x = random.randint(1, self.screen_rect.width - 150)
        y = -20
        speed = self.step_data.get('speed')[1]
        # print(self.step_data.get('ememy')[0])
        emeny = EnemySprite(self.step_data.get('emery')[0], x=x, y=y, speed=speed)
        core.group_enemy.add(emeny)
        # return x, y

    def init_info(self):
        """初始化资源组"""
        pygame.init()

        # 英雄飞机
        # 英雄资源
        hero_path = self.step_data.get('hero')[0]
        hero_speed = self.step_data.get('speed')[2]
        hero = Hero(image_path=hero_path)
        hero.rect.x=200
        hero.rect.y=200
        print("----------------------",hero_path)

        # 背景资源
        bg_path = self.step_data.get('bg')[0]
        bg_speed = self.step_data.get('speed')[0]
        # print(bg_path, bg_speed)
        bg1 = BackgroundSprite(image_path=bg_path, speed=bg_speed, x=0, y=0)
        bg2 = BackgroundSprite(image_path=bg_path, speed=bg_speed, x=0, y=-bg1.rect.height)
        self.group_sprite.add(bg1,bg2,hero)
        self.group_sprite.add(bg2)
        # self.group_sprite.add(hero)

        # 添加一个用户自定义触发事件
        CREATEMENY = pygame.USEREVENT
        # 场景初始化:显示窗口
        global clock
        # 刷新频率控制
        clock = pygame.time.Clock()

    def engine(self):
        self.init_info()
        while True:
            clock.tick(60)
            self.group_sprite.update()
            self.group_sprite.draw(self.screen)

            self.group_enemy.update()
            self.group_enemy.draw(self.screen)

            self.bullets_group.update()
            self.bullets_group.draw(self.screen)

            pygame.display.update()


step = {
    '1': {"bg": ['./images/back/step1.jpg'],
          'emery': ['./images/enemy/enemy3.png'],
          'hero': ['./images/hero/hero.png'],
          'bullet': ['./images/bullet/bullet2.png'],
          'speed': [3, random.randint(1, 3), 3, 3]
          }
    # '2':{}
    # '3':{}
    # '4':{}
    # '5':{}
}
core = Core(step)
core.engine()
