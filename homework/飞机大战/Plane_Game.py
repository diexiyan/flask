import pygame,random


class GameSprite(pygame.sprite.Sprite):
    """游戏父类"""
    def __init__(self, image_path, speed = 1, x = 0, y = 0):
        """__init__(self, image_path, speed = 3, x = 0, y = 0)"""
        super().__init__()
        self.image = pygame.image.load(image_path)
        # 图片的大小
        self.rect = self.image.get_rect()
        self.speed = speed
        # 图片出现位置
        # self.x = x
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.event()
        self.move()

    def event(self):
        """游戏事件"""
        # 获得键盘事件
        even_list = pygame.event.get()
        if len(even_list) > 0:
            for ene in even_list:
                # 退出事件
                if ene.type == pygame.QUIT:
                    pygame.quit()


    def move(self):
        """移动，边界判断"""
        self.rect.y += self.speed
        # print("移动", self.speed, self.rect.y)


class BackGroundSprite(GameSprite):
    """背景类"""
    def move(self):
        """背景图移动，边界判断"""
        # 图片移动
        super().move()
        # 连接图片
        if self.rect.y >= screen_rect.height:
            self.rect.y = -self.rect.height


class Hero(GameSprite):
    def move(self):
        """飞机移动及边界判断"""
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x > screen_rect.width - self.rect.width:
            self.rect.x = screen_rect.width - self.rect.width
        if self.rect.y > screen_rect.height - self.rect.height:
            self.rect.y = screen_rect.height - self.rect.height

    def event(self):
        """飞机事件"""
        # 事件获取
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_LEFT]:
            print("左")
            self.rect.x -= self.speed
        if key_down[pygame.K_RIGHT]:
            print("右")
            self.rect.x += self.speed
        if key_down[pygame.K_UP]:
            print("上")
            self.rect.y -= self.speed
        if key_down[pygame.K_DOWN]:
            print("下")
            self.rect.y += self.speed
        if key_down[pygame.K_SPACE]:
            print("开火")
            self.fire()

    def fire(self):
        bullets = Bullets("./images/bullet/bullet2.png", speed=-3, x=self.rect.x+22, y=self.rect.y+20)
        bullets_group.add(bullets)


class Bullets(GameSprite):

    def move(self):
        """边界判断，"""
        super().move()
        if self.rect.x < 0 \
                or self.rect.y < 0 \
                or self.rect.x > screen_rect.width \
                or self.rect.x > screen_rect.height:
            self.kill()


class enemy_sprites(GameSprite):

    def move(self):
        super().move()
        if self.rect.y > screen_rect.height:
            self.kill()


pygame.init()
# 坐标值，大小
screen_rect = pygame.Rect(0, 0, 512, 768)
# 创建窗口：大小（元组），是否全屏，颜色深度（8的倍数）
screen = pygame.display.set_mode((screen_rect.width, screen_rect.height), 0, 32)

# 背景图片
bg1 = BackGroundSprite('./images/back/step1.jpg')
bg2 = BackGroundSprite('./images/back/step1.jpg')
bg2.rect.y = -bg2.rect.height
# 精灵组对象,添加精灵
# 英雄飞机
hero = Hero('./images/hero/hero.png', x=200, y=300)
game_group = pygame.sprite.Group(bg1, bg2, hero)

# 子弹精灵组
bullets_group = pygame.sprite.Group()
# 敌机精灵组
enemy_group = pygame.sprite.Group()
# 计数器
count = 0

while True:
    count +=1
    print(count)
    if count ==1000:
        print(count,"低级")
        count = 0
        enemy = enemy_sprites("./images/emery/Enemy3.png",speed=random.randint(1,3),x=random.randint(0,screen_rect.width-200),y=0)
        print(enemy.speed)
        enemy_group.add(enemy)
    # 更新
    game_group.update()
    bullets_group.update()
    enemy_group.update()
    # 填充
    game_group.draw(screen)
    bullets_group.draw(screen)
    enemy_group.draw(screen)
    #碰撞检测
    pygame.sprite.groupcollide(enemy_group,bullets_group,False,True)

    # 展示屏幕
    pygame.display.update()
