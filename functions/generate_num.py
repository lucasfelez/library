import random
import time



def generate(how_many):
  estimated_time = round(0.02555 * how_many,2)
  
  nums = []
  # Generate a list of numbers from 0 to how_many (how_many is an integer)
  print("the estimared time is: " + str(estimated_time) + "seconds")
  time.sleep(3)
  start_time = time.time()
  for i in range(how_many):
    nums.append(random.randint(0,how_many*50))
    print("left to generate is:",how_many-len(nums)) # print the number of numbers left to generate
    time.sleep(0.02555) # to save CPU
    
  print("it took " + str(round(time.time()-start_time, 2)) + " seconds to generate " + str(how_many) + " numbers")
  return nums

  
  