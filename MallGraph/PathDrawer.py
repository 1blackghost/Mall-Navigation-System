from PIL import Image, ImageDraw
import os

class Drawer:
    def draw_for_floor_1(self, filename, coordinates):
        # Load the image
        image_path = "static/public/1.png"
        image = Image.open(image_path)

        # Create a draw object
        draw = ImageDraw.Draw(image)

        # Define the coordinates
        xy_coordinates = [(x, y) for x, y, _ in coordinates]

        # Set colors and line properties
        start_color = "red"
        end_color = "green"
        intermediate_color = "white"
        marker_color = "black"
        line_color = "blue"
        line_width = 5
        marker_radius = 5

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
