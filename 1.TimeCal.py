import time

start_time = time.time()
for x in range(1000000):
    print("Hello world")
print("--- %s seconds ---" % (time.time() - start_time))