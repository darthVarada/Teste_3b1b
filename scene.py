from manim import *

class BarChartExample(Scene):
    def construct(self):
        # Functions of the graph
        chartbars = BarChart(
            values=[5, 3, 5, 10, 11, 60, 65, 60, 55, 35, 65],  # 12 dates
            bar_names=["1910 - \n 1929", "1920 - \n 1929", "1930 - \n 1939", "1940 - \n1949", "1950 - \n1959",
                        "1960 - \n1969", "1970 - \n1979", "1980 - \n1989", "1990 - \n1999", "2000 - \n2009", "2010 - \n2019"],
            y_range=[0, 100, 20],
            y_length=6,
            x_length=10,
            color=YELLOW,
            x_axis_config={"font_size": 15},
        )
        Second_Axis = NumberLine(
            x_range=[0, 1200 + 200, 200],
            length=6,
            include_tip=True,
            include_numbers=True,
            rotation=90 * DEGREES,
            buff=0.4,
        )
        #obitos_func = FunctionGraph(
        #    lambda t: chartbars.bars[int((t - 1910) / 10)].get_height(),
        #    color=BLUE,
        #)s

        # Labels
        Second_Axis.next_to(chartbars, RIGHT, buff=0.2)  # Move the second axis to the right
        y_label_left = Text("y-numero de falhas Registradas").scale(0.65).rotate(90 * DEGREES)
        y_label_left.next_to(chartbars, LEFT, buff=0.3)
        y_label_right = Text("y-numero de Obitos Registradas").scale(0.65).rotate(90 * DEGREES)
        y_label_right.next_to(Second_Axis, RIGHT, buff=0.1)

        # Texts
        c_bar_lbls = chartbars.get_bar_labels(font_size=12)
        titolo2 = Tex("Acidentes na Mineração")
        titolo2.to_corner(UP)

        # Animation
        
        self.add(Second_Axis, y_label_right)  # Add the second axis and its label

        self.add(titolo2)
        self.play(DrawBorderThenFill(chartbars), DrawBorderThenFill(c_bar_lbls),
                  DrawBorderThenFill(y_label_left), DrawBorderThenFill(y_label_right), DrawBorderThenFill(Second_Axis))

        self.wait(1)
        #self.play(DrawBorderThenFill(obitos_func))
        self.add(chartbars, c_bar_lbls)
        self.wait(1)
        self.play(FadeOut(chartbars, c_bar_lbls, titolo2, y_label_left, y_label_right, Second_Axis))
        self.wait(1)
