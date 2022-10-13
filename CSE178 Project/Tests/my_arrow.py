from manim import *

import numpy as np


class myArrow(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        arrow = Arrow(start=np.array((-1.0, 0.0, 0.0)),
                      end=3 * RIGHT, color=BLACK, stroke_width=10)
        self.play(arrow.animate(start=np.array((-1.0, 0.0, -20.0))), run_time=5)
        self.play(arrow.animate(color=RED), run_time=3)
