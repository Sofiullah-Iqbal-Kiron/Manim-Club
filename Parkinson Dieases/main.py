from manim import *


class Main(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Tyrosine = Text('Tyrosine', color=BLACK)
        Ldopa = Text('L-dopa', color=BLACK).shift(DOWN)
        Tyrosine_to_Ldopa = Arrow(start=UP, end=DOWN, color=BLACK)
        Tyrosine_to_Ldopa_tip = Text('Tyrosine\nhydroxylase', color=BLACK)

        Dopamine = Text('Dopamine', color=BLACK)
        Ldopa_to_Dopamine = Arrow(start=UP, end=DOWN, color=BLACK)
        Ldopa_to_Dopamine_tip = Text('DOPA\ndecarboxylase', color=BLACK)

        DOPAC = Text('DOPAC', color=BLACK)
        Dopamine_to_DOPAC = Arrow(start=UP, end=DR, color=BLACK)
        Dopamine_to_DOPAC_tip = Text('MONOAMINE\nOXIDASE', color=BLACK)
        VMAT2 = Text('VMAT2', color=BLACK)
        Dopamine_to_VMAT2 = Arrow(start=UP, end=DL, color=BLACK)

        DAT = Text('DAT', color=BLACK)

        Tyrosine_to_Ldopa.next_to(Tyrosine, DOWN * 0.5)
        Tyrosine_to_Ldopa_tip.next_to(Tyrosine_to_Ldopa, LEFT * 0.5)
        Ldopa_to_Dopamine.next_to(Ldopa, DOWN * 0.5)
        Ldopa_to_Dopamine_tip.next_to(Ldopa_to_Dopamine, LEFT * 0.5)
        Dopamine_to_DOPAC.next_to(Dopamine, DR)
        DOPAC.next_to(Dopamine_to_DOPAC, DOWN * 0.5)

        g1 = Group(Tyrosine, Tyrosine_to_Ldopa, Tyrosine_to_Ldopa_tip, Ldopa, Dopamine, Ldopa_to_Dopamine,
                   Ldopa_to_Dopamine_tip, DOPAC, Dopamine_to_DOPAC, Dopamine_to_DOPAC_tip, VMAT2, Dopamine_to_VMAT2)

        self.add(g1)


class Two(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        Tyrosine = Text('Tyrosine', color=BLACK).to_corner(UP, 0.5)
        Ldopa = Text('L-dopa', color=BLACK).next_to(Tyrosine, DOWN * 2.5)
        Tyrosine_to_Ldopa = Arrow(Tyrosine.get_bottom(), Ldopa.get_top(), color=BLACK)
        Tyrosine_to_Ldopa_tip = Text('Tyrosine\nhydroxylase', color=BLACK).scale(0.3).next_to(Tyrosine_to_Ldopa,
                                                                                              LEFT * 0.5)
        Tyrosine_holder = Square(color=BLACK).surround(Tyrosine)
        Tyrosine_to_Ldopa.set_start_and_end_attrs(Tyrosine_holder.get_bottom(), Ldopa.get_top())

        g1 = Group(Tyrosine, Tyrosine_holder, Ldopa, Tyrosine_to_Ldopa, Tyrosine_to_Ldopa_tip).scale(1)
        self.add(g1)
