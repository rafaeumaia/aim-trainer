import random

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Aim Trainer')

target_increment = 300
target_event = pygame.USEREVENT
target_padding = 30

bg_color = (0, 25, 40)

class Target:
    max_size = 30
    growth_rate = 0.2
    color = 'red'
    second_color = 'white'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.growth_rate >= self.max_size:
            self.grow = False

        if self.grow:
            self.size += self.growth_rate
        else:
            self.size -= self.growth_rate

    def drawing(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.second_color, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.second_color, (self.x, self.y), self.size * 0.4)


def main():
    run = True
    targets = []

    pygame.time.set_timer(target_event, target_increment)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == target_event
                x = random.randint(target_padding, WIDTH - target_padding)
                y = random.randint(target_padding, HEIGHT - target_padding)
                target = Target(x, y)
                targets.append(target)

    pygame.quit()


if __name__ == '__main__':
    main()
