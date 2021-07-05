import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + " mil secs")
        return result
    return wrapper
