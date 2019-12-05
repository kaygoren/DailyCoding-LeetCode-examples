''' This problem was asked by Uber.

Given an array of integers,return a new array such that 
each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].'''


def multWithOthers(lst):
  len_lst = len(lst)
  prod = 1
  result = [0]*len_lst

  for i in range(len_lst):
    prod *= lst[i]

  for i in range(len_lst):
    result[i] = (int)(prod/lst[i])

  return result

# Solution without using division
def multWithOthersWithoutDivision(lst):

  len_lst = len(lst)

  left = [1]*(len_lst+1)
  right =[1]*(len_lst+1)
  result = [0]*len_lst

  for i in range(len_lst):
    left[i+1] = lst[i]*left[i]

  for i in range(len_lst-1, -1, -1):
    right[i] = lst[i]*right[i+1]

  for i in range(len_lst):
    result[i]=left[i]*right[i+1]

  return result
