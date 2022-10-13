from manim import *


class TheClass(Scene):
    def construct(self):
        self.add(NumberPlane())
        c = Circle()
        myName = Text("Kiron")
        self.play(c.animate(run_time=5).set_stroke(color=GREEN, width=50, opacity=1))