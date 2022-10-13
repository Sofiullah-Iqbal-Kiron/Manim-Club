from manim import *


class TheClass(Scene):
    def construct(self):
        self.add(NumberPlane())
        ellipse = Ellipse(width=5, height=2.5)
        self.add(ellipse.rotate(90 * DEGREES))
