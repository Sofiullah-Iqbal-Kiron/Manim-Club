from manim import *
from manim_voiceover import *


class Main(VoiceoverScene):
    def construct(self):
        texts = [
            Text("Hello, my name is Sofiullah Iqbal Kiron"),
            Text("I am the Full Stack Web Programmer."),
        ]
        g1 = Group(*texts).arrange(DOWN, 1)
        self.add(g1)
