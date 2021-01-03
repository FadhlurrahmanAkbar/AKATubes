import timeit
def timeExcecution(fname, start):
    stop = timeit.default_timer()
    execution_time = stop - start
    print("{} dieksekusi dalam {:f} detik".format(fname, execution_time))
    return execution_time