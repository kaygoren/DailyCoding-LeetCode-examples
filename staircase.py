# N -> number of stairs, X -> list of steps that can be token at a time
def numOfWays(N, X):
  if N == 0:
    return 1
  ways = [0]*(N+1)
  ways[0] = 1

  for i in range(1, N+1):
    total = 0
    for j in X:
      if i-j >= 0:
        total += ways[i-j]
    ways[i] = total
  return ways[N]

if __name__ == '__main__':
    print(numOfWays(4,[1,3,5]))
