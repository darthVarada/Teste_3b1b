from manim import *

class MineScopeLogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        
        # Customized text for MineScope
        mine_scope = Text("MineScope", color=logo_black, font_size=72)
        
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        
        logo = VGroup(triangle, square, circle, mine_scope)  # order matters
        logo.arrange(RIGHT, buff=1.0)
        logo.move_to(ORIGIN)
        
        self.add(logo)

# Use one of the following lines to render the animation
# MineScopeLogo("render_version").render()  # Use "rl" for rapid render
MineScopeLogo("preview_version").preview()  # Use "pl" for rapid preview
