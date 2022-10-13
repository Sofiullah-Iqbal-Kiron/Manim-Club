from manim import *


class HBDN(Scene):
    def construct(self):
        self.camera.background_color = '#b6f0d8'
        date = Text('2 January, 2022', font='Ebrima',
                    color=BLACK).scale(1)
        bmsg1 = Text("🎁  Happy Birthday Too YOU  🎂", color=GREEN)
        bmsg2 = Text('# many many happy returns of the day #',
                     font='HARLOWSI', color=RED)
        name = Text('[- Nasir Ahmed Sahir -]', font='Calibri', ).scale(1.6)

        self.add(date.to_edge(UP))
        msggrp = VGroup(bmsg1, bmsg2).arrange(direction=DOWN)

        self.play(FadeIn(date))
        self.wait(1)
        self.play(Write(bmsg1), runtime=2)
        self.wait(1)
        self.play(AddTextLetterByLetter(bmsg2), Unwrite(bmsg1), runtime=3)
        self.wait(2)
        self.camera.background_color = BLACK
        self.play(FadeOut(date), ClockwiseTransform(
            msggrp, name), runtime=2)
        self.play(ApplyWave(name, direction=RIGHT,
                  amplitude=0.5, time_width=1))
        self.wait(0.5)
        self.clear()

        nimg = ImageMobject('image.jpg').scale(0.6)
        self.play(FadeIn(nimg), run_time=3)
        self.play(FadeOut(nimg), run_time=1)
        self.wait(1)
        self.clear()

        self.camera.background_color = YELLOW_E
        lasttext = Text('Wish you a better life...', color=GREEN, weight=MEDIUM, font_size=65).set_stroke(
            color=WHITE, width=1, opacity=0.8).scale(1.2)

        happyemoji = Text('🙂').set_color(GRAY_BROWN).scale(1.7)
        lastmsg = VGroup(lasttext, happyemoji).arrange(direction=DOWN)
        self.play(DrawBorderThenFill(lastmsg))
        self.wait(2)
        self.play(FadeOut(lastmsg))
        self.wait(0.8)
