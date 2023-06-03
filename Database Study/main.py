from manim import *
from manim_voiceover import *
from manim_voiceover.services.gtts import GTTSService


class Main(VoiceoverScene):
    def construct(self):
        background = Rectangle(height=config.frame_height, width=config.frame_width). \
            set_color([TEAL, BLUE, GREEN]). \
            set_opacity(0.7)
        self.play(FadeIn(background), run_time=1)
        self.bring_to_back(background)

        # Default starting wait.
        self.wait(0.5)

        # Voiceover setting.
        self.set_speech_service(GTTSService())

        definition = Text("The select operation select tuples that\nsatisfy a given predicate.")
        sigma = Tex(r"$\sigma_p = (r)$").next_to(definition, DOWN)
        g1 = Group(definition, sigma)

        with self.voiceover(
                text="The select operation select tuples <bookmark mark='A'/>that satisfy a given predicate.") as tracker:
            self.play(Write(definition))
            self.wait_until_bookmark("A")
            self.play(Create(sigma))

        # Default ending wait.
        self.wait(1)
