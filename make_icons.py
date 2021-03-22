from svgwrite import Drawing

# set width and height equal to 100 unit squares
W = 100
H = W

# our icons will consist of simple rectangles with uniform spacing
class rect():
    # coordinates for top left vertex
    x = 0
    y = 0

    # width and height of rectangle
    w = 0
    h = 0
    def __init__(self, w, h, x, y):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

# each icon has a name and set of rectangles
# it can be exported as a drawing
class Icon():
    name = ""
    rects = []
    def __init__(self, name, rects):
        self.name = name
        self.rects = rects
    def export(self):
        dwg = Drawing(self.name, width=W, height=H)
        for r in self.rects:
            dwg.add(dwg.rect(insert=(r.x, r.y), size=(r.w, r.h), fill='black'))
        dwg.save()

# Magic numbers
z = int(W / 5)
s = int(W / 20)
x = int(W - z)
y = int((W - 2*s) / 3)


# Tutoring Icon
rects = [
    rect(x,y,0,0),
    rect(x,y,z,y+s),
    rect(x,y,0,2*(y+s))
]
icon = Icon('icons/tutoring.svg',rects)
icon.export()


# Data Mining Icon
rects = [
    rect(W,y,0,0),
    rect(y,W-y-s,0,y+s),
    rect(y,W-y-s,W-y,y+s)
    ]
icon = Icon('icons/data_mining.svg', rects)
icon.export()


# Tech Support Icon
rects = [
    rect(W,W-y-s,0,0),
    rect(W,y,0,W-y),
]
icon = Icon('icons/tech_support.svg', rects)
icon.export()



# Web Development Icon
rects = [
    rect(y,W,0,0),
    rect(W-y-s, W, y+s,0)
]

icon = Icon('icons/web_development.svg', rects)
icon.export()



# Automation Icon
rects = [
    rect(W,y,0,0),
    rect(W,y,0,2*(y+s)),
    rect(y,y,0,y+s),
    rect(y,y,y+s,y+s),
    rect(y,y,2*(y+s), y+s)
]
icon = Icon('icons/automation.svg', rects)
icon.export()
