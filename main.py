import sys
import insertionSort
import List
import timeit
import execution
import time
import os

if __name__ == "__main__":
    sys.setrecursionlimit(6000) 
    dataCountTime = []
    data = ["100DataTerbalik.txt","100DataUrut.txt","10Data.txt","100Data.txt", "500Data.txt", "1000Data.txt", "1500Data.txt", "5000DataTerbalik.txt","5000DataUrut.txt" ]
    # data = ["3000DataEqual.txt"]
    for i in data:
        dataTime = []
        print("=============================================")
        if i == "100DataTerbalik.txt" or i == "5000DataTerbalik.txt":
            print(i[:-4])
            print("WORST CASE")
        elif i == "100DataUrut.txt" or i == "5000DataUrut.txt":
            print(i[:-4])
            print("BEST CASE")
        else:
            print(i[:-4])
        arr = List.LoadList(i)
        print("Banyak data : {}".format(len(arr)))
    #iterative
        start = timeit.default_timer()
        insertionSort.insertionSortIterative(arr)
        print("=============================================")
        # print(arr)   
        dataTime.append("{:f}".format(execution.timeExcecution("Iterative selection sort", start)))
    # recursive section
        arr = List.LoadList(i)
        start = timeit.default_timer()
        insertionSort.insertionSortRecursive(arr, 0)
        print("=============================================")
        # print(arr)
        dataTime.append("{:f}".format(execution.timeExcecution("Recursive selection sort", start)))
