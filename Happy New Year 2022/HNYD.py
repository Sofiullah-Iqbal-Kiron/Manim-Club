# Happy New Year to Dept.

from manim import *


class HNYD(Scene):
    def construct(self):
        # Objects.
        self.camera.background_color = "#c5d9ca"
        wish = Text('System.out.println("Happy New Year-2022");',
                    font='Lucida Sans Typewriter', weight=BOLD, color=BLACK).scale(0.8)
        wish.set_stroke(color=GREEN, width=1.8, opacity=1, background=False)

        wish2 = Text("Wishing you all for a better year..☺", gradient=(GREEN, BLUE), color=GREEN, font="Ubuntu Mono").next_to(
            wish, DOWN).scale(0.7)
        g1 = Group(wish, wish2)

        wishTopre = Text("void greet()", color=BLACK).scale(0.5)
        wishTo = Text("Dept. of CSE (EX. SHIICT)",
                      font='Letter Gothic Std', color=WHITE, weight="SEMIBOLD").scale(1)
        wishTopre.next_to(wishTo, LEFT)
        g2 = Group(wishTopre, wishTo)

        # Animations.
        self.play(AddTextLetterByLetter(wish), run_time=5)
        self.play(DrawBorderThenFill(wish2), run_time=5)
        self.wait(1)
        self.camera.background_color = "#8c7573"
        self.play(ClockwiseTransform(g1, g2), run_time=2)
        self.wait(3)
