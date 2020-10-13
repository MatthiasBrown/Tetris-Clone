
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)

GREEN = ( 0, 255, 0)  #S-BLOCK
RED = ( 255, 0, 0)    # Z-BLOCK
BLUE = (0,0,255) # J-BLOCK
ORANGE = (255, 127, 0)  # L-BLOCK
YELLOW = (255,255,0)   # O-BLOCK
PURPLE = (128, 0 , 128) # T-BLOCK
TURQUOISE = (64, 224, 208) # I-BLOCK

x = 50    # The direction of our Blocks, LEFT/UP is negative direction
y = 50
#axis  # TODO: Set up rotation
height = 60
width = 40
vel = 5

level = [ i for i in range(100)]
level_speed = [i for i in range(10)]


#This the gird the game occurs in, 16 rows by 10 coloums
#tile_gird= ([], [])
