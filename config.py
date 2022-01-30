FPS = 120
dt = 1/FPS


# size of window 
WIN_HEIGHT = 800
WIN_WIDTH = 800

# size for calculations
# x = [-10, 10]
# y = [0, 20]
CALC_WIDTH = 20 
CALC_HEIGHT = 20

# gravity 
ACC = 20

def translate_coords(x, y):
    x_win = x*WIN_WIDTH/CALC_WIDTH + WIN_WIDTH/2
    y_win = (WIN_HEIGHT - 100) - y*WIN_HEIGHT/CALC_HEIGHT
    return int(x_win), int(y_win)