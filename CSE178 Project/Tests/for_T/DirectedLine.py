from manim import *


class DirectedLine(Scene):
    def construct(self):
        text = Tex("\\justify{A directed line is a straight line with number units of positive, zero and negative.}")
        text.shift(UP)
        text
        directedLine = NumberLine(x_range=[-6, 6, 1], unit_size=1, include_tip=True, include_numbers=True).shift(DOWN)
        self.play(Write(text))
        self.play(Create(directedLine))
        self.wait(2)
