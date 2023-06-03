from abc import ABC
from typing import List

from manim import *

from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class Entity(Group):
    def __init__(self, entity_name: str = "Entity", attributes: List[str] = ["att_1", "att_2", "..."]):
        super().__init__()
        self.entity_name = Text(text=entity_name, weight=BOLD)
        self.attributes = attributes
        self.entity_name_bounder = Rectangle(height=self.entity_name.height + 1.2, width=self.entity_name.width + 1.2)
        self.entity_name_bounder.surround(self.entity_name)
        # self.add(self.entity_name_bounder, self.entity_name)


class Main(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())
        e = Entity("Instructor")

        # text = Text(text="instructor", weight=BOLD, color=BLACK)
        # rectangle = Rectangle(height=text.height + 1, width=text.width + 1).surround(text)
        # rectangle.set_fill(color=WHITE, opacity=1)

        with self.voiceover(text="Let's take our first entity, called instructor.") as tracker:
            self.play(GrowFromCenter(e.entity_name_bounder), run_time=tracker.duration / 2)
            self.play(Write(e.entity_name), run_time=tracker.duration / 2)
