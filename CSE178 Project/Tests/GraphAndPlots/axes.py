from manim import *


class TheClass(Scene):
    def construct(self):
        self.camera_class.background_color = RED
        self.add(NumberPlane())
        axes = Axes(axis_config={"include_numbers": True, "include_tip": False})
        graph = axes.plot(lambda x: 2 * x + 1, x_range=[-4, 4, 1], use_vectorized=True)
        c = Circle()
        self.add(axes, c, graph)
        color
