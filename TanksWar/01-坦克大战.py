# coding:utf-8
import pygame,sys
from pygame.locals import *

"""坦克游戏的主程序"""
class TankMain():
    #开始游戏
    def startGame(self):
        #模块初始化，加载系统资源
        pygame.init()
        #创建一个屏幕，屏幕（窗口）的大小，窗口的特性
        screen = pygame.display.set_mode((600,500),0,32)
        #设置主屏幕标题
        pygame.display.set_caption('坦克大战')
        while True:
            #设置屏幕的背景色为黑色
            screen.fill((0,0,0))
            #显示左上角文字
            screen.blit(self.write_text(),(0,5))
            #监听事件
            self.get_event()


            #显示重置
            pygame.display.update()

    #获取事件
    def get_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stopGame()
            elif event.type == KEYDOWN:
                if event.key == K_LALT:
                    pass
                if event.key == K_RIGHT:
                    pass
                if event.key == K_UP:
                    pass
                if event.key == K_DOWN:
                    pass
                if event.key == K_ESCAPE:
                    #键盘的ESC键，退出游戏
                    self.stopGame()

    #关闭游戏
    def stopGame(self):
        pygame.quit()
        sys.exit()

    #在屏幕左上角显示文字内容
    def write_text(self):
        font = pygame.font.SysFont("华文宋体",20)
        text_sf = font.render("敌方坦克数量为：5",True,(255,0,0))
        return text_sf

"""坦克大战所有对象的父类"""
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #所有对象功能的属性

class Tank(BaseItem):
    width=50
    height=50
    def __init__(self,screen):
        super().__init__(self)
        self.screen=screen
        self.derection="D" #坦克方向，默认往下(上下左右)
        self.images={} #坦克所有图片
        self.images["L"] = pygame.image.load("images/tankL.gif")
        self.images["R"] = pygame.image.load("images/tankR.gif")
        self.images["U"] = pygame.image.load("images/tankU.gif")
        self.images["D"] = pygame.image.load("images/tankD.gif")
        self.image=self.images[self.derection]#坦克图片由方向决定
        self.live=True#决定坦克是否消灭了

    def display(self):
        self.screen.blit()


game = TankMain()
game.startGame()