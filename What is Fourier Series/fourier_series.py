from manim import *


class FourierSeries(Scene):
    def construct(self):
        # self.add(NumberPlane())
        self.always_update_mobjects = True
        subscribe = Text("Subscribe", font_size=15, color=WHITE).move_to([6.5, 4.7, 0])
        # subscribe.shift(6.5 * RIGHT)
        self.add(subscribe)

        ourBasicTrigonometricSeriesIs = Text(text="We know that the basic trigonometric series is: ", font="Arial",
                                             font_size=52, weight=SEMIBOLD, width=12, color=GREEN)
        theBasicTrigonometricEquation = MathTex(r"\frac{A_0}{2} + \sum_{n=1}^{\infty} (A_n\cos nx + B_n\sin nx)",
                                                font_size=48)
        g1 = Group(ourBasicTrigonometricSeriesIs, theBasicTrigonometricEquation).arrange(DOWN, buff=MED_LARGE_BUFF)

        self.play(AddTextLetterByLetter(ourBasicTrigonometricSeriesIs), run_time=2)
        self.play(FadeIn(theBasicTrigonometricEquation), run_time=3)
        self.play(g1.animate.scale(0.65).shift(2.9 * UP))
        self.wait(1)

        itWillCalled = Tex(r"It will be called \textbf{Fourier Series} if the terms $A_0, A_n, B_n$ is:",
                           font_size=40).shift(1.5 * LEFT)
        A0 = MathTex(r"A_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)\cdot dx", font_size=40)
        An = MathTex(r"A_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cdot \cos nx\cdot dx", font_size=40)
        Bn = MathTex(r"B_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cdot \sin nx\cdot dx", font_size=40)
        g2 = Group(A0, An, Bn).arrange(DOWN, buff=MED_SMALL_BUFF).move_to(0.5 * DOWN)
        whereFX = Tex(r"Where \textbf{$f(x)$} is any single-valued function defined in interval $(-\pi, \pi)$.",
                      font_size=35).next_to(g2, 1 * DOWN)

        self.play(Create(itWillCalled), run_time=2)
        self.wait(1)
        self.play(itWillCalled.animate.scale(0.7).next_to(g2, 1.3 * UP))
        self.play(itWillCalled.animate.set_fill(RED), SpinInFromNothing(g2), point_color=RED)
        self.play(Indicate(g2))
        self.play(Write(whereFX), run_time=3)
        self.play(whereFX.animate(run_time=1.2).shift(0.5 * DOWN).scale(1.3))
        self.play(Circumscribe(whereFX))
        self.wait(2)
