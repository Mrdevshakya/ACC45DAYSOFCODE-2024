# cook your dish here



from math import ceil



for T in range(int(input())):

    

    L,K = map(int, input().split())

    

    print(int(L % K != 0))
