import time

def timed_fn(fn):
    start = time.time()
    fn()
    duration = time.time() - start
    return duration

def average_run(fn):
    times = [timed_fn(fn) for x in range(10)]
    # throw out top
    times.remove(max(times))    
    # throw out bottom
    times.remove(min(times))
    return sum(times) / len(times)