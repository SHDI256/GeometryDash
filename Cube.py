import pygame


class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, speed, acceleration, image, field):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.transform.scale(pygame.image.load(image), (radius * 2, radius * 2))
        self.radius = radius
        self.speed_start = speed
        self.speed = speed
        self.acceleration = acceleration
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_jump = False
        self.jump_orientation = True
        self.c = 0
        self.end_y = self.rect.y
        self.field = field

    def update(self):
        self.end_y = self.field.get_now_y(self.rect.x + self.radius * 2)
        if self.field.get_now_y(self.rect.x - self.radius) < self.field.get_now_y(self.rect.x + self.radius * 2 + self.field.speed) and \
                self.field.get_now_y(self.rect.x + self.radius) == self.field.get_now_y(self.rect.x + self.radius * 2 + self.field.speed) \
                and not self.is_jump:
            self.is_jump = True
            self.jump_orientation = False

        elif self.is_jump:
            if self.jump_orientation:
                self.rect.y -= (self.speed * (1 / 15) * self.c) + ((self.acceleration * self.c) / 2)
                self.speed -= self.acceleration
            else:
                self.rect.y += (self.speed * (1 / 15) * self.c) + ((self.acceleration * self.c) / 2)
                self.speed += self.acceleration
            self.c += 1

            if self.rect.y + self.radius * 2 >= self.end_y:
                if (self.jump_orientation and self.speed < 0) or ((not self.jump_orientation) and self.speed > 0):
                    self.rect.y = self.end_y
                    self.speed = self.speed_start
                    self.is_jump = False
                    self.jump_orientation = True
                    self.c = 0

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))

    background = pygame.image.load('background-1.jpg')
    background = pygame.transform.scale(background, (1920, 1080))
    screen.blit(background, (0, 0))

    cube = Cube(525, 698, 25, 0, 15, 250, 15, 'cube-3.png')

    clock = pygame.time.Clock()

    running = True
    is_jump = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not cube.is_jump:
                        cube.is_jump = True

        screen.blit(background, (0, 0))
        if cube.is_jump:

            cube.jump(698)

        # barrier.move(10)
        # barrier.render(screen)
        # barrier1.move(10)
        # barrier1.render(screen)
        # barrier2.move(10)
        # barrier2.render(screen)
        cube.render(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()