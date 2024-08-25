import pygame as pg
import numpy as np
import math

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (225,225,0)
BLUE = (0,0,225)
BLACK = (0, 0, 0)

angle = 0

WIDTH, HEIGHT = 800, 600
pg.display.set_caption("3D cube renderer without OPENGL")
screen = pg.display.set_mode((WIDTH, HEIGHT))

scale = 100
circlePos = [WIDTH / 2, HEIGHT / 2]

points = [
    np.matrix([-1, -1, 1]),
    np.matrix([1, -1, 1]),
    np.matrix([1, 1, 1]),
    np.matrix([-1, 1, 1]),
    np.matrix([-1, -1, -1]),
    np.matrix([1, -1, -1]),
    np.matrix([1, 1, -1]),
    np.matrix([-1, 1, -1])
]

projectionMatrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

projected_points = [[0, 0] for _ in range(len(points))]


def connect_points_black(i, j, points):
    pg.draw.line(screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))
def connect_points_green(i, j, points):
    pg.draw.line(screen, GREEN, (points[i][0], points[i][1]), (points[j][0], points[j][1]))
def connect_points_blue(i, j, points):
    pg.draw.line(screen, BLUE, (points[i][0], points[i][1]), (points[j][0], points[j][1]))
clock = pg.time.Clock()

while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)],
    ])

    rotation_y = np.matrix([
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)],
    ])

    rotation_z = np.matrix([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1],
    ])

    angle += 0.01
    screen.fill(BLACK)

    for i, point in enumerate(points):
        rotated2d = np.dot(rotation_z, point.reshape(3, 1))
        rotated2d = np.dot(rotation_y, rotated2d)

        projected2d = np.dot(projectionMatrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circlePos[0]
        y = int(projected2d[1][0] * scale) + circlePos[1]
        projected_points[i] = [x, y]
        pg.draw.circle(screen, RED, (x, y), 5)

    # Connect the points after projection and rotation
    connect_points_black(0, 1, projected_points)
    connect_points_black(1, 2, projected_points)
    connect_points_black(2, 3, projected_points)
    connect_points_black(3, 0, projected_points)

    connect_points_black(4, 5, projected_points)
    connect_points_black(5, 6, projected_points)
    connect_points_black(6, 7, projected_points)
    connect_points_black(7, 4, projected_points)

    connect_points_black(0, 4, projected_points)
    connect_points_black(1, 5, projected_points)
    connect_points_black(2, 6, projected_points)
    connect_points_black(3, 7, projected_points)

    # Additional Connects test
    connect_points_blue(0,2,projected_points)
    connect_points_blue(1,3,projected_points)
    connect_points_blue(4, 6, projected_points)
    connect_points_blue(5, 7, projected_points)
    connect_points_blue(0, 5, projected_points)
    connect_points_blue(1, 4, projected_points)
    connect_points_blue(1, 6, projected_points)
    connect_points_blue(2, 5, projected_points)
    connect_points_blue(3, 6, projected_points)
    connect_points_blue(2, 7, projected_points)
    connect_points_blue(3, 4, projected_points)
    connect_points_blue(7, 0, projected_points)




    # connect_points_green(1,7,projected_points)
    # connect_points_green(2,4,projected_points)
    # connect_points_green(3,5,projected_points)
    #connect_points_green(4,1,projected_points)





    pg.display.update()