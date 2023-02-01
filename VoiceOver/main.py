from manim import *
from manim_voiceover import VoiceoverScene

# Use googles Text to Speech API service, clear internet connection is required.
from manim_voiceover.services.gtts import GTTSService

# Azure Voice Service requires clear internet connnection and
from manim_voiceover.services.azure import AzureService


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
