from vex import *

def draw_rect(xCoordinate, yCoordinate, width, height, borderRadius):
    """Draws a rectangle of the specified color at the specified location."""
    brain.screen.draw_rectangle(xCoordinate + borderRadius, yCoordinate + borderRadius,
                                width - (borderRadius * 2), height - (borderRadius * 2))
    brain.screen.draw_circle(xCoordinate - borderRadius, yCoordinate + borderRadius,
                             borderRadius)
    brain.screen.draw_circle(xCoordinate - borderRadius + width,
                             yCoordinate + borderRadius, borderRadius)
    brain.screen.draw_circle(xCoordinate - borderRadius + width,
                             yCoordinate - borderRadius + height, borderRadius)
    brain.screen.draw_circle(xCoordinate - borderRadius,
                             yCoordinate + borderRadius + height, borderRadius)
    brain.screen.draw_rectangle(xCoordinate + borderRadius, yCoordinate,
                                width - (borderRadius * 2), borderRadius)
    brain.screen.draw_rectangle(xCoordinate + borderRadius, yCoordinate,
                                width - (borderRadius * 2), borderRadius)

class PushButton:
    def __init__(self, x_coordinate, y_coordinate, width, height, bg="#EEEEEE", background="", text="", drop_shadow=False,
                 drop_shadow_x=-3, drop_shadow_y=3, drop_shadow_blur=3, drop_shadow_color="#d6d6d6", border_radius=0):
        self.dropShadowX = drop_shadow_x
        self.dropShadowY = drop_shadow_y
        self.dropShadowBlur = drop_shadow_blur
        self.dropShadowColor = drop_shadow_color
        self.background = bg
        if not background == "":
            self.background = background
        self.text = text
        self.dropShadow = drop_shadow
        self.xCoordinate = x_coordinate
        self.yCoordinate = y_coordinate
        self.width = width
        self.height = height
        self.borderRadius = border_radius
        brain.screen.set_fill_color(self, self.background)
        brain.screen.set_pen_color(self, Color.TRANSPARENT)

        if not self.dropShadow:
            draw_rect(self.xCoordinate + self.dropShadowX, self.yCoordinate + self.dropShadowY, self.width, self.height, self.borderRadius)

        if not self.borderRadius == 0:
            draw_rect(self.xCoordinate, self.yCoordinate, self.width, self.height, self.borderRadius)

        else:
            brain.screen.set_fill_color(self, self.background)
            brain.screen.draw_rectangle(self.xCoordinate, self.yCoordinate, self.width, self.height)

