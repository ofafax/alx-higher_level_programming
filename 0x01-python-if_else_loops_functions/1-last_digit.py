mport random
number = random.randint(-10000, 10000)
lst_num = (number) % 10
if number > 5:
    print(f"Last digit of {number} is {lst_num} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {lst_num} and is 0")
else:
    print(f"Last digit of {number} is {lst_num} and is less than 6 and not 0")
