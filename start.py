# Import all methods from manim library.
from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(GREEN, opacity=0.7)  # set color and transpareny
        self.play(Create(circle), run_time=3)  # show the circle on screen
