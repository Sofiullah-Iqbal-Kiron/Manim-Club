from manim import *
from manim_voiceover import *
from manim_voiceover.services.gtts import GTTSService

Text.set_default(color=BLACK)
Tex.set_default(color=BLACK)


class Main(VoiceoverScene):
    def construct(self):
        self.add_sound("vhs-startup-6088.mp3", gain=1.1)
        # Background.
        background = Rectangle(height=config.frame_height, width=config.frame_width). \
            set_color([TEAL, BLUE, GREEN]). \
            set_opacity(0.7)
        self.play(FadeIn(background, run_time=1.5))
        self.bring_to_back(background)

        # Default starting wait.
        self.wait(1)

        # Voiceover setting.
        self.set_speech_service(GTTSService())

        pi = Tex(r"$\pi$").scale(2.5)
        pi_text = Text("PI, which is an interesting irrational constant.").next_to(pi, DOWN, buff=0.7)
        g1 = Group(pi, pi_text).move_to(ORIGIN)

        speech_text = "Pi, an interesting irrational constant used by mathematicians, scientist, engineers " \
                      "and also by other stuffs."

        with self.voiceover(text=speech_text) as tracker:
            self.play(Create(pi))
            self.play(Write(pi_text))

        pi_value = Tex(r"\begin{center}$3.14159265358$ \dots \linebreak and million lines more\end{center}", color=WHITE).scale(2.4)

        with self.voiceover(text="It has a robust value.") as tracker:
            self.play(FadeOut(background), Transform(g1, pi_value), run_time=1.3)

        # Default ending wait.
        self.wait(2)
