import sys
import insertionSort
import List
import timeit
import execution
import time
import os

if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    dataCountTime = []
    data = ["100DataTerbalik.txt","100DataUrut.txt","10Data.txt","100Data.txt", "500Data.txt", "1000Data.txt", "1500Data.txt", "5000DataTerbalik.txt" ]
    for i in data:
        dataTime = []
        print("=============================================")
        if i == "100DataTerbalik.txt":
            print("WORST CASE")
        elif i == "100DataUrut.txt":
            print("BEST CASE")
        elif i == "5000DataTerbalik.txt":
            print("WORSE CASE")
        arr = List.LoadList(i)
        print("Banyak data : {}".format(len(arr)))
    #iterative
        start = timeit.default_timer()
        insertionSortIterative(arr)
        print(arr)   
        dataTime.append("{:f}".format(execution.timeExceution("Iterative selection sort", start)))
    # recursive section
        arr = List.LoadList(i)
        start = timeit.default_timer()
        insertionSortRecursive(arr, 0)
        print(arr)
        dataTime.append("{:f}".format(execution.timeExceution("Iterative selection sort", start)))
