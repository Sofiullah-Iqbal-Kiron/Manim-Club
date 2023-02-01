from manim import *


class Main(Scene):
    def construct(self):
        code = Code(file_name="ReactHookUseState.js", tab_width=3, language="JavaScript")
        self.play(Write(code))
