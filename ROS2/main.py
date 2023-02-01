from manim import *
from manim_voiceover import VoiceoverScene

# Use googles Text to Speech API service, clear internet connection is required.
from manim_voiceover.services.gtts import GTTSService


class Main(VoiceoverScene):
    def construct(self):
        name = Text(text="Md. Kazi Iqbal Hossen", font_size=40)
        roll = Text(text="18ICTCSE065", font_size=40).next_to(name, DOWN)
        caption = Text(text="Assignment on ROS2", font_size=40).next_to(roll, DOWN)
        self.play(Write(name), run_time=1.5)
        self.play(AddTextLetterByLetter(roll), run_time=1.5)
        self.play(Create(caption), run_time=1.5)
        g1 = Group(name, roll, caption)
        self.play(Circumscribe(g1))
        self.wait(1)
