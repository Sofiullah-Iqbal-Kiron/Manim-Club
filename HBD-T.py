# Heart of manim is animation.
# Add an animation to my scene by play().
# Animation: https://docs.manim.community/en/stable/tutorials/building_blocks.html#animations

from manim import *


class HBDT(Scene):
    def construct(self):
        date = Text('14 August, 2021', font='Chiller', color=BLUE_B).scale(1.3)
        bmsg = Text("🎁  Happy Birthday Too YOU  🎂", color=GREEN)
        bmsg2 = Text('@ many many happy returns of the day @',
                     font='Cabin Sketch', color=WHITE)
        name = Text('"Sadia Jahan Tisha"', font='Calibri', ).scale(2)

        date.scale_in_place(0.85)
        self.add(date.to_edge(UP))
        msggrp = VGroup(bmsg, bmsg2).arrange(direction=DOWN)

        self.play(FadeIn(date))
        self.wait(1)
        self.play(Write(bmsg), runtime=2)
        self.wait(1)
        self.play(Create(bmsg2), runtime=2)
        self.wait(2)
        self.play(FadeOut(date), ClockwiseTransform(
            msggrp, name), runtime=2)
        self.wait(0.5)
        self.clear()
        self.play(Rotate(
            Text("Sadia Jahan Tisha", color=RED), PI*80), runtime=20)
        self.wait(1)
        self.clear()

        self.camera.background_color = '#bdc3c7'
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a = Square().set_color(BLUE).shift(RIGHT)
        m2b = Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis=0)
        m2a.points = points

        self.play(Transform(m1a, m1b), Transform(m2a, m2b), run_time=2)

        self.wait(1)
        self.clear()
        self.camera.background_color = YELLOW_C
        goodbye = Text('Good Bye', color=GREEN).set_stroke(
            color=RED, width=8, opacity=1).scale(2)
        byeemoji = Text('🙂').set_color(BLACK)
        byeText = VGroup(goodbye, byeemoji).arrange(direction=DOWN)
        self.play(GrowFromCenter(byeText))
        self.wait(2)
        self.play(FadeOut(byeText))
        self.wait(0.8)
