import random
from settings.player.default import *
from settings.var import *
import time
import os



def stat():
    print("Ваше хп: ", hp, '\n')
    print("В правой руке ", r_hnd, '\n')
    print("Золото: ", gold, '\n')
    #print("x = ", xlm, " ", "y = ", ylm, '\n') 

    def gmap():

        e = 0

        r = 0

        r2 = 0

        if lm[0][0] == 0:
            while e < 164 and r < 10:
                if random.randint(0,2) == 0:
                    if r2 < 10:
                        lm[r][r2] = empty[1]
                        r2 = r2 + 1
                    else:
                        r2 = 0
                        r = r + 1
                elif random.randint(0,2) == 1:
                    if r2 < 10:
                        lm[r][r2] = m[1]
                        r2 = r2 + 1
                    else:
                        r2 = 0
                        r = r + 1
                elif random.randint(0,2) == 2:
                    if r2 < 10:
                        lm[r][r2] = bt[1]
                        r2 = r2 + 1
                    else:
                        r2 = 0
                        r = r + 1
                e = e + 1
            r = 0
            r2 = 0
            e = 0
        print('\n', lm[0], '\n',lm[1], '\n',lm[2], '\n',lm[3], '\n',lm[4], '\n',lm[5], '\n',lm[6], '\n',lm[7], '\n',lm[8], '\n',lm[9], '\n')


    gmap()
    
    time.sleep(1)
    os.system('cls')

