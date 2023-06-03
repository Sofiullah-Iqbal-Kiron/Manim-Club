from manim import *


class Main(Scene):
    def construct(self):
        self.wait()

        a = RegularPolygon(n=10, color=BLUE_E)
        b = RegularPolygon(n=11, color=YELLOW)
        c = RegularPolygon(n=12, color=WHITE)
        d = RegularPolygon(n=30, color=GREEN_C).next_to(c, RIGHT)

        g1 = Group(a, b, c).arrange(RIGHT, 0.75)
        self.play(Create(a))
        self.play(Transform(a.copy(), b))
        self.play(Transform(b.copy(), c))
        self.clear()
        self.play(Create(d))

        self.wait()
