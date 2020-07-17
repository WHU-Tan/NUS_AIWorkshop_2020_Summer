def num_ways_dp(n):
    dp = [0 for i in range(len(n) + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,len(n)+1):
        if 0 < int(n[i-2]+n[i-1]) <= 26 and n[i-2] != "0":
            if n[i-1] == "0":
                dp[i] = dp[i-2]
            else:
                dp[i] = dp[i-1] + dp[i-2] 
        elif n[i-1] != "0" :
            dp[i] = dp[i-1] 
    return dp[-1]

number = 1
numbers = []
while number != '0':
    number = input()
    numbers.append(num_ways_dp(number))

for i in range(0,len(numbers)-1):
    print(numbers[i])