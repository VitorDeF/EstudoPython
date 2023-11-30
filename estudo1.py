class BaseCalc:

    # return sum of two numbers
    def sum(a, b):
        return a+b

    # return the subtraction of two numbers
    def sub(a, b):
        return a-b

    # return the rest of the division of two numbers
    def rest(a, b):
        while(a>b):
            a = a - b
        return a

    # return the multiply of two numbers
    def mult(a,b):
        for i in range(0,b):
            a+=a
        return a
            

# functions execution
print(BaseCalc.sum(1,5))
print(BaseCalc.rest(10,3))
print(BaseCalc.mult(5,4))