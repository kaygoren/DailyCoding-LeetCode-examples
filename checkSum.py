
def checkSumEqual(arr, k):
    temp_arr = []
    for i in arr:
        if (k-i) in temp_arr:
            return True
        temp_arr.append(i)
    return False


arr = [10, 15, 3, 7]
k = 17
print(checkSumEqual(arr, k))
