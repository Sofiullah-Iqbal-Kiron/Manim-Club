from manim import *
from manim_voiceover.voiceover_scene import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.azure import AzureService

config.background_color = "#f0e067"
Text.set_default(color=BLACK)
Arrow.set_default(color=WHITE)
RoundedRectangle.set_default(color=DARK_BLUE)
Rectangle.set_default(color=DARK_BLUE)


class Main(Scene):
    def construct(self):
        # Default starting delay offset.
        self.wait(0.5)

        texts = [Text("Compiler"),
                 Text("Machine\nDependent\nExecutable"),
                 Text("Demo")]

        source_program = Text("Source\nProgram").shift(LEFT * 3)
        compiler = Text("Compiler").shift(RIGHT * 3)
        compiler_surround = RoundedRectangle(corner_radius=0.5, width=compiler.width + 2,
                                             height=compiler.height + 2).surround(compiler)
        source_program_to_compiler = Arrow(start=source_program.get_corner(RIGHT), end=compiler.get_corner(LEFT))

        self.play(Write(source_program),
                  Create(compiler_surround),
                  AddTextLetterByLetter(compiler),
                  GrowArrow(source_program_to_compiler),
                  run_time=2)

        g1 = Group(source_program, compiler, compiler_surround, source_program_to_compiler)

        self.play(g1.animate.shift(LEFT * 4).scale(0.5))

        texts[1].shift(RIGHT * 2).scale(0.5)
        compiler_to_machine_dependent_executable = Arrow(start=compiler.get_corner(RIGHT),
                                                         end=texts[1].get_corner(LEFT))

        user_input = Text("User Input").scale(0.5).next_to(texts[1], UP * 6)
        output = Text("Output").scale(0.5).shift(DOWN * 2).next_to(texts[1], DOWN * 6)

        self.play(Write(texts[1]),
                  DrawBorderThenFill(compiler_to_machine_dependent_executable))
        self.play(AddTextLetterByLetter(user_input))
        self.play(GrowArrow(Arrow(start=user_input.get_corner(DOWN), end=texts[1].get_corner(UP))),
                  Create(Rectangle(width=texts[1].width + 2.5, height=texts[1].height + 2).surround(texts[1])))
        self.play(GrowArrow(Arrow(start=texts[1].get_corner(DOWN), end=output.get_corner(UP))),
                  Write(output))

        # Default ending delay offset.
        self.wait(2)


class TransitionDiagram(VoiceoverScene):
    def construct(self):
        # Speech service.
        self.set_speech_service(AzureService(voice="en-GB-OliverNeural", style="newscast-casual"))

        A = Text("A")
        A_state = Circle(color=WHITE).surround(A)
        AG = Group(A, A_state).shift(LEFT * 2)

        start_arrow = Arrow(start=A.get_corner(LEFT * 5), end=A.get_corner(LEFT * 0.5))

        B = Text("B")
        B_state = Circle(color=WHITE).surround(B)
        BG = Group(B, B_state).next_to(AG, RIGHT * 10)

        A_to_B = Arrow(start=A.get_corner(RIGHT), end=B.get_corner(LEFT))
        A_to_B_label = Text("a").next_to(A_to_B, UP * 0.5)

        # wait 1 second before start the video
        self.wait()

        with self.voiceover(text="Assume that we have 2 initial state.") as tracker:
            self.play(GrowFromCenter(AG), GrowFromCenter(BG), run_time=tracker.duration)

        with self.voiceover(text="And our finite state machine moves from state A to state B,") as tracker:
            self.play(GrowArrow(A_to_B), run_time=tracker.duration)

        with self.voiceover(text="on input 'a'.") as tracker:
            self.play(Write(A_to_B_label), run_time=tracker.duration)

        self.play(Circumscribe(Group(AG, BG, A_to_B, A_to_B_label)))

        # wait another 1 second after video ends
        self.wait()


class FirstSet(Scene):
    def construct(self):
        S = Text("S").shift(LEFT * 2)
        S_derivatives = Text("abc | def | ghi").next_to(S, RIGHT * 5)
        S_to_derivatives = Arrow(start=S.get_corner(RIGHT), end=S_derivatives.get_corner(LEFT))
        SG = Group(S, S_derivatives, S_to_derivatives).shift(UP)

        first_of_S = Text("FIRST(S) = {a, d, g}").next_to(SG, DOWN * 4)

        self.wait(0.5)

        self.play(Create(S), GrowArrow(S_to_derivatives), Write(S_derivatives), run_time=2)
        self.play(Transform(SG.copy(), first_of_S))

        self.wait()


class three_a_i(Scene):
    def construct(self):
        S = Text("S")
        S_p = Text("AB").next_to(S, RIGHT * 6)
        SG = Group(S, S_p, Arrow(start=S.get_corner(RIGHT), end=S_p.get_corner(LEFT))).shift(UP)
        self.add(SG)
