"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.


queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12"""
# i = 1
# list1 = []
# list2 = []


# def queue_time(customers, n):
#     if n == 1:
#         summ_time = sum(customers)
#         return print(summ_time)
#     else:
#         for i in customers:
#             if sum(list1) <= sum(list2):
#                 list1.append(i)
#             else:
#                 list2.append(i)
#     if sum(list1) <= sum(list2):
#         return print(sum(list2))
#     else:
#         return print(sum(list1))
#         # x = {i : customers[n] for i in range(n)}

def queue_time(customers, n):
    qn = [0] * n
    for c in customers:
        qn = sorted(qn)
        qn[0] += c

    return max(qn)

if __name__ == '__main__':
    queue_time([2,2,3,3,4,4], 10)
