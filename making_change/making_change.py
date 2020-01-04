#!/usr/bin/python

import sys

def making_change(amount, denominations):
  if amount < 0:
    return 0
  if amount == 0:
    return 1
  i = 0
  change_methods = 0
  for i in range(len(denominations)):
    change_methods += making_change((amount - denominations[i]), denominations)
    print(change_methods)
  return change_methods



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
