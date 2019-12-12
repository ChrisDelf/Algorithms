#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):

  # we cannot have negative cookies left or else we have an infinite loop
  if n < 0:
    return 0
  if n == 0:
    return 1
  print(f"{cache}")
  if cache == None:
    cache = [0 for i in range(n + 1)]
  if cache[n] > 0:
    print(f"{cache[n]}")
    return cache[n]

  cookie_methods = 0

# this loops through the range of cookie eating methods 1 , 2, 3 eaten at a time
  for i in range(1, 4):
    print(f"Cache in for loop {cache}")
    # print(i)
    #Fractals we call the function within it self with the new n value.
    cookie_methods += eating_cookies(n - i, cache)
  cache[n] = cookie_methods


  return cookie_methods
print(eating_cookies(3))
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
