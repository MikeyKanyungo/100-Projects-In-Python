import random 
import time 

def main ():
    lst = [0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,0,0,0]
    random.shuffle(lst)
    time.sleep(0.075)
    print (lst) 

    main()

main ()