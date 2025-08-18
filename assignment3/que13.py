#wap to check whether a given number is a perfect square or not
import math
num=int(input("enter the number:"))
if math.sqrt(num)==int(math.sqrt(num)):
    print("perfect square")
else:
    print("not perfect square")