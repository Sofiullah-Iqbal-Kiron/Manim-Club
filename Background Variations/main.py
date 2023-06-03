import math

from manim import *


class Main(Scene):
    def construct(self):
        # Background.
        # background = ImageMobject("sea.jpg")
        background = Rectangle(height=config.frame_height, width=config.frame_width). \
            set_color([TEAL, BLUE, GREEN]). \
            set_opacity(0.7)
        self.play(FadeIn(background), run_time=1)
        self.bring_to_back(background)

        # Default starting wait.
        self.wait(0.5)

        name = Text("Hello Kiron.", color=BLUE)
        self.play(Write(name), run_time=3)
        self.play(Indicate(name))

        # Default ending wait.
        self.wait()
