# ThreeDScene.move_camera() is better than ThreeDScene.begin_ambient_camera_rotation().

from manim import *

thirtyDegree: float = PI / 6
sixtyDegree: float = PI / 3
seventyDegree: float = PI / 2.2
nintyDegree: float = PI / 2


class TheClass(ThreeDScene):
    def construct(self):
        self.camera.background_color = GREEN_A
        number_plane = NumberPlane()
        threeDaxes = ThreeDAxes()
        c = Circle().set_z(-2, 2 * UP)
        self.set_camera_orientation(phi=PI / 3, theta=2 * thirtyDegree, focal_distance=10)
        self.add(number_plane, c, threeDaxes)


class TheClass2(ThreeDScene):
    def construct(self):
        octahedron = Octahedron(edge_length=3)
        octahedron.graph[0].set_color(RED)
        octahedron.faces[2].set_color(YELLOW)
        # self.add(NumberPlane(x_range=[-7, 9, 1], y_range=[-8, 8, 1]))
        # self.set_camera_orientation(phi=70 * DEGREES, theta=60 * DEGREES)
        self.set_camera_orientation(focal_distance=10)
        cylinder = Cylinder(radius=3, height=4, direction=Y_AXIS, show_ends=False, checkerboard_colors=[BLUE_D, BLUE_A])
        self.add(ThreeDAxes(), cylinder.shift(LEFT), octahedron.shift(6 * RIGHT))
        self.wait()
        # for i in range(1, 10, 1):
        #     self.begin_ambient_camera_rotation(rate=-10, about="theta")
        self.move_camera(phi=70 * DEGREES, run_time=3)
        self.move_camera(theta=60 * DEGREES, run_time=3)
        self.move_camera(focal_distance=30)
        self.move_camera(frame_center=2 * RIGHT)
        self.move_camera(theta=300 * DEGREES, run_time=3)
        self.move_camera(frame_center=1 * RIGHT)
        self.move_camera(zoom=1.5)
        self.wait()
        self.move_camera(zoom=0.50)
        self.wait()
