import time
import random

# Naive (cubic) maximum contiguous subsequence sum algorithm.
# seqStart and seqEnd represent the actual best sequence.
def maxSubSum1(a):
  maxSum = 0
  start = 0
  end = 0
  for i in range(len(a)):
    for j in range(i, len(a)):
      sum = 0
      for k in range(i, j+1):
        sum += a[k]
      if sum > maxSum:
        maxSum = sum
        start = i
        end   = j
  return maxSum, start, end

# Quadratic maximum contiguous subsequence sum algorithm.
# seqStart and seqEnd represent the actual best sequence.
def maxSubSum2(a):
  maxSum = 0
  start = 0
  end = 0
  for i in range(len(a)):
    sum = 0
    for j in range(i, len(a)):
      sum += a[j]
      if sum > maxSum:
        maxSum = sum
        start = i
        end   = j
  return maxSum, start, end

# Recursive maximum contiguous subsequence sum algorithm.
# Finds maximum sum in subarray spanning a[left..right].
def maxSumRec(a, left, right):
  if left == right:  # base case
    if a[left] > 0:
      return a[left]
    else:
      return 0
  else:
    center = (left + right) // 2
    maxLeftSum  = maxSumRec(a, left, center)
    maxRightSum = maxSumRec(a, center + 1, right)
    
    maxLeftBorderSum = 0
    maxRightBorderSum = 0
    leftBorderSum = 0
    rightBorderSum = 0
    
    for i in range(center, left-1, -1):
      leftBorderSum += a[i]
      if leftBorderSum > maxLeftBorderSum:
        maxLeftBorderSum = leftBorderSum
    for i in range(center + 1, right+1):
      rightBorderSum += a[i]
      if rightBorderSum > maxRightBorderSum:
        maxRightBorderSum = rightBorderSum
    return max(maxLeftSum, maxRightSum, maxLeftBorderSum + maxRightBorderSum)

# Driver 
def maxSubSum3(a):
  if len(a) > 0:
    return maxSumRec(a, 0, len(a) - 1)
  else:
    return 0

def getTimingInfo(n, alg):
  startTime = time.time()
  totalTime = 0

  rounds = 0
  while totalTime < 4.0:
    test = [ random.randrange(100) for i in range(n) ]
      
    if alg == 1:
      maxSubSum1(test)
    elif alg == 2:
      maxSubSum2(test)
    else:
      maxSubSum3(test)

    totalTime = time.time() - startTime
    rounds += 1
  
  print("Algorithm #%d N = %6d time = %9d microsecs" %
        (alg, n, totalTime * 1000000 // rounds))

def time_comparison():
  n = 10
  while n <= 1000000:
    for alg in range(1, 4):
      if alg != 1 or n < 5000:
        getTimingInfo(n, alg)
    n *= 10

def simple_demo():
  A = [ 4, -3, 5, -2, -1, 2, 6, -2 ]
  res1, start1, end1 = maxSubSum1(A)
  res2, start2, end2 = maxSubSum2(A)
  res3 = maxSubSum3(A)
  print("Alg 1: Max sum is %d; it goes from %d to %d" % (res1, start1, end1))
  print("Alg 2: Max sum is %d; it goes from %d to %d" % (res2, start2, end2))
  print("Alg 3: Max sum is %d" % res3)
    
simple_demo()
time_comparison()
