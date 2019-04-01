import pygame
screen = (0,0,512,768)
# screen_rect = pygame.Rect()
screen1=pygame.display.set_mode((512,768),0,32)
pygame.init()

# font = pygame.font.Font("font/Interstate Cond Mono - Blk.ttf", 48)
"""获取字体矩形对象"""
score_rect = font.render("score" + str("20"), True, (10, 200, 150)).get_rect()
# 设置分数位置
score_rect.left, score_rect.top = (50), (50)
pygame.display.update()