from manim import *
from components import Usecase


class Main(Scene):
    def construct(self):
        actors = ['todo: svg here']

        cases_text = [
            'Add a task',
            'Remove a task',
            'Mark a task\nas done',
            'Mark a task\nas important',
            'Remove all tasks\nin one go',
            'Save tasks',
            'Post tasks\nto sever database',
        ]

        cases = [Usecase(case, 0.5) for case in cases_text]
        cases = Group(*cases).arrange(DOWN, 0.3).scale(0.6).shift(LEFT*2).shift(DOWN*0.5)

        system_heading=Text("Your Daily Tasks", weight=BOLD, font_size=24).next_to(cases,UP*1.5)
        system=Group(cases, system_heading)
        system_rectangle=Rectangle(height=system.height+2, width=system.width+0.5).surround(system)
        self.add(system, system_rectangle)