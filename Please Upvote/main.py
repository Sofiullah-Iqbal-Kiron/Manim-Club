from manim import *
from manim_voiceover import *
from manim_voiceover.services.gtts import GTTSService


class Main(VoiceoverScene):
    def construct(self):
        self.camera.background_color = WHITE
        # self.wait(0.5)
        self.set_speech_service(GTTSService())

        please_upvote = \
            Text("Please Upvote!", color=DARK_BLUE, font="Times New Roman", weight=SEMIBOLD). \
                scale(1.3). \
                shift(UP)
        # with self.voiceover(text="Please Upvote Dear Friend!") as tracker:
        #     self.play(Write(please_upvote), run_time=tracker.duration)

        # self.wait(1)

        smiley_icon = SVGMobject("smiley-icon.svg").scale(1.3).next_to(please_upvote, DOWN * 2)
        # with self.voiceover(text="Thank You.") as tracker:
        #     self.play(Create(smiley_icon), run_time=tracker.duration * 1.8)

        # self.wait(1)
        self.add(please_upvote, smiley_icon)
