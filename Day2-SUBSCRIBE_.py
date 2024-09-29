# cook your dish here
t=int(input()) 
for _ in range(t):
    n,x=map(int,input().split())
    subscription=(n+5)//6 
    total_cost=subscription*x 
    print(total_cost)
