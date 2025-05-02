def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# it's iterating from 1 to 19
# 2. When is the function meant to print "You got it"?
# it should print when i=20 but range is 1 to 20 and 20 is excluded.
# 3. What are your assumptions about the value of i?
# final value of i will be the 19