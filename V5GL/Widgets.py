from vex import *

class PushButton:
    def __init__(self, x_coordinate, y_coordinate, width, height, bg="grey", background="", text="", drop_shadow=False,
                 border_radius=0):
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

        if not self.borderRadius == 0:
            brain.screen.draw_rectangle(self.xCoordinate + self.borderRadius, self.yCoordinate + self.borderRadius, 
                                        self.width - (self.borderRadius * 2), self.height - (self.borderRadius * 2))
            brain.screen.draw_circle(self.xCoordinate - self.borderRadius, self.yCoordinate + self.borderRadius,
                                     self.borderRadius)
            brain.screen.draw_circle(self.xCoordinate - self.borderRadius + self.width,
                                     self.yCoordinate + self.borderRadius, self.borderRadius)
            brain.screen.draw_circle(self.xCoordinate - self.borderRadius + self.width,
                                     self.yCoordinate - self.borderRadius + self.height, self.borderRadius)
            brain.screen.draw_circle(self.xCoordinate - self.borderRadius,
                                     self.yCoordinate + self.borderRadius + self.height, self.borderRadius)
            brain.screen.draw_rectangle(self.xCoordinate + self.borderRadius, self.yCoordinate,
                                        self.width - (self.borderRadius * 2), self.borderRadius)
            brain.screen.draw_rectangle(self.xCoordinate + self.borderRadius, self.yCoordinate,
                                        self.width - (self.borderRadius * 2), self.borderRadius)