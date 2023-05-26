from tkinter import Tk, Label
from PIL import ImageTk, Image

def on_mouse_move(event):
    # Get the current mouse position
    x, y = event.x, event.y
    # Display the mouse position in the console
    print(f"Mouse Position: ({x}, {y})")

def on_mouse_click(event):
    # Stop the Tkinter event loop
    global root
    root.quit()

def main():
    # Create a Tkinter window
    global root
    root = Tk()
    root.title("Image Viewer")

    # Load the image using Pillow
    image = Image.open("static/public/3.png")
    # Resize the image if needed
    image = image.resize((539, 403))

    # Create a Tkinter label to display the image
    img_label = Label(root)
    img_label.pack()

    # Convert the image to a format compatible with Tkinter
    tk_image = ImageTk.PhotoImage(image)
    img_label.config(image=tk_image)

    # Bind the mouse movement event to the window
    root.bind("<Motion>", on_mouse_move)
    # Bind the mouse click event to the window
    root.bind("<Button-1>", on_mouse_click)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
