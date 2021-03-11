import sys
import math
from PIL import Image

# Return a character based on perceived luminosity of RGB value
def getChar(r,g,b):
  lum = math.sqrt(0.299*r*r + 0.587*g*g + 0.114*b*b)
  chars = (' ','.',':','-','=','o','a','O','E','X','M','@')
  char = int(lum/255*len(chars))
  if dark:
    char = len(chars)-char-1
  
  return chars[char]

# arg1 = Resolution (This is more of a ratio. eg: 2 = half size, min: 1)
resX = int(sys.argv[1])
resY = int(resX*1.6) # Rough estimate for char height vs width

# [arg2] = invert ('i' = Output for light mode users)
dark=0
if len(sys.argv) >= 3:
  if sys.argv[2] == 'i':
    dark = 1

# Load image
img = Image.open('thor.png')
pixels = img.load()
w = img.size[0]
h = img.size[1]

# Create new image based on specified resolution
new = Image.new('RGB', (int(w/resX), int(h/resY)), color = 'black')
newPx = new.load()

# Temp pixel
r=0
g=0
b=0

# Do the thing
for j in range(0, resY*int(h/resY), resY):
  for i in range(0, resX*int(w/resX)):
    for k in range (0, resY):
      # Adding RGB values to Temp pixel
      r += pixels[i,j+k][0]
      g += pixels[i,j+k][1]
      b += pixels[i,j+k][2]
    if (i+1) % resX == 0:
      # Average out the added up values and print a thing
      r = int(r/resX/resY)
      g = int(g/resX/resY)
      b = int(b/resX/resY)
      print (getChar(r,g,b), end='')
      
      # Reset Temp pixel values
      r=0
      g=0
      b=0
  print ()
