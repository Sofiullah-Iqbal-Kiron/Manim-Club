# Happy New Year Tisha.

from manim import *


class HNYT(Scene):
    def construct(self):
        # Objects.
        self.camera.background_color = "#c5d9ca"
        wish = Text("{- Happy New Year-2022 -}",
                    font="Consolas", weight=BOLD, color=BLACK)
        wish.set_stroke(color=GREEN, width=1.8, opacity=1, background=False)

        wish2 = Text("Wishing you a better year for the sake of Allah 💚", gradient=(GREEN, RED), color=GREEN, font="Ubuntu Mono").next_to(
            wish, DOWN).scale(0.7)
        g1 = Group(wish, wish2)

        wishTopre = Text("to ->", color=BLACK).scale(0.5)
        wishTo = Text("Sadia Jahan Tisha 🙂",
                      font='Letter Gothic Std', color=WHITE, weight="SEMIBOLD").scale(1.4)
        wishTopre.next_to(wishTo, LEFT)
        g2 = Group(wishTopre, wishTo)

        # Animations.
        self.play(AddTextLetterByLetter(wish), run_time=5)
        self.play(DrawBorderThenFill(wish2), run_time=5)
        self.wait(1)
        self.camera.background_color = "#8c7573"
        self.play(ClockwiseTransform(g1, g2), run_time=2)
        self.wait(3)
