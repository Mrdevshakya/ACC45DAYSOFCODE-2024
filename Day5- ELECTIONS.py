# cook your dish here
def determine_winner(T, test_cases):
    results = []
    
    for i in range(T):
        votes_A, votes_B, votes_C = test_cases[i]
        
        if votes_A > 50:
            results.append("A")
        elif votes_B > 50:
            results.append("B")
        elif votes_C > 50:
            results.append("C")
        else:
            results.append("NOTA")
    
    return results

T = int(input())  

test_cases = []

for _ in range(T):
    test_cases.append(tuple(map(int, input().split())))

results = determine_winner(T, test_cases)

for result in results:
    print(result)