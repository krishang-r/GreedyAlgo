# Question
'''
A farmer used to cultivate vegetables in his field and sell them in a market 50 km away. The farmer has some containers of certain fixed capacities. Out of these, exactly one will be available every day and the remaining will be under circulation in the market.  Depending on the capacity of the container available on a particular day, the farmer has to maximize his daily profit. Write a program to do this with the following input and output requirements. 

Input Format

Read the number of vegetable types (n) available on a particular day in line 1 [1,2,..,n]

Read the weight of each vegetable type in the next n lines

Read the profit that he gets by selling each vegetable type in the subsequent n lines

Read the capacity of the container available on that day

Output Format

Print the total profit (Rounded off to 2 decimal places) that the farmer gets on that particular day
'''


def max_profit(weight, profit, capacity, num):
    profit_by_weight = []
    for i in range(num):
        profit_by_weight.append([profit[i]/weight[i],i])
    profit_by_weight.sort(reverse= True)
    max_profit = 0
    for j in range(num):
        indexed_weight = weight[profit_by_weight[j][1]]
        indexed_profit = profit[profit_by_weight[j][1]]
        if (capacity == 0):
            break
        elif (capacity >= indexed_weight):
            capacity -= indexed_weight
            max_profit += indexed_profit
        else:
            fractional_capacity = capacity/indexed_weight
            max_profit += indexed_profit * fractional_capacity
            capacity -= fractional_capacity * indexed_weight
    print(f'Maximum Profit: {max_profit:.2f}')




weight, profit = [], []
num = int(input("Enter number of objects: "))

for i in range(num):
    weight.append(int(input(f'Enter Weight of {i+1} object: ')))  

for j in range(num):
    profit.append(int(input(f'Enter profit of {j+1} object: ')))

capacity = int(input("Enter the capacity of the container: "))

max_profit(weight, profit, capacity, num)