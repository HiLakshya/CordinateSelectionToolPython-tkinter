import tkinter as tk
from PIL import Image, ImageTk

class ResizableSquareApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Resizable Square")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Draw light black outline across the canvas
        self.canvas.create_line(0, 0, 400, 0, fill="black", width=1)
        self.canvas.create_line(400, 0, 400, 400, fill="black", width=1)
        self.canvas.create_line(400, 400, 0, 400, fill="black", width=1)
        self.canvas.create_line(0, 400, 0, 0, fill="black", width=1)

        # Label coordinates on each corner of the canvas
        self.canvas.create_text(10, 10, text="(0, 0)", anchor="nw")
        self.canvas.create_text(390, 10, text="(400, 0)", anchor="ne")
        self.canvas.create_text(390, 390, text="(400, 400)", anchor="se")
        self.canvas.create_text(10, 390, text="(0, 400)", anchor="sw")

        # Load and display the tshirt.png
        tshirt_image = Image.open("cat.png")
        self.tshirt_photo = ImageTk.PhotoImage(master=self.master, image=tshirt_image)
        self.canvas.create_image(200, 200, image=self.tshirt_photo)

        self.square = None
        self.start_x = None
        self.start_y = None

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_square)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def draw_square(self, event):
        x, y = self.start_x, self.start_y
        if self.square:
            self.canvas.delete(self.square)
        self.square = self.canvas.create_rectangle(x, y, event.x, event.y, fill="blue")

    def stop_draw(self, event):
        bbox = self.canvas.bbox(self.square)
        print("\n\nSquare coordinates: ")
        print(f"Top left: ({bbox[0]}, {bbox[1]})")
        print(f"Top right: ({bbox[2]}, {bbox[1]})")
        print(f"Bottom right: ({bbox[2]}, {bbox[3]})")
        print(f"Bottom left: ({bbox[0]}, {bbox[3]})")

def main():
    root = tk.Tk()
    app = ResizableSquareApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
