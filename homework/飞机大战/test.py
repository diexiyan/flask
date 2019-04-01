import pygame,time
pygame.init()
screen_rect=pygame.Rect(0,0,512,768)
screen=pygame.display.set_mode((screen_rect.width,screen_rect.height),0,32)
class I(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image=pygame.image.load(image_path)
        self.rect=self.image.get_rect()
        self.rect.x=50
        self.rect.y=50
        self.grop=pygame.sprite.Group()
def dead():
    il=I("./images/boum/ting6.png")
    for i in range(6, 10):
        im = "./images/boum/ting" + str(i) + '.png'
        print(im)
        iobj=I(im)
        iobj.grop.add(iobj)
        iobj.grop.update()
        iobj.grop.draw(screen)
        pygame.display.update()
        time.sleep(0.08)
        del iobj
