# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


user_num = int(input("Enter your number: "))
save_num = user_num

prime_num = 2
prime_list = []
while user_num > prime_num:
    if user_num % prime_num == 0:
        prime_list.append(prime_num)
        user_num = user_num / prime_num
    else:
        prime_num += 1

if user_num == save_num:
    print('You entered a prime number.')
else: 
    prime_list.append(int(user_num))
    print(f'Prime multiples for the number {save_num} are {prime_list}.')


