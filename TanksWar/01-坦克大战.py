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


game = TankMain()
game.startGame()