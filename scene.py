from manim import *

class BarChartExample(Scene):
    def construct(self):
        chart = BarChart(
            values=[20, 30, 10, 20, 3],
            bar_names=["cobre", "ferro", "plat", "niobio", "cinco"],
            y_range=[-20, 50, 10],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 30},
        )
        titolo2=Tex("tabela")
        titolo2.to_corner(UP+LEFT)
        c_bar_lbls = chart.get_bar_labels(font_size=48)
        
        self.add(titolo2)
        self.play(DrawBorderThenFill(chart),DrawBorderThenFill(c_bar_lbls))
        self.add(chart, c_bar_lbls)
        self.wait(1)
        self.play(FadeOut(chart, c_bar_lbls, titolo2))
        self.remove(chart, c_bar_lbls, titolo2)
        self.wait(1)
