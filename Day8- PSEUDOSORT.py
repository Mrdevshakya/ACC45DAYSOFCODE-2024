def is_pseudo_sorted(arr):
    n = len(arr)
    disorder_positions = []

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            disorder_positions.append(i)


    if len(disorder_positions) == 0:
        return True


    if len(disorder_positions) > 1:
        return False

    i = disorder_positions[0]
    arr[i], arr[i + 1] = arr[i + 1], arr[i]


    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True

T = int(input())


for _ in range(T):
    
    N = int(input())

    A = list(map(int, input().split()))
    
    if is_pseudo_sorted(A):
        print("YES")
    else:
        print("NO")