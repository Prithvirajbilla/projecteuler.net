def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1


n = 30000*30000
primes_list = [2]
## 126410606437752
i = 3
while i <= (n ** 0.5 + 1):
  s = i ** 0.5 + 1
  flag = True
  for x in primes_list:
    if x <= s:
      if i%x == 0:
        flag = False
        break

  if flag:
    primes_list.append(i)

  i = i + 2

import itertools
store = 1000000000000000

print len(primes_list), primes_list[-1], primes_list[1500]

for subset in itertools.combinations(primes_list[:1500], 5):
  flag = True
  for prime in itertools.combinations(subset, 2):

    k1 = int("%d%d"%(prime[0], prime[1]))
    k2 = int("%d%d"%(prime[1], prime[0]))
    if k1 > primes_list[-1]:
      print k1

    if k2 > primes_list[-1]:
      print k2
    
    if binarySearch(primes_list, 0, len(primes_list)-1, k1) == -1 :
      flag = False
      break

    if binarySearch(primes_list, 0, len(primes_list)-1, k2) == -1:
      flag = False
      break
  if flag:
    s = sum(subset)
    print s, subset
    if s < store:
      store = s
      print store, subset
