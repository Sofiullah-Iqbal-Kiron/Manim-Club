
from manim import *


# All manim class must inherit Scence, cause all the things will be a scence.
class squareToCircle(Scene):
    def construct(self):
        s = Square().rotate(PI/4)
        c = Circle()

        # Playing animation.
        self.play(Create(s))
        self.play(Transform(s, c), run_time=5)
        self.play(FadeOut(s))
