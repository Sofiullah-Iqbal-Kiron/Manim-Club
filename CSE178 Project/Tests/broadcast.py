from manim import *


class TheClass(Scene):
    def construct(self):
        self.add(NumberPlane())
        c = Rectangle(color=RED, height=5, width=9)
        self.play(Broadcast(c))
