"""面向对象扩展开发
修改数据字典step by bh at 20190223"""
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
                    pygame.quit()
                # 生成敌机判断
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

    def colli_kill(self):
        """碰撞检测"""
        pygame.sprite.groupcollide(core.group_enemy, core.bullets_group, True, True)


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
        self.score = None

    def fire(self,  speed=-3):
        """开火,出现后调用"""
        # x坐标
        x = self.rect.x+20
        if len(core.bullets_group) < 100:
            bullet = BulletSprite(core.step_data.get('bullet').get('1').get('image_path')[0], x=x, y=self.rect.y+10, speed=speed)
            # 添加到精灵族
            core.bullets_group.add(bullet)

    def colli_kill(self):
        """碰撞检测"""
        pass

    def wound(self):
        """受伤,碰撞测试调用"""
        print("""碰撞检测""", self.life)
        self.life -= 5
        print("""碰撞检测""", self.life)

        if self.life <= 0:
            print("""碰撞检测""", self.life)

            self.kill()
            return 'ok'
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
            # 连续发射子弹判断
            self.fire()

    def add_score(self):
        self.score += 10


class BulletSprite(GameSprite):
    """运动速度为负"""


class Core:
    """系统初始化保存资源"""

    def __init__(self, step):
        """初始化资源组"""
        self.screen_rect = pygame.Rect(0, 0, 520, 780)
        self.screen = pygame.display.set_mode((self.screen_rect.width, self.screen_rect.height), 0, 32)
        # 资源字典
        self.step_data = step
        self.group_sprite = pygame.sprite.Group()
        self.group_enemy = pygame.sprite.Group()
        self.bullets_group = pygame.sprite.Group()
        self.CREATEMENY = pygame.USEREVENT
        pygame.time.set_timer(self.CREATEMENY, random.randint(1000, 3000))
        self.step_dict = None
    def is_step(self,score=0):
        if score < 200:
            step='2'
        elif score<300:
            step='3'
        else:
            step='1'
        # 参数字典
        self.step_dict = self.step_data.get(step)

    def creat_enemy(self):
        """生成敌机函数,速度为负，位置为随机数返回坐标值"""
        x = random.randint(1, self.screen_rect.width - 150)
        y = -20
        speed = random.randint(1, 3)
        emeny = EnemySprite(self.step_data.get('enemy').get('1').get('image_path')[0], x=x, y=y, speed=speed)
        core.group_enemy.add(emeny)

    def init_info(self):
        """初始化资源组"""
        pygame.init()

        # 英雄飞机
        hero_path = self.step_data.get('hero').get('1').get('image_path')[0]
        hero_speed = self.step_data.get('hero').get('1').get('speed')[0]
        hero = Hero(image_path=hero_path, speed=hero_speed, life=500)
        hero.rect.x = 200
        hero.rect.y = 200
        print("----------------------", hero_path)

        # 背景资源
        bg_path = self.step_data.get('bg').get('1').get('image_path')[0]
        bg_speed = self.step_data.get('bg').get('1').get('speed')[0]
        bg1 = BackgroundSprite(image_path=bg_path, speed=bg_speed, x=0, y=0)
        bg2 = BackgroundSprite(image_path=bg_path, speed=bg_speed, x=0, y=-bg1.rect.height)
        self.group_sprite.add(bg1, bg2, hero)

        global clock
        # 刷新频率控制
        clock = pygame.time.Clock()

    def engine(self):
        self.init_info()
        while True:
            clock.tick(30)
            self.group_sprite.update()
            self.group_sprite.draw(self.screen)

            self.group_enemy.update()
            self.group_enemy.draw(self.screen)

            self.bullets_group.update()
            self.bullets_group.draw(self.screen)

            pygame.display.update()


step = {
    "enemy": {'1': {'image_path': ["./images/enemy/enemy3.png"]},
              '2': {'image_path': ["./images/enemy/enemy3.png"]}
              },
    'bg': {'1': {'speed': [3], 'image_path': ["./images/back/step1.jpg"]},
           '2': {'speed': [1], 'image_path': ["./images/back/step1.jpg"]}
           },
    'hero': {'1': {'speed': [8], 'image_path': ["./images/hero/hero.png"]},
             '2': {'speed': [1], 'image_path': ["./images/hero/hero.png"]}
             },
    'bullet': {'1': {'speed': [40], 'image_path': ["./images/bullet/bullet2.png"]},
               '2': {'speed': [1], 'image_path': ["./images/bullet/bullet2.png"]}
               }
}
core = Core(step)
core.engine()
