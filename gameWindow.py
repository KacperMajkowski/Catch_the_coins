import pygame
import gameParameters

pygame.init()

BLOCK = 50

WIDTH = gameParameters.COLUMNS * BLOCK
HEIGHT = gameParameters.ROWS * BLOCK

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cap")

player = pygame.Surface((BLOCK, BLOCK))
player.fill('Green')

coin = pygame.Surface((BLOCK, BLOCK))
coin.fill('Yellow')


def updateWindow():
    clearScreen()
    drawCoins()
    drawPlayer()
    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()

    pygame.display.update()
    

def clearScreen():
    screen.fill('Black')
    
    
def drawPlayer():
    pygame.draw.rect(screen, 'Green', pygame.Rect(gameParameters.playerX * BLOCK,
                                                  gameParameters.playerY * BLOCK,
                                                  BLOCK,
                                                  BLOCK))
    
    
def drawCoins():
    for row in range(gameParameters.ROWS - 1):
        for col in range(gameParameters.COLUMNS - 1):
            if 0 < gameParameters.board[row][col] < gameParameters.playerID:
                pygame.draw.circle(screen, 'Yellow', ((col + 0.5)*BLOCK, (row+0.5)*BLOCK), BLOCK/2, 0)
            
    
