from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title("my title")
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
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

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.win = window
        self.visited = False

    def draw(self,x1, y1, x2, y2):
        if self.win is None:
            return
        self.x1  = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if self.has_left_wall == True:
            l = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(l, "black")
        else:
            l = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(l, "white")

        if self.has_right_wall == True:
            l = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(l, "black")
        else:
            l = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(l, "white")

        if self.has_top_wall == True:
            l = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(l, "black")
        else:
            l = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(l, "white")
        if self.has_bottom_wall == True:
            l = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(l, "black")
        else:
            l = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(l, "white")

    def draw_move(self, to_cell, undo=False):
        lineColour = "red"
        if undo == True:
            lineColour = "gray"
        x1 = (self.x1 + self.x2) / 2
        y1 = (self.y1 + self.y2) / 2
        x2 = (to_cell.x1 + to_cell.x2) / 2
        y2 = (to_cell.y1 + to_cell.y2) / 2
        l = Line(Point(x1, y1), Point(x2, y2))
        self.win.draw_line(l, lineColour)