import pygame


class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, angle, angular_speed, speed, acceleration, image):
        image = pygame.transform.scale(pygame.image.load(image), (radius * 2, radius * 2))
        self.x = x
        self.y = y
        self.origin_x = x
        self.origin_y = y
        self.radius = radius
        self.angle = angle
        self.angular_speed = angular_speed
        self.speed_start = speed
        self.speed = speed
        self.acceleration = acceleration
        self.image = image
        self.rotated_image = image
        self.is_jump = False
        self.c = 0

    def jump(self, end_y):
        if self.origin_y >= end_y and self.speed < 0:
            self.angle = 0
            self.origin_y = end_y
            self.y = end_y
            self.speed = self.speed_start
            self.is_jump = False
            self.c = 0

        w, h = self.image.get_size()
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(self.angle) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        pivot = pygame.math.Vector2(w / 2, -(h / 2))
        pivot_rotate = pivot.rotate(self.angle)
        pivot_move = pivot_rotate - pivot

        origin = (self.x + (w / 2) + min_box[0] - pivot_move[0],
                  self.y + (h / 2) - max_box[1] + pivot_move[1])

        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.origin_x = origin[0]
        self.origin_y = origin[1]
        self.origin_y -= (self.speed * (1 / 15) * self.c) + ((self.acceleration * self.c) / 2)
        self.speed -= self.acceleration
        self.angle -= self.angular_speed
        self.c += 1

    # TODO
    # def is_collision(self, field):
    #     if self.is_jump:
    #         x1 = self.origin_x + self.radius * 2
    #         y1 = self.origin_y + self.radius * 2
    #         y2 = self.origin_y
    #     else:
    #         x1 = self.x + self.radius * 2
    #         y1 = self.y + self.radius * 2
    #         y2 = self.y
    #     for i, barriers in enumerate(field.field):
    #         for j, barrier in enumerate(barriers):
    #             if barrier == 0:
    #                 if ():
    #                     return True
    #             elif barrier == 1:
    #                 if ():
    #                     return True

    def render(self, screen):
        if self.is_jump:
            screen.blit(self.rotated_image, (self.origin_x, self.origin_y))
        else:
            screen.blit(self.image, (self.x + self.radius, self.y + self.radius))


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