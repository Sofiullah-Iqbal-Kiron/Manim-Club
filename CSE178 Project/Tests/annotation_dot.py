from manim import *


class annotation_dot(Scene):
    def construct(self):
        a_dot = AnnotationDot(radius=1, stroke_width=5, stroke_color=RED, fill_color=GREEN)
        self.add(a_dot, Text(text="Kiron", fill_color=RED))
