import random
import List

# generate random n item list
def listGenerator(n):
    arr = []
    for i in range(n):
        # arr.append(n-i)
        arr.append(random.randint(1,1500))
    return arr

List.SaveList("1500Data.txt",listGenerator(1500))