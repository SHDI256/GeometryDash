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
        self.end_y = self.field.get_now_y(self.rect.x + self.radius) + 1
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

    def crash(self):
        self.image = pygame.transform.scale(self.image, (0, 0))