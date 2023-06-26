# Note: for this problem, I assume there can be bad input. 
# I check to make sure the following is upheld:
# - the program is called with the correct number of arguments
# - limit and threshold arguments are between 0.0 and 1,000,000,000.0
# - each number in the input is between 0.0 and 1,000,000,000.0
# - we consume a maximum of 100 input lines
# Python raises a ValueError if any of the inputs/arguments are not convertible to a float, which I feel is sufficient

import sys

class Compute:
  '''Compute class as described in the README.md'''
  
  def __init__(self, threshold, limit) -> None:
    '''Initializes the threshold and limit values'''
    self.threshold = float(threshold)
    self.limit = float(limit)
    if not 0.0 <= self.threshold <= 1000000000.0 or not 0.0 <= self.limit <= 1000000000.0:
      raise Exception('Argument(s) are not within the required range')
  
  def printOutput(self) -> None:
    '''Prints the n+1 output lines where n is at most 100'''
    sumSoFar = 0
    lineCount = 0
    for line in sys.stdin:  
      if lineCount == 100:
        break   
      value = float(line.strip())
      if not 0.0 <= value <= 1000000000.0:
        raise Exception('Input(s) are not within the required range')
      
      thresholdValue = max(0, value - self.threshold)
      limitValue = min(thresholdValue, self.limit)
      print(limitValue)
      sumSoFar += limitValue
      self.limit -= limitValue
      lineCount += 1
    print(sumSoFar)
    

if __name__ == '__main__':
  if len(sys.argv) != 3:
    raise Exception('Incorrect number of args. Usage: compute.py <threshold> <limit>')
  
  compute = Compute(sys.argv[1], sys.argv[2]) 
  compute.printOutput()
 
