from manim import *


class Main(Scene):
    def construct(self):
        def update_label_text(object):
            object.set(text=str(cnt))
            object.next_to(dot, UP)
            cnt += 1

        cnt = 1
        dot = Dot(ORIGIN)
        label = Text(str(dot.get_x())).next_to(dot, UP)
        label.add_updater(update_label_text)
        self.add(label)
        self.play(dot.animate.move_to(UL*3))
        self.play(dot.animate.move_to(DOWN*3))
