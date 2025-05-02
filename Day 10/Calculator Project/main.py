
import art

def calculator():

    print(art.logo)

    acc=True
    def add(n1, n2):
        return n1 + n2

    def sub(n1, n2):
        return n1 - n2

    def mul(n1, n2):
        return n1 * n2

    def div(n1, n2):
        return n1 / n2

    symbols = {"+": add,
               "-": sub,
               "*": mul,
               "/": div, }

    num1 = float(input("Enter First Number: "))
    while acc:
        op = input("Enter Operation (+,-,*,/) : ")
        num2 = float(input("Enter a Number: "))
        answer = symbols[op](num1, num2)
        print(f"The {num1} {op} {num2} = {answer}.")
        ch=input(f"Do You want {answer} for further operations(y/n) : ").lower()
        if ch=="y":
            num1=answer
        else:
            print("\n"*20)
            calculator()

calculator()