# Programming Project 2
# 16102275 Park Hyun Woo &16102284 Lee Sung Ho
# Programming Project 2 Problem 1


from itm421draw import new_canvas,show

THE_SIZE = 512

canvas = new_canvas(THE_SIZE + 1, THE_SIZE + 1, "white")

# --------------------------------------------------------------------

def draw_front(x, y, side, level):
  
  if level < 1:
    return
  hs = side // 2
  left =   x - hs
  top =    y - hs
  right =  x + hs
  bottom = y + hs
  nside = int(side / 2.2)
  draw_front(left, top, nside, level-1)
  draw_front(left, bottom, nside, level-1)
  draw_front(right, top, nside, level-1) 
  draw_front(right, bottom, nside, level-1)
  canvas.rectangle((x-hs, y-hs, x+hs, y+hs), fill="gray", outline="black")
  
def draw_order(x, y, side, level):
  
  if level < 1:
    return
  hs = side // 2
  left =   x - hs
  top =    y - hs
  right =  x + hs
  bottom = y + hs
  nside = int(side / 2.2)
  draw_order(left, top, nside, level-1)
  draw_order(right, top, nside, level-1)
  canvas.rectangle((x-hs, y-hs, x+hs, y+hs), fill="gray", outline="black")
  draw_order(left, bottom, nside, level-1)
  draw_order(right, bottom, nside, level-1)
  
  
def draw_right(x, y, side, level):
  
  if level < 1:
    return
  hs = side // 2
  left =   x - hs
  top =    y - hs
  right =  x + hs
  bottom = y + hs
  nside = int(side / 2.2)
  draw_right(left, top, nside, level-1)
  draw_right(left, bottom, nside, level-1)
  draw_right(right, bottom, nside, level-1)
  canvas.rectangle((x-hs, y-hs, x+hs, y+hs), fill="gray", outline="black")
  draw_right(right, top, nside, level-1)

def draw_back(x, y, side, level):
  
  if level < 1:
    return
  hs = side // 2
  left =   x - hs
  top =    y - hs
  right =  x + hs
  bottom = y + hs
  nside = int(side / 2.2)
  canvas.rectangle((x-hs, y-hs, x+hs, y+hs), fill="gray", outline="black")
  draw_back(left, top, nside, level-1)
  draw_back(left, bottom, nside, level-1)
  draw_back(right, top, nside, level-1) 
  draw_back(right, bottom, nside, level-1)

  

# --------------------------------------------------------------------

if __name__ == "__main__":
  print("Click into the drawing or press <Enter> to see the next drawing")
  for level in range(1, 7):
    canvas.rectangle((0, 0, THE_SIZE, THE_SIZE), fill="white")
    draw_back(THE_SIZE // 2, THE_SIZE // 2, 5 * THE_SIZE // 9, level)
    show()

