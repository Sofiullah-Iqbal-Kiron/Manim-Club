# .animate is a property method of Mobject to animate the changes we made on it, then use Scene.play() to play the
# animation on the screen.

from manim import *


class demoAnimate(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(ReplacementTransform(square, circle))
        self.play(circle.animate.set_fill(PINK, opacity=0.5), run_time=2)


class demoAnimate2(Scene):
    def construct(self):
        c = Circle()
        s = Square().next_to(c, RIGHT)
        g = Group(c, s)
        g.move_to(ORIGIN)
        g.center()
        self.wait(1)
        x = 10
        while x > 0:
            self.play(g.animate.shift(3 * RIGHT))
            self.play(g.animate.shift(3 * UP))
            self.play(g.animate.move_to(ORIGIN))
            x -= 1
