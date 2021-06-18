import tkinter as tk
import math


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    #draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    draw_sky(canvas, 0, 0)
    draw_sun(canvas, 650, 100)
    draw_cloud(canvas, 10, 10)
    draw_cloud(canvas, 80, 0)
    draw_cloud(canvas, 200, 33)
    draw_cloud(canvas, 450, 23)
    draw_cloud1(canvas, 500, 0)
    draw_cloud1(canvas, 500, 30)
    draw_cloud1(canvas, 470, 15)
    draw_cloud1(canvas, 200, 40)
    draw_ground(canvas, 0, 450)
    draw_mountain(canvas, 200, 500)
    tree_left = scene_left + 50
    tree_top = scene_top + 330
    tree_height = 150
    draw_pine_tree(canvas, tree_left, tree_top, tree_height)
    tree_left = scene_left + 400
    tree_top = scene_top + 350
    tree_height = 150
    draw_pine_tree(canvas, tree_left, tree_top, tree_height)
    tree_left = scene_left + 100
    tree_top = scene_top + 350
    tree_height = 150
    draw_pine_tree(canvas, tree_left, tree_top, tree_height)
    tree_left = scene_left + 650
    tree_top = scene_top + 345
    tree_height = 150
    draw_pine_tree(canvas, tree_left, tree_top, tree_height)


def draw_sky(canvas, screen_left, screen_top):
    screen_top = 0
    screen_left = 0
    screen_right = 801
    sky_bottom = 450
    canvas.create_rectangle(screen_left, screen_top, screen_right, sky_bottom, fill="skyblue", width=False)

def draw_ground(canvas, ground_left, ground_top):
    ground_left = 0
    ground_top = 450
    ground_right = 801
    ground_bottom = 501
    canvas.create_rectangle(ground_left, ground_top, ground_right, ground_bottom, fill= "tan4", width=False)

def draw_cloud(canvas, cloud_left, cloud_top):
    cloud_width = 200
    cloud_height = 80
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill="azure2", width=False)

def draw_cloud1(canvas, cloud_left, cloud_top):
    cloud_width = 150
    cloud_height = 30
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill="ivory2", width=False)

def draw_mountain(canvas, x, y):
    left1 = 350
    left2 = 500
    right1 = 620
    right2 = 500
    top1 = 485
    top2 = 250

    canvas.create_polygon(left1, left2, right1, right2, top1, top2, fill="#2e160a", width=False)
    

def draw_pine_tree(canvas, peak_x, peak_y, height):
 
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

def draw_sun(canvas, sun_left, sun_top, scale=1):
    sun_width = 100 * scale
    sun_height = 100 * scale
    ray_length = 100 * scale
    ray_width = 3 * scale
    ray_count = 10

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left +(sun_width/2)
    sun_center_y = sun_top + (sun_height/2)

    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill="#FFF7B4", width=False)

    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        ray_x = sun_center_x + math.cos(angle)* ray_length
        ray_y = sun_center_y + math.sin(angle)* ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width = ray_width, fill="#FFF7B4")


def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    #create a variable
    text_horizontal_margin= 20
    text_vertical_margin= 10

    #Draw all horizontal lines 
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left,i,right,i)
        canvas.create_text(left +  text_horizontal_margin, i +  text_vertical_margin, text=f"{i}")

    #Draw vertical lines
    for i in range(left, right, grid_spacing):
         canvas.create_line(i, top, i, bottom)
         canvas.create_text(i, top + text_vertical_margin, text=f"{i}")
# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

    

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()

    

# Call the main function so that
# this program will start executing.


main()