from vex import *

class V5GLError(Exception):
    def __init__(self, message="Sorry, V5GL encountered an internal error."):
        self.message = message
        super().__init__(self.message)


class V5Application:
    # bg and background are different names for the same thing, both will produce desired result. Refresh rate determines
    # the screen refresh rate in hertz
    def __init__(self, bg="white", background="", refresh_rate=60):
        self.LoopSpeed = None
        self.background = bg
        if not background == "":
            self.background = background
        self.refreshRate = refresh_rate

        brain.screen.clear_screen()
        brain.screen.set_fill_color(self, self.background)
        brain.screen.set_pen_color(self, Color.TRANSPARENT)
        brain.screen.draw_rectangle(0, 0, 479, 239)

    def Run(self):
        brain.screen.pressed()


