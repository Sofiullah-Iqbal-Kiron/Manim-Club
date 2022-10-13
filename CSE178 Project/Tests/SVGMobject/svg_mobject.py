from manim import *


class TheClass(Scene):
    def construct(self):
        myClock = SVGMobject("clock.svg").shift(3 * RIGHT)
        # myDuke = SVGMobject("duke.svg").shift(2 * LEFT)
        self.play(myClock.animate(run_time=2).shift(3 * LEFT).scale(1.6).set_fill(GRAY_C))
