from manim import *
from manim_voiceover import *
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.azure import AzureService

basic = r'''
Goals of operating system:
\begin{enumerate}
    \item Execute user programs and make solving user problems easier.
    \item Make the computer system convenient to use.
    \item Use the computer system in an efficient manner.
\end{enumerate}
'''
basic_speech = "Let's talk about goals of operating system." \
               "First of all, it is mostly used to execute user programs and make solving user problems easier." \
               "Make the computer system convenient to use." \
               "And use the computer system in an efficient manner."


class Main(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())

        # Background.
        background = Rectangle(height=config.frame_height, width=config.frame_width). \
            set_color([TEAL, BLUE, GREEN]). \
            set_opacity(0.7)
        self.play(FadeIn(background), run_time=1)
        self.bring_to_back(background)

        # Default start wait.
        self.wait(0.5)

        with self.voiceover(basic_speech) as tracker:
            self.play(
                Write(Tex(basic).scale(0.7)),
                run_time=tracker.duration)

        # Default ending wait.
        self.wait(1)


class GrantChart(VoiceoverScene):
    def construct(self):
        self.wait(0.5)
        self.set_speech_service(AzureService(voice="en-GB-OliverNeural", style="newscast-casual"))

        rectangle_def = Rectangle(width=1, height=0.5).set_color(WHITE).set_fill(color=BLUE_E, opacity=0.6)
        rectangles = [rectangle_def.copy() for i in range(5)]
        for i in range(1, len(rectangles), 1):
            rectangles[i].next_to(rectangles[i - 1], RIGHT, buff=0)

        for i in range(0, len(rectangles), 1):
            index = Tex(f"$P_{i + 1}$", color=WHITE).scale(0.6).move_to(rectangles[i].get_center())
            rectangles[i].add(index)

        g1 = Group(*rectangles).move_to(ORIGIN)

        for i in range(len(rectangles)):
            with self.voiceover(text=f"Process {i + 1}.") as tracker:
                self.play(GrowFromCenter(rectangles[i], point_color=WHITE), run_time=tracker.duration)

        self.wait(2)


class ScheduleTable(Scene):
    def construct(self):
        Text.set_default(color=DARK_BLUE)
        Tex.set_default(color=BLACK)
        self.camera.background_color = WHITE
        self.wait(0.5)

        t0 = MobjectTable(
            table=
            [
                [Tex(r"$0$"), Tex(r"$8$")],
                [Tex(r"$1$"), Tex(r"$4$")],
                [Tex(r"$2$"), Tex(r"$9$")],
                [Tex(r"$3$"), Tex(r"$5$")],
            ],
            row_labels=[Tex(r"$P_1$"), Tex(r"$P_2$"), Tex(r"$P_3$"), Tex(r"$P_4$")],
            col_labels=[Text("Arrival Time"), Text("Burst Time")],
            top_left_entry=Text("Process ID"),

            include_outer_lines=True,
            line_config={"color": BLACK},
        ).scale(0.7)

        self.play(Create(t0), run_time=7)
        self.play(Indicate(t0))

        self.wait(2)
