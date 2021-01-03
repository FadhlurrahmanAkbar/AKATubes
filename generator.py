import random
import List

# generate random n item list
def listGenerator(n):
    arr = []
    for i in range(n):
        arr.append(n-i)
        #arr.append(random.randint(1,500))
    return arr
List.SaveList("5000Data.txt",listGenerator(5000))