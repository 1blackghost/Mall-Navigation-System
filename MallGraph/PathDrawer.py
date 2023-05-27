from PIL import Image, ImageDraw
import os

class Drawer:
    def draw_for_floor(self, filename, image_path, coordinates, stair_coordinates, start=False, end=False):
        # Load the image
        image = Image.open(image_path)

        # Create a draw object
        draw = ImageDraw.Draw(image)

        # Define the coordinates
        xy_coordinates = [(x, y) for x, y, _ in coordinates]

        # Set colors and line properties
        start_color = "green" if start else "black"
        end_color = "red" if end else "black"
        intermediate_color = "white"
        marker_color = "black"
        stair_color = "yellow"
        line_color = "blue"
        line_width = 10
        marker_radius = 10

        # Draw circles at start and end locations
        draw.ellipse(
            (
                xy_coordinates[0][0] - marker_radius,
                xy_coordinates[0][1] - marker_radius,
                xy_coordinates[0][0] + marker_radius,
                xy_coordinates[0][1] + marker_radius,
            ),
            fill=start_color,
            outline=start_color,
        )
        draw.ellipse(
            (
                xy_coordinates[-1][0] - marker_radius,
                xy_coordinates[-1][1] - marker_radius,
                xy_coordinates[-1][0] + marker_radius,
                xy_coordinates[-1][1] + marker_radius,
            ),
            fill=end_color,
            outline=end_color,
        )

        # Draw circles at intermediate locations
        for x, y in xy_coordinates[1:-1]:
            if any(x == sx and y == sy for sx, sy, _ in stair_coordinates):
                # Mark stair coordinates as yellow
                draw.ellipse(
                    (x - marker_radius, y - marker_radius, x + marker_radius, y + marker_radius),
                    fill=stair_color,
                    outline=stair_color,
                )
            else:
                # Draw regular markers
                draw.ellipse(
                    (x - marker_radius, y - marker_radius, x + marker_radius, y + marker_radius),
                    fill=marker_color,
                    outline=marker_color,
                )

        # Draw the line
        draw.line(xy_coordinates, fill=line_color, width=line_width)

        # Save the image with the line and markers
        output_dir = "static"
        os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
        output_path = os.path.join(output_dir, filename)
        image.save(output_path, quality=95, dpi=(300, 300))

    def draw_for_floor_1(self, filename, coordinates, start=False, end=False):
        image_path = "static/public/1.png"
        stair_coordinates = [(338, 257, 1)]
        self.draw_for_floor(filename, image_path, coordinates, stair_coordinates, start, end)

    def draw_for_floor_2(self, filename, coordinates, start=False, end=False):
        image_path = "static/public/2.png"
        stair_coordinates = [(882, 571, 2)]
        self.draw_for_floor(filename, image_path, coordinates, stair_coordinates, start, end)

    def draw_for_floor_3(self, filename, coordinates, start=False, end=False):
        image_path = "static/public/3.png"
        stair_coordinates = [(420, 306, 3)]
        self.draw_for_floor(filename, image_path, coordinates, stair_coordinates, start, end)
