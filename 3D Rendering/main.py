from manim import *


class Main(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = Cylinder(radius=2, height=3)
        name = Text("Kiron").scale(2).shift(UP)
        self.set_camera_orientation(phi=75 * DEGREES, theta=20 * DEGREES)
        self.play(Create(cylinder, run_time=3))
        self.play(FadeOut(cylinder))
        self.play(DrawBorderThenFill(axes))
        self.play(Write(name))
