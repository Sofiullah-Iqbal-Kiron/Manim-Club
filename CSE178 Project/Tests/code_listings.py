# Code() class/MObject

from manim import *


class CodeListing(Scene):
    def construct(self):
        code = Code("my_arrow.py", tab_width=4, line_spacing=0.5, font_size=19, font="Consolas", indentation_chars='\t',
                    background="window", generate_html_file=True)
        c = Circle()
        self.play(Create(code), run_time=10)
        self.wait(1)
        self.play(FadeOut(code), run_time=2)
