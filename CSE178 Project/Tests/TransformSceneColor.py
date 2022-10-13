from manim import *


class TheClass(Scene):
    def construct(self):
        f1 = Text("F")
        f2 = Text("F").scale(2)
        f3 = Text("F").scale(0.5)
        f4 = Text("F").scale(-1)
        circle = Circle(radius=2)

        vgroup = VGroup(f1, f2, f3, f4).arrange(6 * RIGHT)
        self.play(ReplacementTransform(vgroup, circle),run_time=5)
