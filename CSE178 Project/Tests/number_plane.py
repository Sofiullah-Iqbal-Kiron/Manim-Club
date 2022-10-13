# Creates a cartesian plane with background lines.
# This NumberPlane can be used for coordinate lookup when animating with manim.
# Or simply, this is a grid.
# In manims basic coordinate has x(-7.1, 7.1), y(-4, 4)

from manim import *


class TheClass(Scene):
    def construct(self):
        axis_config_for_my_grid = {"stroke_width": 10,
                                   "include_ticks": True,
                                   "include_tip": True,
                                   "line_to_number_buff": SMALL_BUFF,
                                   "label_direction": DR,
                                   "font_size": 15, }
        grid = NumberPlane(x_range=(-4, 10, 1), axis_config=axis_config_for_my_grid).shift(ORIGIN)
        self.play(Create(grid, run_time=5, lag_ratio=0.1))
        c = Circle()
        self.play(Create(c))
        self.play(c.animate.shift(UP))
        self.play(c.animate.shift(RIGHT))
        self.play(c.animate.shift(UR))


class TheClass2(Scene):
    def construct(self):
        pass
