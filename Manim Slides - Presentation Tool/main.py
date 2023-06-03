from manim import *
from manim_slides import Slide


class Main(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        self.pause()

        self.start_loop()
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_runc=linear)
        self.end_loop()

        self.play(dot.animate.move_to(ORIGIN))
        self.pause()
