import pygame
import random
import time
pygame.font.init()
Height=1000
Width=563
Win=pygame.display.set_mode((Height,Width))
pygame.display.set_caption("SPACE EVADERS")
BG=pygame.image.load('bg1.jpg')
PW=40
PH=60
font=pygame.font.SysFont("comicsans",30)
Player_Velocity=5
star_vel=1
star_width=10
star_height=20
def draw(player,elapsed_time,stars):
    Win.blit(BG,(0,0))
    time_text=font.render(f"TIME:{round(elapsed_time)}s",1,"white")
    Win.blit(time_text,(10,10))
    pygame.draw.rect(Win,"orange",player)
    for star in stars:
        pygame.draw.rect(Win,"white",star)
    pygame.display.update()
    
def main():
    run=True
    player=pygame.Rect(300,499,PW,PH)
    clock=pygame.time.Clock()
    start_time=time.time()
    elapsed_time=0
    star_add_increment=2000
    star_count=0
    stars=[]
    hit=False
    while run:
        star_count+=clock.tick(60)
        elapsed_time=time.time()-start_time
        if star_count>star_add_increment:
            for _ in range(3):
                star_x=random.randint(0,Height-star_width)
                star=pygame.Rect(star_x,-star_height,star_width,star_height)
                stars.append(star)
            star_add_increment=max(2000,star_add_increment - 50)
            star_count=0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x-Player_Velocity>=0:
            player.x-=Player_Velocity
        if keys[pygame.K_RIGHT]and player.x+Player_Velocity<=960:
            player.x+=Player_Velocity
        if keys[pygame.K_UP]and player.y-Player_Velocity>=0:
            player.y-=Player_Velocity
        if keys[pygame.K_DOWN]and player.y+Player_Velocity<=505:
            player.y+=Player_Velocity
        for star in stars[:]:
            star.y+=star_vel
            if star.y>Height:
                stars.remove(star)
            elif star.y+ star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit=True
                break
        if hit:
            lost_text=font.render("You Lost!",1,"white")
            Win.blit(lost_text,(10,50))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        draw(player,elapsed_time,stars)
    pygame.quit()
if __name__=="__main__":
    main()
