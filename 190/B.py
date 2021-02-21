N, S, D = map(int, input().split())
for _ in range(N):
  X_N, Y_N = map(int, input().split())
  if X_N < S and Y_N > D:
    print("Yes")
    exit()
print("No")
