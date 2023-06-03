# Creating a svg which is written in latex and compiled using manim. Then use it as a svgmobjec.

# Issue: I think the box.svg object which is generated inside a seperated environment that taking entire line as a inline block.

from manim import *

tbox = r'''
\newtcolorbox{mybox}{colback=red!5!white, colframe=red!75!black, width=8cm}
\begin{mybox}
    \textcolor{black}{This is my own box.}
\end{mybox}
'''


class Main(Scene):
    def construct(self):
        self.wait(0.5)

        # self.camera.background_color = WHITE
        # Basic self settings.
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{tcolorbox, tikz}")

        self.always_update_mobjects = True
        box = Tex(tbox, tex_template=myTemplate)

        theBox = SVGMobject("box.svg").scale(0.5)
        self.play(DrawBorderThenFill(theBox), run_time=3)
        self.play(Indicate(theBox, color=theBox.get_color()))

        self.wait()


class AtomSVG(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        apple = SVGMobject("apple.svg").scale(2)
        self.play(Create(apple), run_time=3)
        self.play(apple.animate.scale(0.5))

        self.wait(2)


class LogoAnimate(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.wait(0.5)

        react = SVGMobject("react logo.svg", height=2.2, width=2.2).shift(LEFT * 5)
        angular = SVGMobject("angular logo.svg", height=2.2, width=2.2).next_to(react, RIGHT * 5)
        vue = SVGMobject("vue logo.svg", height=2.2, width=2.2).next_to(angular, RIGHT * 5)

        g1 = Group(react, angular, vue).move_to(ORIGIN)

        for fra in g1:
            self.add_sound("grow sound.mp3", gain=1.5)
            self.play(GrowFromPoint(fra, fra.get_center()), run_time=0.5)
            self.wait(1)

        self.wait(3)

        self.play(FadeOut(Group(angular, vue), run_time=0.6), react.animate.move_to(ORIGIN).scale(2))
        self.play(Circumscribe(react))
        self.wait(3)


class QuotedText(Scene):
    def construct(self):
        self.wait(0.5)

        text = r'''
        A REST API should spend almost all of its descriptive effort
        \linebreak
        in defining the media type(s) used for representing resources
        \linebreak
        and driving application state.
        '''
        quote = Tex(text)
        quoter = Text("- Roy Fielding").next_to(quote, DOWN).shift(RIGHT * 4)
        self.play(Write(quote, run_time=4))
        self.play(Create(quoter, run_time=2))
        self.wait(2)
        self.play(Unwrite(quote), FadeOut(quoter))
