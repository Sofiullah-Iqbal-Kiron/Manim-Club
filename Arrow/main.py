from manim import *


class Main(Scene):
    def construct(self):
        t = Text("Kiron").shift(UP * 2).shift(LEFT)
        t2 = Text("Tisha").shift(DOWN * 2).shift(RIGHT)
        a1 = Arrow(start=t.get_corner(DOWN), end=t2.get_corner(UP))
        self.play(Write(t), GrowArrow(a1), Create(t2), run_time=3)
        self.wait()
        g1 = Group(t, t2, a1)
        self.play(g1.animate.scale(1.5))
        self.wait()
        self.play(t2.animate.shift(UP * 2))
        self.play(a1.animate.put_start_and_end_on(start=t.get_corner(DOWN), end=t2.get_corner(UP)))
        self.wait()
