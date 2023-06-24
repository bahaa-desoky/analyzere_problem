# Assumption Note: for this problem, I assume there is no bad input, as the input has been explicitly specified.
# In case we needed to account for bad input, having try-except blocks or if checks would be helpful.

import sys

class Compute:
  def __init__(self, threshold, limit) -> None:
    self.threshold = float(threshold)
    self.limit = float(limit)
  
  def printOutput(self) -> None:
    sumSoFar = 0
    for line in sys.stdin:     
      value = float(line.strip())
      thresholdValue = max(0, value - self.threshold)
      limitValue = min(thresholdValue, self.limit)
      sumSoFar += limitValue
      self.limit -= limitValue
      print(limitValue)
    print(sumSoFar)
    

if __name__ == '__main__':   
  compute = Compute(sys.argv[1], sys.argv[2]) 
  compute.printOutput()
 
