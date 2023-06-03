from manim import *


class Main(Scene):
    def construct(self):
        dot = Dot(radius=0.5)
        label = Text(text=dot.get_x()).next_to(dot, UP, buff=0.5)
        self.add(dot, label)
