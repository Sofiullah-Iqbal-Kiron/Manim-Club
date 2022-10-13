from manim import *


class theClass(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.next_to(circle, RIGHT, buff=3)

        self.play(Create(circle), Create(square), run_time=4)
