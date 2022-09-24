# Mario
## The Terminal

### Video Demo:  <DEMO HERE>

### CS50
This repository was made as part of Harvard's CS50x course; 'an introduction to the intellectual enterprises of Computer Science'.
This 11 week course was taught by Professor David Malan and was definitely very useful. I highly recommend taking this course if 
you are a self-taught programmer like me.

### Description
My final project is a game somewhat like the Mario we have all come to know and love but there's a twist.
This version is played in a terminal; not some fancy console like a PlayStation, Xbox or Nintendo Switch.
This game has coins, obstacles and levels just like the original but the best part is it even has the 
iconic flag at the end of the level.

### Usage
This project should work on any system as long as the steps below are followed:
> 1. Open a terminal. I suggest Visual Studio Code
> 2. Run the command `pip install keyboard`
> 3. Save the folder somewhere on you device
> 4. Use the `cd` command to navigate to that folder
> 5. Run the command `python mario.py`

### Function

#### Movement
All the levels are separate lists with each row being a sub-list.
The player '**M**' is a variable with an x and y coordinate in the level.
Based on the coordinates of the player, a:
> - L (left)
> - R (right)
> - U (up)
> - D (down)
> - LU (left-up) 
> - RU (right-up)
> - LD (left-down)
> - RD (right-down)

variables are set around the player as below:
> - level[y][x] = M
> - L = level[y][x-1]
> - R = level[y][x+1]
> - U = level[y-1][x]
> - D = level[y+1][x]
> - LU = level[y-1][x-1]
> - RU = level[y-1][x+1]
> - LD = level[y+1][x-1]
> - RD = level[y+1][x+1]

Those variables are used to identify the block 
(**#**,**O** etc.) and whether the player can walk on 
top of it or fall. Movement happens when specific 
keys (a,d,w,e,q,z,x) are pressed. This is detected 
with the keyboard library using the line `if keyboard.is_pressed('key')`.
After a key is clicked, the player's current position is changed to `' '`
and using the **L**, **R** etc. variables the player will move.
The player will automatically move down `if D == " ":` and the player isn't jumping.

#### Coins
When the user presses `W`, the player jumps but there is an if statement which 
determines `if U == "?":` . If so, the `coins += 1` is executed.
If the player falls down the hole in the game, a variable `CaveCoins` is used 
which allows the player to go back to the first level after getting 10 more coins.

#### Game Over
In level 1, the only way the player can die is by falling down the hole more than once.

In level 2 though, it's not as easy. The player can now die by standing on top of a 
spike near the start or falling into the red lava at the end.

#### The End
After you have overcome many obstacles and gained many coins, you will come to the 
flag at the end. By completing the game, Mario shall swap the evil flag for a much 
better red one.

