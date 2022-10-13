from manim import *


class TheClass(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle,
                 AnimatedBoundary(circle, colors=[RED, GREEN, DARK_BROWN, BLUE], max_stroke_width=5, cycle_rate=4))
        self.wait(3)
