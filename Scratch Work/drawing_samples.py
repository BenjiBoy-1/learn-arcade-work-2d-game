import arcade
from arcade import start_render, finish_render

"""
this is a sample (shrugs while looking confused)
"""

arcade.open_window(600, 600, "Drawing Example")



arcade.set_background_color(arcade.csscolor.SKY_BLUE)

start_render()

#grass
arcade.draw_lrbt_rectangle_filled(left=0, right=599, bottom=0, top=300, color=arcade.csscolor.GREEN)

#first tree
arcade.draw_lrbt_rectangle_filled( 90, 110, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

#second tree
arcade.draw_lrbt_rectangle_filled( 190, 210, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN, 3)

#3rd Tree
arcade.draw_lrbt_rectangle_filled( 290, 310, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

#4th tree
arcade.draw_lrbt_rectangle_filled( 390, 410, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

#5th Tree
arcade.draw_lrbt_rectangle_filled( 490, 510, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                                    (480, 360),
                                    (470, 320),
                                    (530, 320),
                                    (520, 360)
                                    ),
                           arcade.csscolor.DARK_GREEN)
# Sun at the left side of the screen
arcade.draw_circle_filled(100, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(100, 550, 0, 550, arcade.color.YELLOW, 3)  # Left
arcade.draw_line(100, 550, 200, 550, arcade.color.YELLOW, 3)  # Right
arcade.draw_line(100, 550, 100, 450, arcade.color.YELLOW, 3)  # Down
arcade.draw_line(100, 550, 100, 650, arcade.color.YELLOW, 3)  # Up

# Diagonal rays
arcade.draw_line(100, 550, 150, 600, arcade.color.YELLOW, 3)  # Top-Right
arcade.draw_line(100, 550, 150, 500, arcade.color.YELLOW, 3)  # Bottom-Right
arcade.draw_line(100, 550, 50, 600, arcade.color.YELLOW, 3)  # Top-Left
arcade.draw_line(100, 550, 50, 500, arcade.color.YELLOW, 3)  # Bottom-Left

#writing text
arcade.draw_text("Good Morning Mother F****r",
                 95, 230,
                 arcade.color.BLACK, 24)

finish_render()

arcade.run()