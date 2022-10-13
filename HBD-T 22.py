from manim import *


class MyText(Scene):
    def construct(self):
        # objects
        hbdtu = Text("Happy birthday to you...", fill_opacity=1, color=GREEN, font_size=72, font="Consolas")
        name = Text("Sadia Jahan Tisha", fill_opacity=1, color=WHITE, font_size=80,
                    font="Arial Rounded MT Bold").next_to(hbdtu, DOWN)
        g1 = Group(hbdtu, name)
        sentiEmoji = Text("🙂").scale(3)

        self.play(Write(hbdtu, run_time=4))
        self.play(AddTextLetterByLetter(name, run_time=4))

        self.clear()
        self.play(CounterclockwiseTransform(g1, sentiEmoji))
        self.wait(1)
