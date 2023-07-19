import sys #kolyaska
import time #vremennaya
import random #randomnaya

if __name__ == '__main__': #esli dakabi
    def sleep(rnd): #ZZZZZZZ
        time.sleep(rnd) #ZZZZZZZZ
        return "" #eeee ti che
    rnd = [round(random.uniform(0.1, 1.2), 3), round(random.uniform(0.1, 0.6), 3)] #net ti ne praV
    print(((("eras" if sys.argv[1] == "erase" else sys.argv[1]) if sys.argv[1] != "flash" else "send") + "ing " + ("into " if sys.argv[1] == "boot" else "") + f"\'{sys.argv[2]}\'" + ("" if sys.argv[1] != "flash" else f"({random.randint(10000, 50000)} KB)") + f"...{sleep(rnd[0])}\nOKAY [ {rnd[0]}s]\n" + ("" if sys.argv[1] != "flash" else f"writing \'{sys.argv[2]}\'...\nOKAY [ {rnd[1]}s]\n") + "finished. total time: " + str((rnd[0] if sys.argv[1] != "flash" else (rnd[0] + rnd[1]))) + "s") if sys.argv[1] != "devices" else f"{''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8))}\tfastboot") #chto privet
