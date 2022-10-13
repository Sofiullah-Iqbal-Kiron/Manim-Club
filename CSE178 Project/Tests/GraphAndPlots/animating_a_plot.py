from manim import *


class TheClass(Scene):
    def construct(self):
        axes = Axes(x_range=[-5, 5, 1], y_range=[-4, 5, 1], axis_config={"include_tip": True})
        graph = axes.plot(lambda x: x ** 2, x_range=[0, 2, 1], color=BLUE)
        graph2 = axes.plot(lambda x: 2 * x - 1, x_range=[0, 3, 1], color=BLUE)
        self.play(Write(axes), run_time=2)
        self.play(Write(graph), run_time=2)
        self.play(Transform(graph, graph2))
        self.wait(1)
