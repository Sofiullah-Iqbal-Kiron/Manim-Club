from manim import *


class Main(Scene):
    def construct(self):
        self.wait(1)
        code = Code(file_name="ReactHookUseState.js",
                    tab_width=3, language="JavaScript")
        self.play(Write(code), run_time=7)
        self.wait(3)
