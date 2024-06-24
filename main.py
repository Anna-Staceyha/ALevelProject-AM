"""
import pygame
import sys

#creating and setting caption of the screen
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Images in PyGame!")

#surface - the image i want
backgroundImage = pygame.image.load("vecteezy_beautiful-seasonal-nature-mountain-landscape-illustration_9155728-1.jpg")
backgroundImage_rect = backgroundImage.get_rect(center=(0, 0))


#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #makes screen blank
    screen.fill("white")

    screen.blit(backgroundImage, (backgroundImage_rect))
    #display the screen


    pygame.display.update()"""

import pygame

# dimensions of the game
screen_length = 1080
screen_height = 720

# sets the background colour to light grey
background_colour = (200, 200, 200)
title = "Anna's Game"

screen = pygame.display.set_mode([screen_length, screen_height])
pygame.display.set_caption(title)

# load button images
start_img = pygame.image.load('start.png').convert_alpha()
exit_img = pygame.image.load('exit.png').convert_alpha()

# loads the background image I want
path_to_image = "vecteezy_beautiful-seasonal-nature-mountain-landscape-illustration_9155728-1.jpg"

# button class

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.click_delay = 100 # Delay in milliseconds
        self.last_click = 0

    def draw(self):

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.last_click = pygame.time.get_ticks()
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))


# create button instances
start_button = Button(450, 30, start_img, 0.2)
exit_button = Button(450,25, exit_img, 0.2)

# game loop
"""run = True
while run:

    # loads the background image I want
    path_to_image = "vecteezy_beautiful-seasonal-nature-mountain-landscape-illustration_9155728-1.jpg"
    # ensures that the whole image is displayed
    length = screen_length
    height = screen_height
    left_edge = 0
    top_edge = 0

    start_button.draw()
    exit_button.draw()

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()"""

"""screen.fill(background_colour)  #
  image = pygame.transform.scale(pygame.image.load(path_to_image), [int(length), int(height)])
    screen.blit(image,[left_edge, top_edge])"""

# game loop
run = True
while run:
    try:
        # loads the background image I want
        path_to_image = "vecteezy_beautiful-seasonal-nature-mountain-landscape-illustration_9155728-1.jpg"
        # ensures that the whole image is displayed
        length = screen_length
        height = screen_height
        left_edge = 0
        top_edge = 0

        start_button.draw()
        exit_button.draw()

        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    except Exception as e:
        print("An error occurred:", e)
        pygame.quit()
