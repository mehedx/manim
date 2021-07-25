from manimlib.imports import *

class crush(Scene):
    def construct(self):
        Your Crush Name= TextMobject("I hope you're doing fine!")
        self.play(Write(Your Crush Name))
        self.play(FadeOut(Your Crush Name))
        self.wait()
        Your Crush Name=TextMobject("Smile and Stay blessed :)")
        self.play(Write(Your Crush Name))
        self.play(FadeOut(Your Crush Name))
        self.wait()
        Wink Wink= TextMobject("Enjoy a song , dedicated to your birthday 7w7")
        self.play(Write(Wink Wink))
        self.play(FadeOut(Wink Wink))
        self.wait()

