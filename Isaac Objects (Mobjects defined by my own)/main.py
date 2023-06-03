# Implement Animation for this mobject.
from abc import ABC

from manim import *


class IndexPositionError(Exception):
    def __str__(self):
        return "'index_pos' should be either 'UP' or 'DOWN'"


# Extend from VMobject cause no other has defined animations.
# Don't extend from Mobject directly because of Mobject is abstract.
class Array(VMobject):
    def __init__(
            self,
            entries: Mobject | str = [],
            show_index: bool = True,
            start_index: int = 0,
            index_step: int = 1,
            index_pos: np.ndarray = UP,
            index_color: color = WHITE,
            box_height: float = 1.0,
            box_width: float = 1.0,
            box_color: color = YELLOW,
            entry_color: color = PURE_BLUE,
            stroke_width: float = 1.5
    ):
        self.length = len(entries)
        self.entries = entries
        super().__init__()

        if index_pos is not UP and index_pos is not DOWN:
            raise IndexPositionError()

        # boxes
        self.base_box = Rectangle(height=box_height, width=box_width, stroke_width=stroke_width, stroke_color=box_color)
        self.boxes = Group(*[self.base_box.copy() for i in range(0, self.length)]).arrange(buff=0)

        # indices
        if show_index:
            self.indices = []
            count = 0
            while count < self.length:
                self.indices.append(Tex(f"${start_index}$", color=index_color))
                start_index += index_step
                count += 1
            for i in range(0, self.length, 1):
                self.indices[i].scale(box_height * 0.7)
                self.indices[i].next_to(self.boxes[i], index_pos, buff=MED_SMALL_BUFF)

        # entries, must be a list of Mobjects or str.
        for i in range(0, self.length, 1):
            if type(self.entries[i]) is str:
                self.entries[i] = Text(f"{self.entries[i]}")
            self.entries[i]. \
                set_color(entry_color). \
                scale_to_fit_height(box_height * 0.70). \
                scale_to_fit_width(box_width * 0.82). \
                move_to(self.boxes[i])

        # adding all submobjects
        if show_index:
            self.add(*self.indices)
        self.add(*self.boxes)
        self.add(*self.entries)
        self.move_to(ORIGIN)


class Pointer(VMobject):
    def __init__(self):
        super().__init__()
        pass


class Main(Scene):
    def construct(self):
        a = Array(["Kiron", "Nirob", "Israt"], start_index=2, index_pos=RIGHT)
        self.play(Create(a, run_time=8))
