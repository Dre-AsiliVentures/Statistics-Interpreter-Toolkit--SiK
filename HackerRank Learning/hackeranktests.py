import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter your input: " ))
    if n>1 and n<100:
        remainder=n%2
        print("Remainder is:"+str(remainder))
        if remainder==0: #If the number is even, print it
                print("Not weird")
                if n>2 and n<5:
                    print("Not Weird")
                elif n>6 and n<20:
                    print("Weird")
                else:
                    pass
        else:
            print("Not Weird")