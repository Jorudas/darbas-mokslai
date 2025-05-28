# DEBUGINIMAS
# # Buggy Code: Print even numbers from a list.
# numbers = [1, 2, 3, 4, 5, 6]
# for i in range(len(numbers)):
#     # if numbers [i] % 2 == 0:   #Klaidinga eilutė if numbers % 2 == 0:	Teisinga eilutė if numbers [i] % 2 == 0:
# if numbers % 2 == 0:
#         print(numbers[i])




# #  DEBUGINIMAS
#         # Intention: Practice summing numbers in a list using a for loop
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers: #1      #nebuvo dvitaskio po numbers
#     total = total + num
# print("Sum is:", total)  # 2    # total su viena L



#  DEBUGINIMAS
# # Intention: Practice using conditionals to check even or odd numbers
# nums = [1, 2, 3, 4, 5]
# for i in nums:
#     if i % 2 == 0:      # 1       #dadejau ligybes zenkla
#         print(f"{i} is even")
#     else:              # 2        #dadejau dvitaski
#         print(f"{i} is odd")



# # Intention: Practice building a list of squares with a for loop
# squares = []
# for i in range(1, 6):   # 1       #dvitaskis dadetas po skliaustelio
#     squares.append(i * i)  # 2
# print("Squares:", squares)  # 3  #koreguota i squares





# # Intention: finding the maximum element in a list using loops
# numbers = [3, 7, 2, 9, 5]
# max_num = numbers[0]
# for n in numbers:
#     if n > max_num:                # is maziau pakeista i daugiau
#         max_num = n
# print("Max number is", max_num)    #po max uzdetas bruksnelis apacioje




# Intention: Practice using loops to calculate factorial of a number
# n = 5
# result = 1     # Pradedam nuo 1, nes daugyba nuo 0 visada duotu 0
# for i in range(1, n + 1):
#     result *= i
# print(f"Factorial of {n} is {result}")



# # Intention: Practice checking if a string is a palindrome
# s = "racecar"
# if s == s[::-1]:
#     print("Is a palindrome")      # sukeista vietomis printai
# else:
#     print("Not a palindrome")




# Intention: Practice summing even numbers in a range
# total = 0
# for i in range(1, 11):
#     if i % 2 == 1:
#         total += i
# print("Sum of even numbers:", total)







