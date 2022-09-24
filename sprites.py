from level import level

x = 1
y = 3

M = "\033[0;31mM\033[0;37;40m"
level[y][x] = M

coins = 0
CoinsCave = 0

#initialise variables for cells around the player
L = level[y][x-1]
R = level[y][x+1]

U = level[y-1][x]
D = level[y+1][x]

LU = level[y-1][x-1]
LD = level[y+1][x-1]
RU = level[y-1][x+1]
RD = level[y+1][x+1]
