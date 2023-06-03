from manim import *
from manim_voiceover import VoiceoverScene

# Use googles Text to Speech API service, clear internet connection is required.
from manim_voiceover.services.gtts import GTTSService

# Azure Voice Service requires clear internet connnection and
from manim_voiceover.services.azure import AzureService

# Own recording service
from manim_voiceover.services.recorder import RecorderService

config.background_color = "#e0e6e2"  # None #
Tex.set_default(color=BLACK)
Text.set_default(color=BLACK)
Mobject.set_default(color=RED)
Dot.set_default(color=BLACK)
VMobject.set_default(color=BLACK, stroke_width=4)
Square.set_default(color=GREEN)

main_tex = config.tex_template

r_preamble = r"""
\usepackage[document]{ragged2e}
\usepackage[usestackEOL]{stackengine}
\usepackage
{
	polyglossia,
	anyfontsize,
	tcolorbox
}

\setmainlanguage[numerals=Devanagari]{bengali}
\setotherlanguage{english}
\newfontfamily\bengalifont[Script=Bengali]{Kalpurush}
"""

bn_tex = TexTemplate(preamble=r_preamble, tex_compiler="lualatex")


class Main(VoiceoverScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.set_speech_service(GTTSService())
        circle = Circle(radius=3, color=WHITE, fill_color=GRAY_C)
        tisha = Text(text='Study Seriously Sadia Jahan Tisha.\nStop naughtiness.')
        logo = ImageMobject("logo-top.jpg")

        with self.voiceover(text="This top logo is created inside photoshop. Isn't amazing?") as tracker:
            self.play(GrowFromCenter(logo), run_time=tracker.duration)


# Azure tts docs: https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=stt
class TextAzure(VoiceoverScene):
    def construct(self):
        self.set_speech_service(AzureService(voice="en-GB-OliverNeural", style="newscast-casual"))
        banner = ManimBanner().scale(0.6)
        with self.voiceover(
                text="This is exampling with AzureVoice service. Hello Kiron. Let's talk some dirty you naughty boy.") as tra:
            self.play(banner.create(), run_time=tra.duration)


class MathTexVoiceOver(VoiceoverScene):
    def construct(self):
        self.set_speech_service(AzureService(voice="bn-BD-PradeepNeural", style="newcast-casual"))
        tex = Tex(r"$a^2+2ab+b^2$").scale(2)
        with self.voiceover(
                text="আমার কাছে একটি বীজগাণিতিক রাশি রয়েছে। এ এর বর্গ যোগ এ এবং বি এর গুণফলের দ্বিগুণের সাথে বি এর বর্গের সমষ্টি।") as tracker:
            self.play(Write(tex), run_time=tracker.duration)


class CallHasib(VoiceoverScene):
    def construct(self):
        self.set_speech_service(AzureService(voice="bn-BD-NabanitaNeural", style="newcast-casual"))
        text = Tex(r"\textbf{হাসিব ভাই} $০৩৭$", tex_template=bn_tex).scale(
            2)  # bug: follow1: https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/quadratic-formula-arabic.py, follow2: https://github.com/3b1b/manim/issues/525
        with self.voiceover(text="হাসিব ভাই ০৩৭") as tracker:
            self.play(Write(text), run_time=tracker.duration)


class DoubledLine(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        line = Line(color=WHITE, start=(-3, 0, 0), end=(3, 0, 0), stroke_width=2)
        doubled_line = VGroup(line, line.copy().shift(UP * 0.1))

        self.play(ShowIncreasingSubsets(doubled_line))
        self.wait(2)
