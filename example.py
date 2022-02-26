# def solution(number):
#    sum_numbers = 0
#    for i in range(0, number):
#        if i % 3 == 0 or i % 5 == 0:
#            sum_numbers += i
#
#        elif i == 0:
#            print('return 0 ')
#    return sum_numbers
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    sum_2 = sum(numbers[:2])
    return print(sum_2)

if __name__ == '__main__':
    sum_two_smallest_numbers([19, 5, 42, 2, 77])
