# Docs: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html

from manim import *


# A rectangle surrounding a Mobject.

class TheClass(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        title = Title(r'A Quote from "Sir Isaac Newton"')
        myName = Text("Kiron".upper(), font_size=55, font="Times New Roman", color=BLACK)
        boxMyName = SurroundingRectangle(myName, color=RED, corner_radius=0.5, buff=LARGE_BUFF, stroke_width=30,
                                         stroke_opacity=1, stroke_color=BLACK)
        self.play(FadeIn(boxMyName, run_time=1.6), Indicate(myName, scale_factor=3, run_time=2))
        self.wait(2)
