import keyboard
import time
import os

from level import *
from title import *
from sprites import *

os.system('clear')
time.sleep(0.5)

#print title
format(main)
time.sleep(1)

#print the level
print(f"Coins: {coins}")
formatF(level)

while True:

    #Player Movement
    if keyboard.is_pressed("space"):
        time.sleep(0.1)
        os.system('clear')
        format(main)
        print(f"Coins: {coins}")
        format(level)
    #move player up when 'w' is pressed
    elif keyboard.is_pressed("w"):
        #sleep so user can't move 
        time.sleep(0.1)
        for i in range(2):
            if U == " ":
                os.system('clear')
                format(main)
                #make player's current position " "
                level[y][x] = " "
                #minus one from y
                y -= 1
                #move player to new position
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
                #re-initialise variables
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
            elif U == Q and (D == G or D == B) or U == Q and D == " ":
                os.system('clear')
                format(main)
                level[y-1][x] = Do
                coins += 1
                if level == cave:
                    CoinsCave += 1
                print(f"Coins: {coins}")
                format(level)
        
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
            elif D == " ":
                os.system('clear')
                format(main)
                level[y][x] = " "
                y += 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
            else:
                os.system('clear')
                format(main)
                print(f"Coins: {coins}")
                format(level)
        if U == Do and D == " ":
            os.system('clear')
            format(main)
            level[y][x] = " "
            y += 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)
        
            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
            time.sleep(0.2)
        elif D == " ":
            for i in range(2):
                os.system('clear')
                format(main)
                #make player's current position " "
                level[y][x] = " "
                #minus one from y
                y += 1
                #move player to new position
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
                #re-initialise variables
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)

    elif keyboard.is_pressed("a"):
        os.system('clear')
        format(main)
        time.sleep(0.1)
        if L == " ":
            if x != 0:
                level[y][x] = " "
                x -= 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)

                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
            else:
                print(f"Coins: {coins}")
                format(level)
        elif L != " " and LU == " " and U == " ":
            os.system('clear')
            format(main)
            level[y][x] = " "
            y -= 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)

            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
            time.sleep(0.2)
            os.system('clear')
            format(main)
            level[y][x] = " "
            x -= 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)

            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
        else:
            print(f"Coins: {coins}")
            format(level)

    elif keyboard.is_pressed("d"):
        os.system('clear')
        format(main)
        time.sleep(0.1)
        if R == " ":
            if x != 52:
                level[y][x] = " "
                x += 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)

                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]

                if level == underground:
                    if R == " |":
                        time.sleep(0.1)
                        os.system('clear')
                        format(main)

                        level[y-3][x+1] = " |"
                        level[y-2][x+1] = "Σ|"
                        print(f"Coins: {coins}")
                        format(level)
                        level[y-2][x+1] = " |"
                        level[y-1][x+1] = "Σ|"
                        time.sleep(0.1)
                        os.system('clear')
                        format(main)
                        print(f"Coins: {coins}")
                        format(level)
                        level[y-1][x+1] = " |"
                        level[y-0][x+1] = "Σ|"
                        time.sleep(0.1)
                        os.system('clear')
                        format(main)
                        print(f"Coins: {coins}")
                        format(level)

                        flag = "\033[0;31mΣ\033[0;37;40m"
                        level[y-1][x+1] = " |"
                        level[y-0][x+1] = flag + "|"
                        time.sleep(0.1)
                        os.system('clear')
                        format(main)
                        print(f"Coins: {coins}")
                        format(level)
                        level[y-1][x+1] = flag + "|"
                        level[y-0][x+1] = " |"
                        time.sleep(0.1)
                        os.system('clear')
                        format(main)
                        print(f"Coins: {coins}")
                        format(level)
                        level[y-2][x+1] = flag + "|"
                        level[y-1][x+1] = " |"
                        time.sleep(0.1)
                        os.system('clear')
                        format(main)
                        print(f"Coins: {coins}")
                        format(level)
                        level[y-3][x+1] = flag + "|"
                        level[y-2][x+1] = " |"
                        time.sleep(0.1)
                        os.system('clear')
                        format(main)
                        format(win)

                        L = level[y][x-1]
                        R = level[y][x+1]

                        U = level[y-1][x]
                        D = level[y+1][x]

                        LU = level[y-1][x-1]
                        LD = level[y+1][x-1]
                        RU = level[y-1][x+1]
                        RD = level[y+1][x+1]
                        time.sleep(0.2)
                        exit()
            else:
                print(f"Coins: {coins}")
                format(level)
        elif R != " " and RU == " " and U == " ":
            os.system('clear')
            format(main)
            level[y][x] = " "
            y -= 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)

            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
            time.sleep(0.2)
            os.system('clear')
            format(main)
            level[y][x] = " "
            x += 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)

            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
        else:
            os.system('clear')
            format(main)
            print(f"Coins: {coins}")
            format(level)

    elif keyboard.is_pressed("q"):
        time.sleep(0.1)
        os.system('clear')
        format(main)
        if U == " ":
            level[y][x] = " "
            y -= 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)
           
            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
            time.sleep(0.2)

            if L != " " and LU == " ":
                os.system('clear')
                format(main)
                level[y][x] = " "
                y -= 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)

                os.system('clear')
                format(main)
                level[y][x] = " "
                x -= 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
            elif L == " " or LU != " ":
                os.system('clear')
                format(main)
                level[y][x] = " "
                y += 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
        else:
            os.system('clear')
            format(main)
            print(f"Coins: {coins}")
            format(level)

    elif keyboard.is_pressed("e"):
        time.sleep(0.1)
        os.system('clear')
        format(main)
        if U == " ":
            level[y][x] = " "
            y -= 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)
           
            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
            time.sleep(0.2)

            if R != " " and RU == " ":
                os.system('clear')
                format(main)
                level[y][x] = " "
                y -= 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)

                os.system('clear')
                format(main)
                level[y][x] = " "
                x += 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
            elif R == " " or RU != " ":
                os.system('clear')
                format(main)
                level[y][x] = " "
                y += 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
        else:
            os.system('clear')
            format(main)
            print(f"Coins: {coins}")
            format(level)

    elif keyboard.is_pressed("x"):
        time.sleep(0.1)
        os.system('clear')
        format(main)
        if U == " " and RU == " ":
            level[y][x] = " "
            y -= 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)
           
            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
            time.sleep(0.2)
            os.system('clear')
            format(main)

            level[y][x] = " "
            x += 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)
           
            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
            time.sleep(0.2)
            if R == " " and RD == " ":
                os.system('clear')
                format(main)
                level[y][x] = " "
                x += 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
                os.system('clear')
                format(main)

                level[y][x] = " "
                y += 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
            elif R == " " and RD != " ":
                os.system('clear')
                format(main)
                level[y][x] = " "
                x += 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
            elif D == " ":
                os.system('clear')
                format(main)
                level[y][x] = " "
                y += 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
            else:
                os.system('clear')
                format(main)
                print(f"Coins: {coins}")
                format(level)

        else:
            format(level)

    elif keyboard.is_pressed("z"):
        time.sleep(0.1)
        os.system('clear')
        format(main)
        if U == " " and LU == " ":
            level[y][x] = " "
            y -= 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)
           
            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
            time.sleep(0.2)
            os.system('clear')
            format(main)

            level[y][x] = " "
            x -= 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)
           
            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
            time.sleep(0.2)
            if L == " " and LD == " ":
                os.system('clear')
                format(main)
                level[y][x] = " "
                x -= 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
                os.system('clear')
                format(main)

                level[y][x] = " "
                y += 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
            elif L == " " and LD != " ":
                os.system('clear')
                format(main)    
                level[y][x] = " "
                x -= 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
            elif D == " ":
                os.system('clear')
                format(main)
                level[y][x] = " "
                y += 1
                level[y][x] = M
                print(f"Coins: {coins}")
                format(level)
            
                L = level[y][x-1]
                R = level[y][x+1]

                U = level[y-1][x]
                D = level[y+1][x]

                LU = level[y-1][x-1]
                LD = level[y+1][x-1]
                RU = level[y-1][x+1]
                RD = level[y+1][x+1]
                time.sleep(0.2)
            else:
                os.system('clear')
                format(main)
                print(f"Coins: {coins}")
                format(level)

        else:
            format(level)
   

    elif keyboard.is_pressed("ctrl + c"):
        exit()

    if D == S:
        os.system('clear')
        format(main)
        format(gameOver)
        exit()

    #Physics
    if D == " ":
        try:
            time.sleep(0.1)
            os.system('clear')
            format(main)
            level[y][x] = " "
            y+= 1
            level[y][x] = M
            print(f"Coins: {coins}")
            format(level)

            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
            time.sleep(0.2)
        except:
            if CoinsCave == 0:
                level[y][x] = " "
                level = cave
                x = 2
                y = 3
                level[y][x] = M

                continue
            else:
                os.system('clear')
                format(main)
                format(gameOver)
                exit()

    elif D == Lv:
        time.sleep(0.1)
        os.system('clear')
        format(main)
        level[y][x] = " "
        y+= 1
        level[y][x] = M
        print(f"Coins: {coins}")
        format(level)

        L = level[y][x-1]
        R = level[y][x+1]

        U = level[y-1][x]
        D = level[y+1][x]

        LU = level[y-1][x-1]
        LD = level[y+1][x-1]
        RU = level[y-1][x+1]
        RD = level[y+1][x+1]
        time.sleep(0.2)
        os.system('clear')
        format(main)
        format(gameOver)
        exit()

    #Teleport
    if D == T:
        if coins >= 7:
            level = underground
            x = 2
            y = 2
            level[y][x] = M

            continue

    elif level == cave:
        if CoinsCave == 9:
            level = home
            x = 9
            y = 3
            level[y][x] = M
            os.system('clear')
            format(main)
            print(f"Coins: {coins}")
            format(level)

            L = level[y][x-1]
            R = level[y][x+1]

            U = level[y-1][x]
            D = level[y+1][x]

            LU = level[y-1][x-1]
            LD = level[y+1][x-1]
            RU = level[y-1][x+1]
            RD = level[y+1][x+1]
            time.sleep(0.2)



