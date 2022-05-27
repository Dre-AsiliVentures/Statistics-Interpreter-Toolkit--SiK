# Creating Lists
import time
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
functions=['Append','Insert','Pop','Remove','Remove','Sort','Reverse']
print("The length of functions are: {}".format(len(functions)))
print("The last term of functions is: {}".format(functions[6]))

#Method 1: Direct Method
sixteenlists=['MondayReverse','TuesdayInsert','WednesdayAppend',
'ThursdayRemove','FridayPop','SaturdayPop','SundaySort']

print ("Method 1: Direct:\n\n      {}\n".format(sixteenlists))
#Method 2 : Using lists function
digit=days[0]+functions[3]
print(digit)
digits=list()
def Lists_insert():
    print("The Length empty list is:\n{}".format(len(digits)))
    print("The empty list looks like:\n{}".format(digits))
    digits.insert(0,days[0]+functions[6])
    digits.insert(1,days[1]+functions[1])
    digits.insert(2,days[2]+functions[0])
    digits.insert(3,days[3]+functions[3])
    digits.insert(4,days[4]+functions[2])
    digits.insert(5,days[5]+functions[2])
    digits.insert(6,days[6]+functions[3])
    for i in range(0,7):
        print("\n       -------")
        time.sleep(1)
        print("\n               --------")
        print("The list at {} ".format(i)+"is"+" {}\n".format(digits[i]==sixteenlists[i]))
        return digits
Lists_insert()
time.sleep(2)
print("The Reverse function now executing -------\n")
time.sleep(1)
print("Unakumbuka the original list was like:\n{}".format(digits))
print("\n Now after reversing inakaa hivi:{}".format(digits.reverse()))
# HackerRank Exercise
if __name__ == '__main__':
    N = int(input("Enter N"))
    for i in range(1,N):
        list=[]
        print(list)
        i=int(N*0.23)
        e=N*100
        list.insert(i,e)
        list.remove(e)
        print(list.sort())
        list.pop()
        print(list.reverse)
