from manim import *


class Main(Scene):
    def construct(self):
        actors=['todo: svg here']

        cases_text = [
            'Add\na task',
            'Remove\na task',
            'Mark a task\nas done',
            'Mark a task\nas important',
            'Remove all tasks\nin one go',
            'Save tasks',
            'Post tasks\nto sever database',
        ]
        cases_Paragraph = [Paragraph(case, alignment='center') for case in cases_text]

        case_group = Group(*cases_Paragraph).arrange(DOWN, 0.5).scale(0.6).shift(LEFT)
        system_heading=Text("Your Daily Tasks", weight=BOLD)
        system_rectangle=Rectangle()

        add_a_task=Text('Add a Task.')
        case_surround_oval = Ellipse(width=4, height=2.5, stroke_width=2, stroke_color=BLUE_A).surround(add_a_task)
        self.play(Create(case_surround_oval), Write(add_a_task))

        # for c in cases_in_paragraph:
        #     self.play(Write(c))

        # self.play(g1.animate.arrange(DOWN, buff=1))
