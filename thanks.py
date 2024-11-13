import time
import gc
import board
import displayio
import random
from adafruit_st7789 import ST7789
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.polygon import Polygon
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line



# Colors
BACKGROUND = 0XFFFFFF



displayio.release_displays()

spi = board.SPI()
tft_cs = board.D2
tft_dc = board.D3

dbus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(dbus, rotation=270, width=240, height=135, rowstart=40, colstart=53)


# Make the display context
main_group = displayio.Group()

# Make a background color fill
color_bitmap = displayio.Bitmap(display.width, display.height, 3)
color_palette = displayio.Palette(5)
color_palette[0] = BACKGROUND
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)
display.root_group = main_group

feather1 = RoundRect(70, 50, 101, 60, 30, fill = 0XFF0000, outline = 0X000000)
main_group.append(feather1)

feather2 = RoundRect(75, 45, 90, 60, 30, fill = 0XFFA500, outline = 0X000000)
main_group.append(feather2)

feather3 = RoundRect(80, 40, 80, 60, 30, fill = 0XFFFF00, outline = 0X000000)
main_group.append(feather3)

leg1 = Rect(100, 100, 10, 100, fill = 0XFFA500, outline = 0X000000)
main_group.append(leg1)

leg2 = Rect(130, 100, 10, 100, fill = 0XFFA500, outline = 0X000000)
main_group.append(leg2)

body = Circle(120, 87, 25, fill = 0X964B00, outline = 0X000000)
main_group.append(body)

head = Circle(120, 67, 20, fill = 0X964B00, outline = 0X000000)
main_group.append(head)

eye1 = Circle(130, 57, 3, fill = 0X000000, outline = 0X000000)
main_group.append(eye1)

eye2 = Circle(110, 57, 3, fill = 0X000000, outline = 0X000000)
main_group.append(eye2)

gobbler = RoundRect(120, 77, 10, 20, 5, fill = 0XFF0000, outline = 0X000000)
main_group.append(gobbler)

beak = Triangle(110, 67, 130, 67, 120, 87, fill = 0XFFA500, outline = 0X000000)
main_group.append(beak)

direction_x = 1
velocity_x = 1
direction_y = 1
velocity_y = 1
direction_z = 1
velocity_z = 1
direction_o = 1
velocity_o = 1
radius_r = 2

while True:
    if body.x >= 1:
        direction_x *= -1
    body.x += (velocity_x * direction_x)
    if feather1.x >= 1:
        direction_y *= -1
    feather1.x += (velocity_y * direction_y)
    if feather2.x >= 1:
        direction_z *= -1
    feather2.x += (velocity_z * direction_z)
    if feather3.x >= 1:
        direction_o *= -1
    feather3.x += (velocity_o * direction_o)
    if eye1.r >= 1:
        eye1.r += radius_r
    time.sleep(0.2)
    
