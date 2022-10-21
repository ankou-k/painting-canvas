from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):
  DEFAULT_PEN_SIZE = 5.0
  DEFAULT_COLOR = 'red'
  CANVAS_HEIGHT = "200";
  #input("How tall do you want the Canvas to be (pixels)? (Please do not not fill entire screen.) ")
  CANVAS_WIDTH = "200";
  #input("How wide do you want the Canvas to be (pixels)?  (Please do not not fill entire screen.) ")

  def __init__(self):
    self.root = Tk()
    
    self.pen_button = Button(self.root, text='pen', command=self.use_pen)
    self.pen_button.grid(row=0, column=0, sticky='e')

    self.brush_button = Button(self.root, text='brush', command=self.use_brush)
    self.brush_button.grid(row=1, column=0, sticky='e')

    self.color_button = Button(self.root, text='color', command=self.use_color)
    self.color_button.grid(row=0, column=6, sticky='w')

    self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
    self.eraser_button.grid(row=1, column=6, sticky='w')

    self.canv = Canvas(self.root, bg='white', width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
    self.canv.grid(column=1, row=0, rowspan=4)
    #self.canv.config(bg='black')

    self.circle_button = Button(self.root, text='create circle', command=self.use_circle)
    self.circle_button.grid(row=2, column=0, sticky='e') ### change self.canv -> self.circle_button

    self.undo_button = Button(self.root, text='undo', command=self.undo)
    self.undo_button.grid(row=2, column=6, sticky='w')

    self.clear_button = Button(self.root, text='clear', command=self.clear_screen)
    self.clear_button.grid(row=3, column=6, sticky='w')

    self.choose_size_scale = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
    self.choose_size_scale.grid(row=4, column=1)

    Label(self.root, text="hello").place()

    self.setup()
    self.root.mainloop()

  def setup(self):
    self.old_x = None
    self.old_y = None
    self.color = self.DEFAULT_COLOR
    self.pen_size = self.DEFAULT_PEN_SIZE
    self.eraser_on = False
    self.prev_action = None
    
    self.active_button = self.pen_button
    self.canv.bind('<B1-Motion>', self.paint)
    self.canv.bind('<Button-1>', self.draw_shape)
    self.canv.bind('<ButtonRelease-1>', self.reset)
  
  def clear_screen(self):
    self.canv.delete("all")

  def undo(self):
    '''Undo functionality. Added for Ryan Project.'''
    if (self.prev_action):
      self.canv.delete(self.prev_action)
      self.prev_action = None

  def use_circle(self):
    self.activate_button(self.circle_button)

  def use_pen(self):
    self.activate_button(self.pen_button)

  def use_brush(self):
    self.activate_button(self.brush_button)
  
  def use_color(self):
    self.activate_button(self.color_button)
    self.color = askcolor(color=self.color)[1]

  def use_eraser(self):
    self.activate_button(self.eraser_button, eraser_mode=True)

  def activate_button(self, some_button, eraser_mode=False):
    self.active_button.config(relief=RAISED)
    some_button.config(relief=SUNKEN)
    self.active_button = some_button
    self.eraser_on = eraser_mode

  def reset(self, event):
    self.old_x, self.old_y = None, None
  
  def paint(self, event):
    self.pen_size = self.choose_size_scale.get()
    pen_color = self.color
    if self.eraser_on:
      pen_color = 'white'
  
    if self.old_x and self.old_y:
      if self.active_button == self.brush_button: 
          self.prev_action = self.canv.create_oval(self.old_x, self.old_y, (event.x), (event.y), outline=pen_color)
      else:
          self.prev_action = self.canv.create_line(self.old_x, self.old_y, event.x, event.y, width=self.pen_size, fill=pen_color, capstyle=ROUND, smooth=TRUE, splinesteps=25)    
    self.old_x = event.x
    self.old_y = event.y
  
  def draw_shape(self, event):
    pen_color = self.color

    if self.active_button == self.circle_button: 
      self.prev_action = self.canv.create_oval(event.x, event.y, (event.x + 50), (event.y + 50), outline=pen_color, fill=pen_color)


myPaint = Paint()

