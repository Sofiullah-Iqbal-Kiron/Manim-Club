from manim import *

# VoiceOver imports
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.azure import AzureService


class FourierSeries(VoiceoverScene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{csquotes}")
        # self.add(NumberPlane())
        self.always_update_mobjects = True
        self.set_speech_service(AzureService(voice="en-GB-OliverNeural", style="newscast-casual"))
        # self.set_speech_service(GTTSService())

        # subscribe = Text("Subscribe", font_size=15, color=WHITE).move_to([6.5, 4.7, 0])
        # subscribe.shift(6.5 * RIGHT)
        # self.add(subscribe)

        ourBasicTrigonometricSeriesIs = Text(text="We know that the basic trigonometric series is: ", font="Arial",
                                             font_size=52, weight=SEMIBOLD, width=12, color=GREEN)
        theBasicTrigonometricEquation = MathTex(r"\frac{A_0}{2} + \sum_{n=1}^{\infty} (A_n\cos nx + B_n\sin nx)",
                                                font_size=48)
        g1 = Group(ourBasicTrigonometricSeriesIs, theBasicTrigonometricEquation).arrange(DOWN, buff=MED_LARGE_BUFF)

        with self.voiceover(text="We know that the basic trigonometric series is...") as tracker:
            self.play(AddTextLetterByLetter(ourBasicTrigonometricSeriesIs), run_time=tracker.duration / 2)

        with self.voiceover(text="the equation appearing on the screen.") as tracker:
            self.play(FadeIn(theBasicTrigonometricEquation), run_time=tracker.duration)

        self.play(g1.animate.scale(0.65).shift(2.9 * UP))
        self.wait(1)

        itWillCalled = Tex(
            r'This equation will be called \textbf{\enquote{Fourier Series}} if the terms $A_0, A_n, B_n$ could be substituted into:',
            tex_template=myTemplate, font_size=34)
        A0 = MathTex(r"A_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)\cdot dx", font_size=40)
        An = MathTex(r"A_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cdot \cos nx\cdot dx", font_size=40)
        Bn = MathTex(r"B_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cdot \sin nx\cdot dx", font_size=40)
        g2 = Group(A0, An, Bn).arrange(DOWN, buff=MED_SMALL_BUFF).move_to(0.5 * DOWN)
        whereFX = Tex(r"Where \textbf{$f(x)$} is any single-valued function defined in interval $(-\pi, \pi)$.",
                      font_size=35).next_to(g2, 1 * DOWN)
        with self.voiceover(
                text="This equation will be called \"Fourier Series\" if the terms, A nought, A N, B N could be substituted into") as tracker:
            self.play(Create(itWillCalled), run_time=tracker.duration / 1.2)

        self.play(itWillCalled.animate.scale(0.7).next_to(g2, 1.3 * UP), run_time=0.5)
        self.play(itWillCalled.animate.set_fill(RED), SpinInFromNothing(g2), point_color=RED)

        with self.voiceover(text="these equations.") as tracker:
            self.play(Indicate(g2), run_time=tracker.duration)

        with self.voiceover(
                text="Where F of x is any single valued function defined in the exclusive interval from minus pai to pai.") as tracker:
            self.play(Write(whereFX), run_time=tracker.duration / 1.8)

        self.play(whereFX.animate(run_time=1.2).shift(0.5 * DOWN).scale(1.15))

        with self.voiceover(text="Thank you for watching.") as tracker:
            self.play(Circumscribe(whereFX), run_time=tracker.duration * 1.2)
        self.wait(2)
