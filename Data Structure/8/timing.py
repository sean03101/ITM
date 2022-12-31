import random, time

import selection
#import solution as selection

def getTiming(algname, alg, a, k):
  start_time = time.perf_counter()
  answer = alg(a, k)
  stop_time = time.perf_counter()
  print("%s returns as k-th element %s in %s microseconds" %
        (algname, answer, (stop_time - start_time) * 1000000.0))

a = [ "Hi", "ITM411", "ITM512", "ITM421", "SeoulTech", "ITM"]
getTiming("select", selection.select, a, 3)
getTiming("quick_select", selection.quick_select, a, 3)

b = random.sample(range(10000000), 1000000)
getTiming("select", selection.select, b, 54321)
getTiming("quick_select", selection.quick_select, b, 54321)

