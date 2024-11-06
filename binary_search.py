#the binary search algorithm 
def binary_search(list, target):

  first = 0
  last = len(list) - 1
  counter = 0 

  while first <= last:
    midpoint = (first + last)//2
    counter = counter + 1
    print("count is at:", counter)
    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1

  return None



#checking for a value from the table 
#printing it to the console
def verify(index):
  if index is not None:
    print("target found at index:", index)
  else:
    print("target not found in list")


numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)


result = binary_search(numbers, 6)
verify(result)



