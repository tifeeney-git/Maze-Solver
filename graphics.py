from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title("my title")
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def draw_line(self, line, fillColour="black"):
        line.draw(self.canvas, fillColour)

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y
    
    def draw(self, canvas, fillColour):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fillColour, width=2)

