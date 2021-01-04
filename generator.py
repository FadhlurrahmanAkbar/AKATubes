import random
import List

# generate random n item list
def listGenerator(n):
    arr = []
    pick = str(input())
    for i in range(n):
        if pick == "urut":
            arr.append(i+1)
        elif pick == "reverse":
            arr.append(n-i)
        elif pick == "rand":
            arr.append(random.randint(1,500))
    return arr
List.SaveList("2000DataTerbalik.txt",listGenerator(2000))