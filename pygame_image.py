import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kt_img = pg.image.load("fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)
    kt_img3 = pg.transform.rotate(kt_img, 3)
    kt_img4 = pg.transform.rotate(kt_img, 6)
    kt_img5 = pg.transform.rotate(kt_img, 9)
    kt_img6 = pg.transform.rotate(kt_img, 12)
    kt_img7 = pg.transform.rotate(kt_img, 9)
    kt_img8 = pg.transform.rotate(kt_img, 6)
    kt_img9 = pg.transform.rotate(kt_img, 3)
    kt_imgs = [kt_img, kt_img3, kt_img4, kt_img5, kt_img6,kt_img7, kt_img8, kt_img9]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200
        screen.blit(bg_img,[-x, 0])

        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
  
        screen.blit(kt_imgs[tmr%7],[300,200])

        pg.display.update()
        tmr += 1        
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()