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
    drawObjects()
    drawPlayer()
    drawEnd()
    
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
    
    
def drawObjects():
    for row in range(gameParameters.ROWS):
        for col in range(gameParameters.COLUMNS):
            if 0 < gameParameters.board[row][col] < 10:
                pygame.draw.circle(screen, 'Yellow', ((col + 0.5)*BLOCK, (row+0.5)*BLOCK), BLOCK/2, 0)
            if 10 <= gameParameters.board[row][col] < 20:
                pygame.draw.circle(screen, 'Red', ((col + 0.5)*BLOCK, (row+0.5)*BLOCK), BLOCK/2, 0)
            if 20 < gameParameters.board[row][col] < 30:
                pygame.draw.circle(screen, 'Purple', ((col + 0.5)*BLOCK, (row+0.5)*BLOCK), BLOCK/2, 0)
            if 30 < gameParameters.board[row][col] < 40:
                pygame.draw.rect(screen, 'Purple', pygame.Rect(col * BLOCK, row * BLOCK, BLOCK, BLOCK))
                

def drawEnd():
    pygame.draw.rect(screen, 'Yellow', pygame.Rect(gameParameters.endX * BLOCK,
                                                   gameParameters.endY * BLOCK,
                                                   BLOCK,
                                                   BLOCK))
            
    
